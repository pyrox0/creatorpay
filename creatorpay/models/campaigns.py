from decimal import Decimal
from pydantic import BaseModel, constr, HttpUrl
from enum import IntEnum
from ulid import ULID


class PaymentTypes(IntEnum):
    """The different payment models that a campaign can have."""

    Monthly = 1
    PerWork = 2


class Tier(BaseModel):
    """A single campaign tier.

    Attributes
    ----------
    id : ULID
        The ID of the tier, used to index it.
    price : Decimal
        The price of this Tier, in the currency of the Campaign.
    supporter_limit : int | None
         The max number of people that can subscribe to this Tier. Defaults to unlimited.
    title: constr(max_length=20)
        The title of this Tier to display in the UI. Defaults to "Tier <Tier Number>"
    tier_picture: HttpUrl | None
        Link to the image used for the Tier's header. Defaults to None.

    """

    id: int | ULID
    price: Decimal
    supporter_limit: int | None = None
    title: constr(max_length=20) = "Tier Title"  # type:ignore
    tier_picture: HttpUrl | None = None

    class Config:
        arbitrary_types_allowed = True


class Campaign(BaseModel):
    """Represents a campaign, i.e. what a creator is raising money to do or create.

    Attributes
    ----------
    id : ULID
        The ID of the campaign
    creator_id : ULID
        The ID of the User who created the Campaign.
    tiers : list[ULID]
        The list of Tier ULIDs associated with the Campaign.
        Defaults to an empty list.
    nsfw : bool
        Whether a campaign is NSFW. Requires a User to be over 18 in order to view/subscribe to the Campaign.
        Defaults to False.
    payment_type : PaymentTypes
        The payment model that the Campaign accepts, defaults to Monthly.
    currency : constr(min_length=3, max_length=3)
        The currency that a Campaign will use as its primary currency, defaults to USD.
    """

    id: int
    creator_id: int
    tiers: list[int | ULID] = []
    nsfw: bool = False
    payment_type: PaymentTypes = PaymentTypes.Monthly
    currency: constr(min_length=3, max_length=3) = "USD"  # type:ignore

    class Config:
        arbitrary_types_allowed = True
