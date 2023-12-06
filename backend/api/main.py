from fastapi  import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import tag_generation,auth,user





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

app.include_router(tag_generation.router, prefix="/api/v1")
app.include_router(auth.router,prefix="/api/v1")
app.include_router(user.router,prefix='/api/v1')

@app.get("/")
async def root():
    return{
        "message":"AI enabled Image tagger Genderations!"
    }