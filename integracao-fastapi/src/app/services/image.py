from models import image as image_model
from supabase import create_client
from prettyconf import config

# Initialize the Supabase client
supabase_url = "https://mbivubybidjkektfefjh.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1iaXZ1YnliaWRqa2VrdGZlZmpoIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NTcyOTYwMiwiZXhwIjoyMDAxMzA1NjAyfQ.yiPBjxnpvURnzywWaxgNJM9y3jHk79jKiim3i0vFcVo"
supabase = create_client(supabase_url, supabase_key)

async def create_image(image: image_model):
    print("EXECUTANDO: create_image")
    return None

async def read_images():
    print("EXECUTANDO: read_images")
    return None

async def update_image(image):
    print("EXECUTANDO: update_image")
    return None

