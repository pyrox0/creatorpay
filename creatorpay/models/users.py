from pydantic import BaseModel, HttpUrl, conlist, constr
from ulid import ULID
from enum import StrEnum


class SocialServices(StrEnum):
    custom = "Custom"
    bluesky = "Bluesky"
    discord = "Discord"
    etsy = "Etsy"
    facebook = "Facebook"
    instagram = "Instagram"
    kofi = "Ko-fi"
    paypal = "Paypal"
    telegram = "Telegram"
    tiktok = "TikTok"
    twitch = "Twitch"
    twitter = "X"
    youtube = "YouTube"


class ProfileLink(BaseModel):
    """Represents a single link in a user's bio.


    Attributes
    ----------
    service : SocialServices
        The service that this links to, set to custom if not in the list of services
    link : pydantic.HttpUrl
        A link to the service, can be set to whatever the User likes.
    """

    service: SocialServices = SocialServices.custom
    link: HttpUrl


class Profile(BaseModel):
    """Represents the profile of a specific User.

    Attributes
    ----------
    id : ULID
        The ID of this profile.
    user_id : ULID
        The id of the User whose profile this is
    accent_color : str | None
        The hex color to use for the User's profile accent color.
    display_name : constr(max_length=32) | None
        The User's display name.
    profile_picture : HttpUrl | None
        Link to the User's profile picture.
    header_picture : HttpUrl | None
        Link to the User's header image.
    pronouns : constr(max_length=20) | None
        The User's pronouns. Limited to 20 characters in length.
    bio : constr(max_length=50) | None
        The User's bio, limited to 250 characters.
    links : conlist(item_type=ProfileLink, unique_items=True, max_items=10) | None
        The User's links for their bio. Up to 10 links are supported.

    """

    id: ULID
    user_id: ULID
    accent_color: str | None = None
    display_name: constr(max_length=32) | None = None  # type:ignore
    profile_picture: HttpUrl | None = None
    header_picture: HttpUrl | None = None
    pronouns: constr(max_length=20) | None = None  # type:ignore
    bio: constr(max_length=250) | None = None  # type:ignore
    links: conlist(
        item_type=ProfileLink, unique_items=True, max_items=10
    ) | None = None  # type:ignore

    class Config:
        arbitrary_types_allowed = True


class User(BaseModel):
    """A unique user. Represents public information, provides the associated Account ID to get private information.

    Attributes
    ----------
    id : ULID
        The ID of the user, used for all API calls.
    account_id : ULID
        The associated Account of this user, used to get private information for the account.
    username : constr(max_length=32)
        The user's username, used for logins. Has to be valid ASCII and 32 chars max.
    country : constr(max_length=3)
        The 3-letter country code of the user's country.
    profile_id : ULID
        The User's profile.
    """

    id: ULID
    username: constr(max_length=32)  # type: ignore
    country: constr(max_length=3)  # type: ignore
    account_id: ULID
    profile: Profile

    class Config:
        arbitrary_types_allowed = True
