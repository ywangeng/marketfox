from fastapi import APIRouter

router = APIRouter()


@router.get("")
def ok():
    return {"service": "MarketFox API", "status": "ok"}
