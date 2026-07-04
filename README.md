# faportalsmp

**Asynchronous Python library for the [Portals](https://portals.tg) Gift Marketplace API.**

A maintained fork of `aportalsmp` — trade Telegram gifts (NFTs), place and manage
offers, run giveaways, read your account, and **deposit & withdraw GRAM**.

```bash
pip install faportalsmp
```

> Imported as **`aportalsmp`**:
> ```python
> import aportalsmp as portals
> ```

---

## Quick start

```python
import asyncio
import aportalsmp as portals

AUTH = "tma query_id=...&user=...&auth_date=...&hash=..."  # see Authentication

async def main():
    floors = await portals.giftsFloors(authData=AUTH)
    print("Plush Pepe floor:", floors.floor("plushpepe"))

    listings = await portals.search(gift_name="Plush Pepe", sort="price_asc", limit=5, authData=AUTH)
    for gift in listings:
        print(gift.name, gift.model, gift.price)

    balances = await portals.myBalances(authData=AUTH)
    print("Balance:", balances.balance, "GRAM")

asyncio.run(main())
```

---

## Authentication

Every request needs `authData` — a Telegram Mini App `initData` string prefixed
with `tma `. Generate it from a Telegram user session with `update_auth()`:

```python
from aportalsmp import update_auth

# with api_id / api_hash (creates a .session file)
authData = await update_auth(api_id=12345, api_hash="abc...", session_name="account")

# or from an existing Pyrogram/Kurigram session string
authData = await update_auth(session_string="BQ...")
```

---

## Wallet — GRAM deposits & withdrawals

> GRAM is the native coin (moved on the TON network). Amounts and balances are in
> **GRAM**; addresses and the on-chain transfer use the **TON** network.

### Balance, limits & history

```python
bal    = await portals.myBalances(authData=AUTH)     # .balance, .frozen_funds
limits = await portals.walletLimits(authData=AUTH)   # .min_deposit, .min_withdraw, .max_withdraw, .daily_limit
hist   = await portals.walletHistory(offset=0, limit=20, authData=AUTH)
```

### Deposit GRAM

A deposit is a native GRAM transfer to the Portals deposit wallet carrying a text
comment equal to the **deposit id** — that's how the marketplace credits your
balance.

**Intent — send it yourself (from any wallet/bot):**

```python
info = await portals.deposit(authData=AUTH)
print(info.address)   # where to send GRAM
print(info.comment)   # text comment to attach (the deposit id)
print(info.amount)    # expected amount, if provided
```

**Auto-send — the library signs & broadcasts for you** (needs a wallet mnemonic):

```python
info = await portals.deposit(
    amount=0.5,
    mnemonic="word1 word2 ... word24",   # used only to sign, never transmitted
    wallet_version="v4r2",                # v4r2 (default), v3r2, v3r1, v5r1
    authData=AUTH,
)
print(info.sent_tx)   # {'status': 'sent', 'amount': 0.5, 'to': ..., 'comment': ...}

statuses = await portals.depositStatus(ids=info.id, authData=AUTH)
```

### Withdraw GRAM

```python
withdrawal_id = await portals.withdrawGram(amount=1.0, wallet="UQ...external_address", authData=AUTH)
statuses = await portals.withdrawStatus(ids=withdrawal_id, authData=AUTH)
```

> `withdrawPortals` and `withdrawTon` are kept as aliases of `withdrawGram`.

---

## Gifts

| Function | Purpose |
| --- | --- |
| `giftsFloors(authData)` | Floor prices for every collection (by short name) |
| `filterFloors(gift_name, authData)` | Model / backdrop / symbol floors for a collection |
| `collections(limit, authData)` | Collections with floor, supply, volume |
| `search(...)` | Search listings with filters & sorting |
| `marketActivity(...)` | Recent buys / listings / offers / price updates |
| `myPortalsGifts(offset, limit, listed, authData)` | Your owned gifts |
| `myActivity(offset, limit, authData)` | Your activity |
| `buy(nft_id, price, authData)` | Buy a listing |
| `sale(nft_id, price, authData)` / `bulkList(nfts, authData)` | List gift(s) for sale |
| `changePrice(nft_id, price, authData)` | Re-price a listing |
| `transferGifts(nft_ids, username, anonymous, authData)` | Transfer gifts to a user |
| `withdrawGifts(nft_ids, authData)` | Withdraw gifts out of the marketplace |
| `getGiveaways / giveawayInfo / joinGiveaway` | Giveaways |

```python
gifts = await portals.search(
    gift_name="Plush Pepe",
    model="Sad Cat",
    backdrop=["Onyx Black", "Midnight Blue"],
    sort="price_asc", min_price=0, max_price=5000, limit=20,
    authData=AUTH,
)
if gifts:
    result = await portals.buy(nft_id=gifts[0].id, price=gifts[0].price, authData=AUTH)
```

Gift names resolve leniently — `"plush pepe"`, `"Durov's Cap"` and `"Durov’s Cap"` all work.

---

## Your gifts & inventory

See everything you own, then unlist, quick-sell, transfer or withdraw it.

```python
# full inventory — everything you own (listed or not)
mine = await portals.inventory(offset=0, limit=50, authData=AUTH)
for g in mine:
    print(g.name, g.model, g.status)

groups = await portals.inventoryCollections(authData=AUTH)   # grouped by collection, with counts
value  = await portals.inventoryValue(authData=AUTH)          # estimated inventory value (GRAM)

# only your marketplace listings
listed = await portals.myPortalsGifts(listed=True, authData=AUTH)

# take a gift off sale
await portals.unlist(nft_id=mine[0].id, authData=AUTH)              # or bulkUnlist(nft_ids=[...])

# instant-sell into the best collection offer
await portals.quickSalePreview(nft_ids=[mine[0].id], authData=AUTH)  # preview payout
await portals.quickSale(nft_ids=[mine[0].id], authData=AUTH)

# withdraw the gift out of Portals (to your Telegram account)
await portals.withdrawGifts(nft_ids=[mine[0].id], authData=AUTH)

# or transfer it to another Portals user
await portals.transferGifts(nft_ids=[mine[0].id], username="someone", authData=AUTH)

# check gifts are still available before buying
await portals.checkAvailability(nft_ids=[some_id], authData=AUTH)
```

| Function | Purpose |
| --- | --- |
| `inventory(offset, limit, authData)` | Every gift you own (listed or not) |
| `inventoryCollections(authData)` | Inventory grouped by collection, with counts |
| `inventoryValue(authData)` | Estimated total inventory value (GRAM) |
| `myPortalsGifts(offset, limit, listed, authData)` | Your gifts by marketplace listing status |
| `unlist(nft_id, authData)` / `bulkUnlist(nft_ids, authData)` | Remove gift(s) from sale |
| `quickSalePreview / quickSale(nft_ids, authData)` | Preview & instant-sell into the top offer |
| `checkAvailability(nft_ids, authData)` | Check gifts are still available |
| `withdrawGifts(nft_ids, authData)` | Withdraw gifts out of Portals (to Telegram) |
| `transferGifts(nft_ids, username, anonymous, authData)` | Transfer gifts to another user |

---

## Offers

```python
await portals.makeOffer(nft_id="...", offer_price=10, expiration_days=7, authData=AUTH)
await portals.editOffer(offer_id="...", new_price=12, authData=AUTH)
await portals.cancelOffer(offer_id="...", authData=AUTH)

await portals.collectionOffer(gift_name="Plush Pepe", amount=100, max_nfts=3, authData=AUTH)
top = await portals.topOffer(gift_name="Plush Pepe", authData=AUTH)

received = await portals.myReceivedOffers(authData=AUTH)
placed   = await portals.myPlacedOffers(authData=AUTH)
```

---

## Keeping the gift list fresh

Collection IDs live in `aportalsmp/utils/collections_ids.py` and are generated
from the public `/collections` endpoint. When new gifts drop, regenerate them:

```bash
python scripts/update_collections.py
```

---

## Data objects

Every response is wrapped in a lightweight object with typed properties and a
`.toDict()` escape hatch:

`PortalsGift`, `CollectionOffer`, `GiftOffer`, `Points`, `Stats`, `Balances`,
`DepositInfo`, `DepositStatus`, `WithdrawStatus`, `WalletLimits`,
`WalletHistory`, `Filters`, `GiftsFloors`, `Collections`, `Activity`,
`MyActivity`, `SaleResult`, `Giveaway`, `GiveawayRequirements`, …

---

## Errors

All errors subclass `Exception` and live in `aportalsmp`:

`authDataError`, `offerError`, `accountError`, `requestError`,
`connectionError`, `floorsError`, `giftsError`, `tradingError`.

```python
from aportalsmp import requestError

try:
    await portals.buy(nft_id="...", price=1.0, authData=AUTH)
except requestError as e:
    print("API error:", e)
```

---

## Disclaimer

Unofficial library — not affiliated with Portals. Trading and GRAM transfers move
real assets; test with small amounts first and keep your mnemonics safe. Use at
your own risk.
