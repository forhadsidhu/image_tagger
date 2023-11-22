from fastapi  import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware






app = FastAPI(title='Image-Tagger-API',
              description="This is image tagger generation api for dam application'",
              version="0.0.1")


origin  = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origin,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


@app.get("/")
async def root():
    return{
        "message":"AI enabled Image tagger Genderations!"
    }