from fastapi import FastAPI
import instaloader
app =FastAPI()

@app.get('/')
async def root():
   
    return {
        "followers":9
    }