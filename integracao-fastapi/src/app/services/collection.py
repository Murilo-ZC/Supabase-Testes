from models import collection as collection_model
from supabase import create_client
from prettyconf import config

# Initialize the Supabase client
supabase_url = "https://mbivubybidjkektfefjh.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1iaXZ1YnliaWRqa2VrdGZlZmpoIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NTcyOTYwMiwiZXhwIjoyMDAxMzA1NjAyfQ.yiPBjxnpvURnzywWaxgNJM9y3jHk79jKiim3i0vFcVo"
supabase = create_client(supabase_url, supabase_key)

async def create_collection(collection):
    print("EXECUTANDO: create_collection")
    return None

async def read_collections():
    print("EXECUTANDO: read_collections")
    return None