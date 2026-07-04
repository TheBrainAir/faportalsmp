from __future__ import annotations

from .utils.other import API_URL, HEADERS_MAIN
from .handlers import fetch, requestExceptionHandler
from .classes.Exceptions import authDataError, tradingError

##########################################################################
#     Premarket orders on Portals Gift Marketplace (collateral-based).   #
##########################################################################

async def premarketCollaterals(authData: str = "") -> dict:
    """
    Collateral options available for premarket orders
    (``GET /premarket/orders/collaterals``).

    Args:
        authData (str): The authentication data required for the API request.

    Returns:
        dict: The raw collaterals payload.

    Raises:
        authDataError: If authData is not provided.
        requestError: If the API request fails.
    """
    return await _get("premarket/orders/collaterals", "premarketCollaterals", authData)

async def premarketCollections(authData: str = "") -> dict:
    """
    Collections that currently support premarket orders
    (``GET /premarket/orders/collections``)."""
    return await _get("premarket/orders/collections", "premarketCollections", authData)

async def premarketPreviewGift(payload: dict = None, authData: str = "") -> dict:
    """
    Preview adding a gift to a premarket order before committing
    (``POST /premarket/orders/preview-gift``).

    The premarket body is collateral-based and marketplace-defined; pass the
    request body as ``payload`` (e.g. ``{"nft_id": ..., "collateral": ...}``).

    Args:
        payload (dict): The preview request body.
        authData (str): The authentication data required for the API request.

    Returns:
        dict: The raw preview payload.

    Raises:
        authDataError: If authData is not provided.
        tradingError: If payload is not provided.
        requestError: If the API request fails.
    """
    if not payload:
        raise tradingError("aportalsmp: premarketPreviewGift(): Error: payload is required")
    return await _post("premarket/orders/preview-gift", "premarketPreviewGift", authData, payload)

async def premarketAddGift(payload: dict = None, authData: str = "") -> dict:
    """
    Add a gift to a premarket order (``POST /premarket/orders/add-gift``).

    The premarket body is collateral-based and marketplace-defined; pass the
    request body as ``payload``.

    Args:
        payload (dict): The add-gift request body.
        authData (str): The authentication data required for the API request.

    Returns:
        dict: The raw response.

    Raises:
        authDataError: If authData is not provided.
        tradingError: If payload is not provided.
        requestError: If the API request fails.
    """
    if not payload:
        raise tradingError("aportalsmp: premarketAddGift(): Error: payload is required")
    return await _post("premarket/orders/add-gift", "premarketAddGift", authData, payload)

# =================== Helpers ===================

async def _get(path: str, func_name: str, authData: str) -> dict:
    if not authData:
        raise authDataError(f"aportalsmp: {func_name}(): Error: authData is required")
    HEADERS = {**HEADERS_MAIN, "Authorization": authData}
    response = await fetch(method="GET", url=API_URL + path, headers=HEADERS, impersonate="chrome110")
    requestExceptionHandler(response, func_name)
    return response.json()

async def _post(path: str, func_name: str, authData: str, payload: dict) -> dict:
    if not authData:
        raise authDataError(f"aportalsmp: {func_name}(): Error: authData is required")
    HEADERS = {**HEADERS_MAIN, "Authorization": authData}
    response = await fetch(method="POST", url=API_URL + path, json=payload, headers=HEADERS, impersonate="chrome110")
    requestExceptionHandler(response, func_name)
    try:
        return response.json()
    except Exception:
        return {}
