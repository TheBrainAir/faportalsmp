from __future__ import annotations

from .utils.other import API_URL, HEADERS_MAIN
from .handlers import fetch, requestExceptionHandler
from .classes.Exceptions import authDataError, accountError

#######################################################################
#     Referral & cashback programmes on Portals Gift Marketplace.     #
#######################################################################

# =================== Referrals ===================

async def referralInfo(authData: str = "") -> dict:
    """
    Your referral programme summary — code, earnings and progress
    (``GET /referral/info``).

    Args:
        authData (str): The authentication data required for the API request.

    Returns:
        dict: The raw referral info payload.

    Raises:
        authDataError: If authData is not provided.
        requestError: If the API request fails.
    """
    return await _get("referral/info", "referralInfo", authData)

async def referralFriends(offset: int = 0, limit: int = 20, authData: str = "") -> dict:
    """
    The users you referred (``GET /referral/friends``).

    Args:
        offset (int): Pagination offset. Defaults to 0.
        limit (int): Maximum number of entries. Defaults to 20.
        authData (str): The authentication data required for the API request.

    Returns:
        dict: The raw friends/referrals payload.

    Raises:
        authDataError: If authData is not provided.
        requestError: If the API request fails.
    """
    return await _get(f"referral/friends?offset={offset}&limit={limit}", "referralFriends", authData)

async def referralLevels(authData: str = "") -> dict:
    """
    Referral tiers/levels and their rewards (``GET /referral/levels``)."""
    return await _get("referral/levels", "referralLevels", authData)

async def applyReferral(code: str = "", authData: str = "") -> dict:
    """
    Apply a referral code to your account (``POST /referral/apply``).

    Args:
        code (str): The referral code to apply.
        authData (str): The authentication data required for the API request.

    Returns:
        dict: The raw response.

    Raises:
        authDataError: If authData is not provided.
        accountError: If code is not provided.
        requestError: If the API request fails.
    """
    if not code:
        raise accountError("aportalsmp: applyReferral(): Error: code is required")
    return await _post("referral/apply", "applyReferral", authData, payload={"code": code})

async def claimReferral(authData: str = "") -> dict:
    """
    Claim your accumulated referral rewards (``POST /referral/claim``)."""
    return await _post("referral/claim", "claimReferral", authData)

# =================== Cashback ===================

async def cashbackInfo(authData: str = "") -> dict:
    """
    Your cashback summary — current level, accrued and claimable amounts
    (``GET /cashback/info``)."""
    return await _get("cashback/info", "cashbackInfo", authData)

async def cashbackLevels(authData: str = "") -> dict:
    """
    Cashback tiers/levels and their rates (``GET /cashback/levels``)."""
    return await _get("cashback/levels", "cashbackLevels", authData)

async def claimCashback(authData: str = "") -> dict:
    """
    Claim your accumulated cashback (``POST /cashback/claim``)."""
    return await _post("cashback/claim", "claimCashback", authData)

# =================== Helpers ===================

async def _get(path: str, func_name: str, authData: str) -> dict:
    if not authData:
        raise authDataError(f"aportalsmp: {func_name}(): Error: authData is required")
    HEADERS = {**HEADERS_MAIN, "Authorization": authData}
    response = await fetch(method="GET", url=API_URL + path, headers=HEADERS, impersonate="chrome110")
    requestExceptionHandler(response, func_name)
    return response.json()

async def _post(path: str, func_name: str, authData: str, payload: dict = None) -> dict:
    if not authData:
        raise authDataError(f"aportalsmp: {func_name}(): Error: authData is required")
    HEADERS = {**HEADERS_MAIN, "Authorization": authData}
    response = await fetch(method="POST", url=API_URL + path, json=payload, headers=HEADERS, impersonate="chrome110")
    requestExceptionHandler(response, func_name)
    try:
        return response.json()
    except Exception:
        return {}
