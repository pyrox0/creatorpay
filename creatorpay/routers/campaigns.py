from fastapi import APIRouter, HTTPException
from ..models.campaigns import Campaign, Tier
from decimal import Decimal

TEST_TIERS = [
    Tier(id=0, price=Decimal(0.5), title="Tier 1"),
    Tier(id=1, price=Decimal(1.0), title="Tier 1"),
    Tier(id=2, price=Decimal(5.0), title="Tier 1"),
]

TEST_TIER_IDS = [0, 1, 2]

TEST_CAMPAIGN_1 = Campaign(id=1, creator_id=0, tiers=TEST_TIER_IDS)
TEST_CAMPAIGN_2 = Campaign(id=2, creator_id=1, tiers=TEST_TIER_IDS)

TEST_CAMPAIGNS = [TEST_CAMPAIGN_1, TEST_CAMPAIGN_2]

router = APIRouter(
    prefix="/campaigns",
    tags=["campaigns"],
)


@router.get(
    "/{campaign_id}", summary="Get all information about the requested campaign."
)
async def get_campaign(campaign_id: int) -> Campaign:
    camp = [c for c in TEST_CAMPAIGNS if c.id == campaign_id][0]
    if not camp:
        raise HTTPException(status_code=404, detail="Campaign does not exist")
    return camp


@router.get("/{campaign_id}/tiers", summary="Get all tiers from the provided campaign.")
async def get_campaign_tiers(campaign_id: int) -> list[Tier]:
    camp = [c for c in TEST_CAMPAIGNS if c.id == campaign_id][0]
    if not camp:
        raise HTTPException(status_code=404, detail="Campaign does not exist")
    return [t for t in TEST_TIERS if t.id in camp.tiers]
