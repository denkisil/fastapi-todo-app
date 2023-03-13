from pydantic import BaseSettings

class Settings(BaseSettings):
	MAX_FILESIZE: int = 4 * 1024 * 1024
	JWT_EXPIRES_AT: int
	SUPABASE_URL: str
	SUPABASE_KEY: str
	JWT_SECRET: str


	class Config:
		env_file = ".env"

def return_settings():
	return Settings()
