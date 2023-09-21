from fastapi import FastAPI
import instaloader
app =FastAPI()

@app.get('/')
async def root():
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, "ravitechseries")
    followeers = profile.followers
    return {
        "followers":followeers
    }