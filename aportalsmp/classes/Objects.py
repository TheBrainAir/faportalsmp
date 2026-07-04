from __future__ import annotations

from ..utils.functions import cap

class PortalsGift:
    def __init__(self, data: dict):
        self.__dict__ = data
    
    def toDict(self):
        return self.__dict__
    
    @property
    def id(self):
        return self.__dict__.get("id", None)
    
    @property
    def tg_id(self):
        return self.__dict__.get("external_collection_number", None)
    
    @property
    def collection_id(self):
        return self.__dict__.get("collection_id", None)

    @property
    def name(self):
        return self.__dict__.get("name", None)

    @property
    def photo_url(self):
        return self.__dict__.get("photo_url", None)

    @property
    def price(self):
        return float(self.__dict__.get("price", 0))

    @property
    def model(self):
        for attr in self.__dict__.get("attributes", []):
            if attr["type"] == "model":
                return attr["value"]
        return None
    
    @property
    def model_rarity(self):
        for attr in self.__dict__.get("attributes", []):
            if attr["type"] == "model":
                return attr["rarity_per_mille"]
        return None
    
    @property
    def symbol(self):
        for attr in self.__dict__.get("attributes", []):
            if attr["type"] == "symbol":
                return attr["value"]
        return None
    
    @property
    def symbol_rarity(self):
        for attr in self.__dict__.get("attributes", []):
            if attr["type"] == "symbol":
                return attr["rarity_per_mille"]
        return None
    
    @property
    def backdrop(self):
        for attr in self.__dict__.get("attributes", []):
            if attr["type"] == "backdrop":
                return attr["value"]
        return None
    
    @property
    def backdrop_rarity(self):
        for attr in self.__dict__.get("attributes", []):
            if attr["type"] == "backdrop":
                return attr["rarity_per_mille"]
        return None
    
    @property
    def listed_at(self):
        return self.__dict__.get("listed_at", None)

    @property
    def status(self):
        return self.__dict__.get("status", None)

    @property
    def animation_url(self):
        return self.__dict__.get("animation_url", None)

    @property
    def emoji_id(self):
        return self.__dict__.get("emoji_id", None)

    @property
    def floor_price(self):
        return float(self.__dict__.get("floor_price", 0))

    @property
    def unlocks_at(self):
        return self.__dict__.get("unlocks_at", None)

class CollectionOffer:
    def __init__(self, data: dict):
        if isinstance(data, list):
            data = data[0] if data else {}
        self.__dict__ = data
    
    def toDict(self):
        return self.__dict__
    
    @property
    def id(self):
        return self.__dict__.get("id", None)

    @property
    def collection_id(self):
        return self.__dict__.get("collection_id", None)

    @property
    def sender_id(self):
        return self.__dict__.get("sender_id", None)
    
    @property
    def amount(self):
        return float(self.__dict__.get("amount", None)) if self.__dict__.get("amount", None) else None
    
    @property
    def max_nfts(self):
        return int(self.__dict__.get("max_nfts", None)) if self.__dict__.get("max_nfts", None) else None
    
    @property
    def current_nfts(self):
        return int(self.__dict__.get("current_nfts", None)) if self.__dict__.get("current_nfts", None) else None
    
    @property
    def status(self):
        return self.__dict__.get("status", None)
    
    @property
    def created_at(self):
        return self.__dict__.get("created_at", None)
    
    @property
    def updated_at(self):
        return self.__dict__.get("updated_at", None)
    
    @property
    def expires_at(self):
        return self.__dict__.get("expires_at", None)
    
    @property
    def name(self):
        return self.__dict__.get("collection", {}).get("name", None)
    
    @property
    def short_name(self):
        return self.__dict__.get("collection", {}).get("short_name", None)
    
    @property
    def photo_url(self):
        return self.__dict__.get("collection", {}).get("photo_url", None)
    
    @property
    def floor_price(self):
        return float(self.__dict__.get("collection", {}).get("floor_price", None)) if self.__dict__.get("collection", {}).get("floor_price", None) else None

class GiftOffer:
    def __init__(self, data: dict):
        if isinstance(data, list):
            data = data[0] if data else {}
        self.__dict__ = data
    
    def toDict(self):
        return self.__dict__
    
    @property
    def id(self):
        return self.__dict__.get("id", None)

    @property
    def amount(self):
        return float(self.__dict__.get("amount", None)) if self.__dict__.get("amount", None) else None
    
    @property
    def status(self):
        return self.__dict__.get("status", None)
    
    @property
    def created_at(self):
        return self.__dict__.get("created_at", None)
    
    @property
    def updated_at(self):
        return self.__dict__.get("updated_at", None)
    
    @property
    def expires_at(self):
        return self.__dict__.get("expires_at", None)
    
    @property
    def nft(self):
        return PortalsGift(self.__dict__.get("nft", {}))
    
class Points:
    def __init__(self, data: dict):
        self.__dict__ = data

    def toDict(self):
        return self.__dict__
    
    @property
    def total_points(self):
        return int(self.__dict__.get("total_points", 0))
    
    @property
    def purchase_points(self):
        return int(self.__dict__.get("summary", {}).get("purchase_points", 0))
    
    @property
    def sell_points(self):
        return int(self.__dict__.get("summary", {}).get("sell_points", 0))
    
    @property
    def referral_points(self):
        return int(self.__dict__.get("summary", {}).get("referral_points", 0))
    
    @property
    def bonus_points(self):
        return int(self.__dict__.get("summary", {}).get("bonus_points", 0))
    
    @property
    def purchase_count(self):
        return int(self.__dict__.get("summary", {}).get("purchase_count", 0))
    
    @property
    def sell_count(self):
        return int(self.__dict__.get("summary", {}).get("sell_count", 0))
    
    @property
    def referral_count(self):
        return int(self.__dict__.get("summary", {}).get("referral_count", 0))
    
    @property
    def bonus_count(self):
        return int(self.__dict__.get("summary", {}).get("bonus_count", 0))
    
class Stats:
    def __init__(self, data: dict):
        self.__dict__ = data

    def toDict(self):
        return self.__dict__
    
    @property
    def total_bought(self):
        return int(self.__dict__.get("total_bought", 0))

    @property
    def total_sold(self):
        return int(self.__dict__.get("total_sold", 0))

    @property
    def total_volume(self):
        return float(self.__dict__.get("total_volume", 0))
    
class Balances:
    def __init__(self, data: dict):
        self.__dict__ = data

    def toDict(self):
        return self.__dict__

    @property
    def balance(self):
        return float(self.__dict__.get("balance", 0))

    @property
    def frozen_funds(self):
        return float(self.__dict__.get("frozen_funds", 0))

class DepositInfo:
    """
    Result of creating a TON deposit (POST /deposits).

    Wraps whatever the API returns and exposes the fields needed to complete
    the on-chain transfer: the destination ``address``, the ``amount`` and the
    text ``comment`` (deposit id) that must be attached to the transaction so
    Portals can credit the balance.
    """
    def __init__(self, data):
        if isinstance(data, dict):
            self.__dict__ = data
        elif isinstance(data, str):
            self.__dict__ = {"id": data}
        else:
            self.__dict__ = {}

    def toDict(self):
        return self.__dict__

    @property
    def id(self):
        return self.__dict__.get("id") or self.__dict__.get("deposit_id")

    @property
    def address(self):
        for key in ("wallet_address", "address", "deposit_address", "destination", "to"):
            value = self.__dict__.get(key)
            if value:
                return value
        return None

    @property
    def amount(self):
        value = self.__dict__.get("amount")
        return float(value) if value not in (None, "") else None

    @property
    def comment(self):
        return self.__dict__.get("comment") or self.__dict__.get("payload") or self.id

    @property
    def status(self):
        return self.__dict__.get("status")

    @property
    def sent_tx(self):
        """Details of the transaction sent by deposit()'s auto-send mode (if any)."""
        return self.__dict__.get("_sent_tx")

class DepositStatus:
    def __init__(self, data: dict):
        self.__dict__ = data if isinstance(data, dict) else {}

    def toDict(self):
        return self.__dict__

    @property
    def id(self):
        return self.__dict__.get("id") or self.__dict__.get("deposit_id")

    @property
    def status(self):
        return self.__dict__.get("status")

    @property
    def amount(self):
        value = self.__dict__.get("amount")
        return float(value) if value not in (None, "") else None

    @property
    def created_at(self):
        return self.__dict__.get("created_at")

    @property
    def updated_at(self):
        return self.__dict__.get("updated_at")

class WithdrawStatus:
    def __init__(self, data: dict):
        self.__dict__ = data if isinstance(data, dict) else {}

    def toDict(self):
        return self.__dict__

    @property
    def id(self):
        return self.__dict__.get("id") or self.__dict__.get("withdrawal_id")

    @property
    def status(self):
        return self.__dict__.get("status")

    @property
    def amount(self):
        value = self.__dict__.get("amount")
        return float(value) if value not in (None, "") else None

    @property
    def external_address(self):
        return self.__dict__.get("external_address") or self.__dict__.get("address")

    @property
    def created_at(self):
        return self.__dict__.get("created_at")

class WalletLimits:
    def __init__(self, data: dict):
        self.__dict__ = data if isinstance(data, dict) else {}

    def toDict(self):
        return self.__dict__

    def _num(self, *keys):
        for key in keys:
            value = self.__dict__.get(key)
            if value not in (None, ""):
                return float(value)
        return None

    @property
    def min_deposit(self):
        return self._num("min_deposit", "min_deposit_amount")

    @property
    def min_withdraw(self):
        return self._num("min_withdraw", "min_withdraw_amount", "min_amount")

    @property
    def max_withdraw(self):
        return self._num("max_withdraw", "max_withdraw_amount", "max_amount")

    @property
    def daily_limit(self):
        return self._num("daily_limit")

    @property
    def withdraw_fee(self):
        return self._num("withdraw_fee", "fee")

class WalletHistory:
    """A single wallet history entry (deposit / withdrawal / trade)."""
    def __init__(self, data: dict):
        self.__dict__ = data if isinstance(data, dict) else {}

    def toDict(self):
        return self.__dict__

    @property
    def id(self):
        return self.__dict__.get("id")

    @property
    def type(self):
        return self.__dict__.get("type")

    @property
    def status(self):
        return self.__dict__.get("status")

    @property
    def amount(self):
        value = self.__dict__.get("amount")
        return float(value) if value not in (None, "") else None

    @property
    def created_at(self):
        return self.__dict__.get("created_at")

class Filters:
    def __init__(self, data: dict):
        self.__dict__ = data

    def toDict(self):
        return self.__dict__

    def model(self, name: str):
        return float(self.__dict__.get("models", {}).get(cap(name), 0))

    def symbol(self, name: str):
        return float(self.__dict__.get("symbols", {}).get(cap(name), 0))
    
    def backdrop(self, name: str):
        return float(self.__dict__.get("backdrops", {}).get(cap(name), 0))

    @property
    def backdrops(self):
        return self.__dict__.get("backdrops", {})

    @property
    def models(self):
        return self.__dict__.get("models", {})

    @property
    def symbols(self):
        return self.__dict__.get("symbols", {})

class GiftsFloors:
    def __init__(self, data: dict):
        self.__dict__ = data

    def toDict(self):
        return self.__dict__

    def floor(self, giftShortName: str):
        return float(self.__dict__.get(giftShortName, 0)) if giftShortName in self.__dict__ else 0.0
    
class Collections:
    def __init__(self, collections: list):
        self._collections = collections

    def gift(self, gift_name: str):
        for c in self._collections:
            if c.get("name") == cap(gift_name):
                return CollectionItem(c)
        return None

class CollectionItem:
    def __init__(self, data: dict):
        self.__dict__ = data

    @property
    def id(self):
        return self.__dict__.get("id")

    @property
    def name(self):
        return self.__dict__.get("name")

    @property
    def short_name(self):
        return self.__dict__.get("short_name")

    @property
    def photo_url(self):
        return self.__dict__.get("photo_url")

    @property
    def day_volume(self):
        return float(self.__dict__.get("day_volume", 0))

    @property
    def volume(self):
        return float(self.__dict__.get("volume", 0))

    @property
    def floor_price(self):
        return float(self.__dict__.get("floor_price", 0))

    @property
    def supply(self):
        return int(self.__dict__.get("supply", 0))

class Activity:
    def __init__(self, data: dict):
        self.__dict__ = data

    def toDict(self):
        return self.__dict__

    @property
    def nft(self):
        return PortalsGift(self.__dict__.get("nft", {}))
    
    @property
    def offer_id(self):
        return self.__dict__.get("offer_id", None)
    
    @property
    def type(self):
        return self.__dict__.get("type", None)
    
    @property
    def amount(self):
        return float(self.__dict__.get("amount", 0))
    
    @property
    def created_at(self):
        return self.__dict__.get("created_at", None)
    
class MyActivity:
    def __init__(self, data: dict):
        self.__dict__ = data

    def toDict(self):
        return self.__dict__

    @property
    def nft(self):
        return PortalsGift(self.__dict__.get("nft", {}))
    
    @property
    def target_user_id(self):
        return self.__dict__.get("target_user_id", None)
    
    @property
    def nft_id(self):
        return self.__dict__.get("nft_id", None)
    
    @property
    def offer_id(self):
        return self.__dict__.get("offer_id", None)
    
    @property
    def type(self):
        return self.__dict__.get("type", None)
    
    @property
    def amount(self):
        return float(self.__dict__.get("amount", 0))
    
    @property
    def created_at(self):
        return self.__dict__.get("created_at", None)
    
    @property
    def referrer_revenue(self):
        return float(self.__dict__.get("referrer_revenue", 0))
    
    @property
    def collection_id(self):
        return self.__dict__.get("collection_id", None)
    
    @property
    def metadata(self):
        return self.__dict__.get("metadata", {})
    
    @property
    def offer_status(self):
        return self.__dict__.get("offer", {}).get("status", None)
    
    @property
    def offer_price(self):
        return float(self.__dict__.get("offer", {}).get("price", 0))
    
    @property
    def recipient_id(self):
        return self.__dict__.get("offer", {}).get("recipient_id", None)

class SaleResult:
    def __init__(self, data: dict):
        self.__dict__ = data

    def toDict(self):
        return self.__dict__

    @property
    def successful_nfts(self):
        return self.__dict__.get("successful_nfts", [])
    
    @property
    def failed_nfts(self):
        return self.__dict__.get("failed_nfts", [])

class GiveawayChannel:
    def __init__(self, data: dict):
        self.__dict__ = data

    def toDict(self):
        return self.__dict__
    
    @property
    def username(self):
        return self.__dict__.get("username", None)
    
    @property
    def id(self):
        return self.__dict__.get("id", None)
    
    @property
    def title(self):
        return self.__dict__.get("title", None)
    
    @property
    def is_member(self):
        return self.__dict__.get("is_member", None)

class GiveawayPrize:
    def __init__(self, data: dict):
        self.__dict__ = data

    def toDict(self):
        return self.__dict__
    
    @property
    def id(self):
        return self.__dict__.get("nft_id", None)

    @property
    def name(self):
        return self.__dict__.get("nft_name", None)

    @property
    def photo_url(self):
        return self.__dict__.get("nft_photo", None)

    @property
    def animation_url(self):
        return self.__dict__.get("nft_animation_url", None)

    @property
    def emoji_id(self):
        return self.__dict__.get("nft_emoji_id", None)

    @property
    def status(self):
        return self.__dict__.get("nft_status", None)

    @property
    def collection_id(self):
        return self.__dict__.get("nft_collection_id", None)

    @property
    def tg_id(self):
        return self.__dict__.get("nft_external_collection_number", None)

    @property
    def model(self):
        for attr in self.__dict__.get("nft_attributes", []):
            if attr.get("type", None) == "model":
                return attr.get("value", None)
            
    @property
    def model_rarity(self):
        for attr in self.__dict__.get("nft_attributes", []):
            if attr.get("type", None) == "model":
                return attr.get("rarity_per_mille", None)
            
    @property
    def symbol(self):
        for attr in self.__dict__.get("nft_attributes", []):
            if attr.get("type", None) == "symbol":
                return attr.get("value", None)
            
    @property
    def symbol_rarity(self):
        for attr in self.__dict__.get("nft_attributes", []):
            if attr.get("type", None) == "symbol":
                return attr.get("rarity_per_mille", None)
            
    @property
    def backdrop(self):
        for attr in self.__dict__.get("nft_attributes", []):
            if attr.get("type", None) == "backdrop":
                return attr.get("value", None)
            
    @property
    def backdrop_rarity(self):
        for attr in self.__dict__.get("nft_attributes", []):
            if attr.get("type", None) == "backdrop":
                return attr.get("rarity_per_mille", None)

    @property
    def floor_price(self):
        value = self.__dict__.get("nft_floor_price", 0)
        try:
            return float(value)
        except (TypeError, ValueError):
            return 0.0

    @property
    def position(self):
        return self.__dict__.get("position", None)

class Giveaway:
    def __init__(self, data: dict):
        self.__dict__ = data

    def toDict(self):
        return self.__dict__
    
    @property
    def channels(self):
        return [GiveawayChannel(channel) for channel in self.__dict__.get("channels", [])]

    @property
    def id(self):
        return self.__dict__.get("id", None)
    
    @property
    def starts_at(self):
        return self.__dict__.get("starts_at", None)
    
    @property
    def ends_at(self):
        return self.__dict__.get("ends_at", None)
    
    @property
    def status(self):
        return self.__dict__.get("status", None)
    
    @property
    def require_premium(self):
        return self.__dict__.get("require_premium", None)
    
    @property
    def require_boost(self):
        return self.__dict__.get("require_boost", None)
    
    @property
    def min_volume(self):
        return float(self.__dict__.get("min_volume", 0))
    
    @property
    def participants_count(self):
        return int(self.__dict__.get("participants_count", 0))
    
    @property
    def prizes_count(self):
        return int(self.__dict__.get("prizes_count", 0))
    
    @property
    def prizes(self):
        return [GiveawayPrize(prize) for prize in self.__dict__.get("prizes", [])]
    
    @property
    def is_participating(self):
        return self.__dict__.get("is_participating", None)
    
    @property
    def is_creator(self):
        return self.__dict__.get("is_creator", None)
    
    @property
    def created_at(self):
        return self.__dict__.get("created_at", None)

class GiveawayRequirements:
    def __init__(self, data: dict):
        self.__dict__ = data

    def toDict(self):
        return self.__dict__
    
    @property
    def can_participate(self):
        return self.__dict__.get("can_participate", None)
    
    @property
    def is_already_participating(self):
        return self.__dict__.get("is_already_participating", None)
    
    @property
    def require_premium(self):
        return self.__dict__.get("requirements", {}).get("require_premium", None)
    
    @property
    def require_boost(self):
        return self.__dict__.get("requirements", {}).get("require_boost", None)
    
    @property
    def min_volume(self):
        return float(self.__dict__.get("requirements", {}).get("min_volume", 0))
    
    @property
    def channels(self):
        return [GiveawayChannel(channel) for channel in self.__dict__.get("requirements", {}).get("channels", [])]
    
    @property
    def premium_missing(self):
        return self.__dict__.get("missing_requirements", {}).get("premium", None)
    
    @property
    def boost_missing(self):
        return self.__dict__.get("missing_requirements", {}).get("boost", None)
    
    @property
    def volume_missing(self):
        return float(self.__dict__.get("missing_requirements", {}).get("min_volume", None))
    
    @property
    def user_volume(self):
        return float(self.__dict__.get("missing_requirements", {}).get("user_volume", None))
    
    @property
    def channels_missing(self):
        return [GiveawayChannel(channel) for channel in self.__dict__.get("missing_requirements", {}).get("channels", [])]
    
    @property
    def giveaway_status(self):
        return self.__dict__.get("giveaway_status", None)
    
    @property
    def is_active(self):
        return self.__dict__.get("is_active", None)
    
    @property
    def has_ended(self):
        return self.__dict__.get("has_ended", None)
