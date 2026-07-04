from __future__ import annotations

from .utils.other import API_URL, HEADERS_MAIN
from .handlers import fetch, requestExceptionHandler
from .classes.Exceptions import accountError, authDataError
from .classes.Objects import Points, Balances, Stats

#############################################################################
#     Module for working with your account on Portals Gift Marketplace.     #
#############################################################################

async def myPoints(authData: str = "") -> Points:
    """
    Retrieves the user's Portals Points information.

    Args:
        authData (str): The authentication data required for the API request.

    Returns:
        Points: An instance of Points containing the user's points information if the request is successful.

    Raises:
        authDataError: If authData is not provided.
        requestError: If the API request fails.
    """
    URL = API_URL + "points/me"

    if authData == "":
        raise authDataError("portalsmp: myPoints(): Error: authData is required")

    HEADERS = {**HEADERS_MAIN, "Authorization": authData}

    response = await fetch(method="GET", url=URL, headers=HEADERS, impersonate="chrome110")
    
    requestExceptionHandler(response, "myPoints")

    return Points(response.json())

async def myStats(authData: str = "") -> Stats:
    """
    Retrieves the user's statistics.

    Args:
        authData (str): The authentication data required for the API request.

    Returns:
        Stats: An instance of Stats containing the user's statistics if the request is successful.

    Raises:
        authDataError: If authData is not provided.
        requestError: If the API request fails.
    """
    URL = API_URL + "users/profile/stats"

    if authData == "":
        raise authDataError("aportalsmp: myStats(): Error: authData is required")

    HEADERS = {**HEADERS_MAIN, "Authorization": authData}

    response = await fetch(method="GET", url=URL, headers=HEADERS, impersonate="chrome110")

    requestExceptionHandler(response, "myStats")

    return Stats(response.json())

async def myBalances(authData: str = "") -> Balances:
    """
    Retrieves the user's balances.

    Args:
        authData (str): The authentication data required for the API request.

    Returns:
        Balances: An instance of Balances containing the user's balances if the request is successful.

    Raises:
        authDataError: If authData is not provided.
        requestError: If the API request fails.
    """
    URL = API_URL + "users/wallets/"

    if authData == "":
        raise authDataError("aportalsmp: myBalances(): Error: authData is required")

    HEADERS = {**HEADERS_MAIN, "Authorization": authData}

    response = await fetch(method="GET", url=URL, headers=HEADERS, impersonate="chrome110")

    requestExceptionHandler(response, "myBalances")

    return Balances(response.json())

# TON withdrawal moved to wallet.py. Re-exported here for backwards compatibility
# (`from aportalsmp.account import withdrawPortals` still works).
from .wallet import withdrawGram, withdrawTon, withdrawPortals  # noqa: E402,F401