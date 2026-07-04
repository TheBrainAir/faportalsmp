from __future__ import annotations

from urllib.parse import quote_plus

from .utils.other import API_URL, HEADERS_MAIN
from .handlers import fetch, requestExceptionHandler
from .classes.Exceptions import accountError, authDataError, tradingError
from .classes.Objects import (
    DepositInfo,
    DepositStatus,
    WithdrawStatus,
    WalletLimits,
    WalletHistory,
)

###############################################################################
#     Module for GRAM deposits & withdrawals on Portals Gift Marketplace.     #
#                                                                             #
#     GRAM is the native coin (moved on the TON network); amounts are in      #
#     GRAM, while addresses / TON Connect / liteservers are TON-network.      #
###############################################################################

# 1 GRAM = 10^9 nano
_NANO = 1_000_000_000


# ============================ Deposit ============================

async def deposit(amount: float = 0, mnemonic: str | list = "", address: str = "",
                  wallet_version: str = "v4r2", authData: str = "") -> DepositInfo:
    """
    Create a GRAM deposit to your Portals balance.

    A deposit is a native GRAM transfer (on the TON network) to the Portals
    deposit wallet carrying a text comment equal to the deposit id (that's how
    the marketplace matches the incoming transfer to your account). This function
    always mints the deposit id via ``POST /deposits`` and returns a
    :class:`DepositInfo` describing where and how to send the GRAM.

    Two modes:
      * **Intent (default)** — pass only ``authData``. You (or your bot) send the
        GRAM yourself to ``DepositInfo.address`` with comment ``DepositInfo.comment``.
      * **Auto-send** — also pass ``mnemonic`` (+ ``amount``). The library signs and
        broadcasts the transfer for you via pytoniq. ``DepositInfo.sent_tx`` will
        describe the sent transfer.

    Args:
        amount (float): Amount of GRAM to deposit. Required for auto-send.
        mnemonic (str | list): 24-word wallet mnemonic (string or list). If given,
            enables auto-send. Never logged or transmitted anywhere except signing.
        address (str): Override the destination address (normally taken from the API).
        wallet_version (str): Wallet contract version for auto-send: "v4r2" (default),
            "v3r2", "v3r1", "v5r1".
        authData (str): The authentication data required for the API request.

    Returns:
        DepositInfo: deposit id, destination address, amount and comment.

    Raises:
        authDataError: If authData is not provided.
        accountError: If auto-send is requested but amount/address are missing, or
            the TON SDK is not installed.
        requestError: If the API request fails.
    """
    if not authData:
        raise authDataError("aportalsmp: deposit(): Error: authData is required")

    URL = API_URL + "deposits"
    HEADERS = {**HEADERS_MAIN, "Authorization": authData}

    response = await fetch(method="POST", url=URL, headers=HEADERS, impersonate="chrome110")

    requestExceptionHandler(response, "deposit")

    try:
        payload = response.json()
    except Exception:
        payload = (response.text or "").strip().strip('"')

    info = DepositInfo(payload)

    if mnemonic:
        if not amount or float(amount) <= 0:
            raise accountError("aportalsmp: deposit(): Error: amount is required for auto-send")
        destination = address or info.address
        if not destination:
            raise accountError(
                "aportalsmp: deposit(): Error: destination address was not returned by the API; "
                "pass address=... explicitly")
        comment = info.comment
        if not comment:
            raise accountError("aportalsmp: deposit(): Error: deposit id/comment missing from API response")
        sent = await _send_ton_comment(destination, float(amount), str(comment), mnemonic, wallet_version)
        info.__dict__["_sent_tx"] = sent

    return info


async def depositStatus(ids: str | list = "", authData: str = "") -> list[DepositStatus]:
    """
    Poll the status of one or more deposits (``GET /deposits/statuses``).

    Args:
        ids (str | list): A deposit id or list of deposit ids to check. If empty,
            recent deposits are returned.
        authData (str): The authentication data required for the API request.

    Returns:
        list[DepositStatus]: Status entries for the requested deposits.

    Raises:
        authDataError: If authData is not provided.
        requestError: If the API request fails.
    """
    if not authData:
        raise authDataError("aportalsmp: depositStatus(): Error: authData is required")

    URL = API_URL + "deposits/statuses"
    URL += _ids_query(ids)

    HEADERS = {**HEADERS_MAIN, "Authorization": authData}

    response = await fetch(method="GET", url=URL, headers=HEADERS, impersonate="chrome110")

    requestExceptionHandler(response, "depositStatus")

    return _wrap_statuses(response.json(), DepositStatus)


# ============================ Withdraw ============================

async def withdrawGram(amount: float = 0, wallet: str = "", authData: str = "") -> str | None:
    """
    Withdraw GRAM from your Portals balance to an external wallet address
    (``POST /users/wallets/withdraw``).

    Args:
        amount (float): The amount of GRAM to withdraw.
        wallet (str): The external TON address to withdraw to.
        authData (str): The authentication data required for the API request.

    Returns:
        str | None: The id of the withdrawal if successful.

    Raises:
        accountError: If amount or wallet is not provided.
        authDataError: If authData is not provided.
        requestError: If the API request fails.
    """
    URL = API_URL + "users/wallets/withdraw"

    if not amount:
        raise accountError("aportalsmp: withdrawGram(): Error: amount is required")
    if not wallet:
        raise accountError("aportalsmp: withdrawGram(): Error: wallet is required")
    if not authData:
        raise authDataError("aportalsmp: withdrawGram(): Error: authData is required")

    HEADERS = {**HEADERS_MAIN, "Authorization": authData}

    PAYLOAD = {
        "amount": str(amount),
        "external_address": wallet,
    }

    response = await fetch(method="POST", url=URL, json=PAYLOAD, headers=HEADERS, impersonate="chrome110")

    requestExceptionHandler(response, "withdrawGram")

    return response.json().get("id", None) if 200 <= response.status_code < 300 else None


# Backwards-compatible aliases (older / neutral names for withdrawGram).
withdrawPortals = withdrawGram
withdrawTon = withdrawGram


async def withdrawStatus(ids: str | list = "", authData: str = "") -> list[WithdrawStatus]:
    """
    Poll the status of one or more withdrawals
    (``GET /users/wallets/withdrawals/statuses``).

    Args:
        ids (str | list): A withdrawal id or list of withdrawal ids. If empty,
            recent withdrawals are returned.
        authData (str): The authentication data required for the API request.

    Returns:
        list[WithdrawStatus]: Status entries for the requested withdrawals.

    Raises:
        authDataError: If authData is not provided.
        requestError: If the API request fails.
    """
    if not authData:
        raise authDataError("aportalsmp: withdrawStatus(): Error: authData is required")

    URL = API_URL + "users/wallets/withdrawals/statuses"
    URL += _ids_query(ids)

    HEADERS = {**HEADERS_MAIN, "Authorization": authData}

    response = await fetch(method="GET", url=URL, headers=HEADERS, impersonate="chrome110")

    requestExceptionHandler(response, "withdrawStatus")

    return _wrap_statuses(response.json(), WithdrawStatus)


# ============================ Wallet info ============================

async def walletLimits(authData: str = "") -> WalletLimits:
    """
    Retrieve deposit/withdrawal limits and fees (``GET /users/wallets/limits``).

    Args:
        authData (str): The authentication data required for the API request.

    Returns:
        WalletLimits: min/max amounts, daily limit and fees.

    Raises:
        authDataError: If authData is not provided.
        requestError: If the API request fails.
    """
    if not authData:
        raise authDataError("aportalsmp: walletLimits(): Error: authData is required")

    URL = API_URL + "users/wallets/limits"
    HEADERS = {**HEADERS_MAIN, "Authorization": authData}

    response = await fetch(method="GET", url=URL, headers=HEADERS, impersonate="chrome110")

    requestExceptionHandler(response, "walletLimits")

    return WalletLimits(response.json())


async def walletHistory(offset: int = 0, limit: int = 20, authData: str = "") -> list[WalletHistory]:
    """
    Retrieve the wallet transaction history (``GET /users/wallets/history``).

    Args:
        offset (int): Pagination offset. Defaults to 0.
        limit (int): Maximum number of entries to return. Defaults to 20.
        authData (str): The authentication data required for the API request.

    Returns:
        list[WalletHistory]: Wallet history entries (deposits, withdrawals, trades).

    Raises:
        authDataError: If authData is not provided.
        requestError: If the API request fails.
    """
    if not authData:
        raise authDataError("aportalsmp: walletHistory(): Error: authData is required")

    URL = API_URL + f"users/wallets/history?offset={offset}&limit={limit}"
    HEADERS = {**HEADERS_MAIN, "Authorization": authData}

    response = await fetch(method="GET", url=URL, headers=HEADERS, impersonate="chrome110")

    requestExceptionHandler(response, "walletHistory")

    data = response.json()
    items = data.get("history", data.get("transactions", data)) if isinstance(data, dict) else data
    return [WalletHistory(item) for item in items] if isinstance(items, list) else []


# ============================ Helpers ============================

def _ids_query(ids: str | list) -> str:
    """Build a ``?ids=a&ids=b`` query string from a single id or list of ids."""
    if not ids:
        return ""
    if isinstance(ids, str):
        ids = [ids]
    parts = [f"ids={quote_plus(str(i))}" for i in ids if i]
    return ("?" + "&".join(parts)) if parts else ""


def _wrap_statuses(data, cls):
    """Normalise the various shapes the statuses endpoints may return into a list."""
    if isinstance(data, list):
        rows = data
    elif isinstance(data, dict):
        rows = data.get("statuses") or data.get("results") or data.get("deposits") \
            or data.get("withdrawals") or []
        if not rows and ("id" in data or "status" in data):
            rows = [data]
    else:
        rows = []
    return [cls(row) for row in rows]


async def _send_ton_comment(address: str, amount: float, comment: str,
                            mnemonic: str | list, wallet_version: str = "v4r2"):
    """
    Sign and broadcast a native GRAM transfer with a text comment using pytoniq.

    This is the auto-send path used by :func:`deposit`. It connects to public
    TON liteservers (no API key needed) and sends ``amount`` GRAM to ``address``
    with ``comment`` as the transfer message body.
    """
    try:
        from pytoniq import LiteBalancer, WalletV4R2, WalletV3R2, WalletV3R1, WalletV5R1
        from pytoniq_core import begin_cell
    except ImportError as exc:  # pragma: no cover
        raise accountError(
            "aportalsmp: deposit(): Error: auto-send requires pytoniq. "
            "Reinstall the library (pip install -U faportalsmp) or run: pip install pytoniq") from exc

    if isinstance(mnemonic, str):
        mnemonic = mnemonic.split()

    wallets = {
        "v4r2": WalletV4R2,
        "v3r2": WalletV3R2,
        "v3r1": WalletV3R1,
        "v5r1": WalletV5R1,
    }
    WalletCls = wallets.get(str(wallet_version).lower(), WalletV4R2)

    nano = int(round(float(amount) * _NANO))

    # Standard TON text comment: op=0 (uint32) followed by the UTF-8 string.
    body = begin_cell().store_uint(0, 32).store_string(str(comment)).end_cell()

    provider = LiteBalancer.from_mainnet_config(trust_level=2)
    await provider.start_up()
    try:
        wallet = await WalletCls.from_mnemonic(provider, mnemonic)
        await wallet.transfer(destination=address, amount=nano, body=body)
    finally:
        await provider.close_all()

    return {"status": "sent", "amount": float(amount), "to": address, "comment": str(comment)}
