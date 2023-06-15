from fastapi import APIRouter
from services import image as image_service
from models.image import Image

router = APIRouter()

@router.post("/")
async def create_image(image: Image):
    return await image_service.create_image(image)

@router.get("/")
async def get_image():
    return await image_service.read_images()

@router.put("/")
async def update_image(image: Image):
    return await image_service.update_image(image)
