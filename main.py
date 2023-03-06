import uvicorn 

if __name__ == '__main__':
	uvicorn.run('src.app:app', reload=True)