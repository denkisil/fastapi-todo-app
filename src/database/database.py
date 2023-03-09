from src.config.config import return_settings

from supabase import Client, create_client


env = return_settings()
	

class Base:
	def __init__(self):
		self.db: Client = create_client(env.SUPABASE_URL, env.SUPABASE_KEY)