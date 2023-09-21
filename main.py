from fastapi import FastAPI
import instaloader
app =FastAPI()

@app.get('/')
async def root():
    L = instaloader.Instaloader()
    #L.login("hlopy38", "hlo@hlo20")
    #L.load_session_from_file() 
    profile = instaloader.Profile.from_username(L.context, "ravitechseries")
    followeers = profile.followers
    return {
        "followers":followeers
    }