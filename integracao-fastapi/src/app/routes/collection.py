from fastapi import APIRouter
from services import collection as collection_service
from models.collection import Collection

router = APIRouter()

@router.post("/")
async def create_collection(collection: Collection):
    return await collection_service.create_collection(collection)

@router.get("/")
async def read_collections():
    return await collection_service.read_collections()


