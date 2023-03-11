from pydantic import BaseSettings

class Settings(BaseSettings):
	JWT_EXPIRES_AT: int
	JWT_ALGORITHM: str
	SUPABASE_URL: str
	SUPABASE_KEY: str
	JWT_SECRET: str

	class Config:
		env_file = ".env"

def return_settings():
	return Settings()