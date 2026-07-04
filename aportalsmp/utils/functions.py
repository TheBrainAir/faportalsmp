from __future__ import annotations

from urllib.parse import quote_plus
import re

def cap(text) -> str:
    words = re.findall(r"\w+(?:'\w+)?", text)
    for word in words:
        if len(word) > 0:
            cap = word[0].upper() + word[1:]
            text = text.replace(word, cap, 1)
    return text

def listToURL(gifts: list) -> str:
    return '%2C'.join(quote_plus(cap(gift)) for gift in gifts)

def activityListToURL(activity: list) -> str:
    return '%2C'.join(activity)

def toShortName(gift_name: str) -> str:
    return gift_name.replace(" ", "").replace("'", "").replace("’", "").replace("-", "").lower()

def resolve_collection_id(gift_name: str) -> str | None:
    """
    Resolve a gift/collection name to its Portals collection UUID robustly.

    Handles differences in capitalization, straight vs. curly apostrophes
    (e.g. "Durov's Cap" vs "Durov’s Cap") and hyphen casing
    (e.g. "Jack-in-the-Box" vs "Jack-In-The-Box"). Returns None if unknown.
    """
    # imported lazily to avoid an import cycle (collections_ids imports this module)
    from .collections_ids import collections_ids, short_name_ids
    if gift_name in collections_ids:
        return collections_ids[gift_name]
    capped = cap(gift_name)
    if capped in collections_ids:
        return collections_ids[capped]
    return short_name_ids.get(toShortName(gift_name))

def convertForListing(nft_id: str = "", price: float = 0):
    return {"nft_id": nft_id, "price": str(price)}

def convertForBuying(nft_id: str = "", price: float = 0):
    return {"id": nft_id, "price": str(price)}