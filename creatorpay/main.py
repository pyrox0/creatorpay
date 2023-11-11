from fastapi import FastAPI

from .routers import auth_router, users_router, account_router, payments_router, campaigns_router

app = FastAPI(
    title="CreatorPay API",
    summary="An API for creators, coders, and all to fund themselves.",
    terms_of_service="https://creatorpay.app/api-terms",
    contact={
        "name": "CreatorPay Support",
        "url": "https://creatorpay.app/support/",
        "email": "support@creatorpay.app",
    },
    license_info={
        "name": "Creative Commons Attribution No Derivatives 4.0 International",
        "identifier": "CC-BY-ND-4.0",
    },
)

app.include_router(auth_router)
app.include_router(account_router)
app.include_router(campaigns_router)
app.include_router(payments_router)
app.include_router(users_router)
