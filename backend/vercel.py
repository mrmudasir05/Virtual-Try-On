from fastapi import FastAPI
from main import app as main_app

app = FastAPI()
app.mount("/api", main_app)

# Export for Vercel serverless deployment
handler = app
