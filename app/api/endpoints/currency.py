from fastapi import APIRouter

from schemas.currency import Currency


router = APIRouter()


@router.get("currency/list/")
async def list_currencies() -> list[Currency]:
    currencies = []
    
    return currencies
