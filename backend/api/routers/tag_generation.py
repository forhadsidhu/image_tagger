import json
import os
from fastapi import status,HTTPException,Depends,APIRouter,UploadFile,File
from typing import List,Optional
from .nlp_processing  import ImageTagProcessingFacade,CaptionGenerator,NERExtractor,NLTKNer
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from db_utilities.database import get_db
from db_utilities import models
from .. import oauth2
from .feature_extraction import ImageFeature



from api import schemas
router = APIRouter(prefix='/generation',tags=['Generate'])


API_TOKEN='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'
NLP_API_URL='https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning'



@router.post("/image_tag",status_code=status.HTTP_201_CREATED,response_model=schemas.tagGenerationOut)
async def upload(input_file:UploadFile=File(...),db: Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    
    # Getting input image from client side
    input_image = await input_file.read()
    
    caption_generator = CaptionGenerator(API_TOKEN,NLP_API_URL)
    nltk_ner = NLTKNer()
    image_feature_extractor = ImageFeature()
    ner_extractor = NERExtractor(ner_strategy=nltk_ner)
    image_tag_processor = ImageTagProcessingFacade(caption_generator=caption_generator,ner_extractor=ner_extractor)
    
    # Getting image tag using hugging face models.
    response = image_tag_processor.process_image_and_extract_ner(input_image=input_image)
    
    # Getting image feature vector which will be stored in db for finding similarity.
    serialized_feature_str = image_feature_extractor.get_image_features(image=input_image)
 
    # Save the image tag and corresponding feature into the database
    image_response = models.ImageResponse(
        image_path = '1',
        image_tags = str(response),
        features = serialized_feature_str
    )

    db.add(image_response)
    db.commit()
    db.refresh(image_response)

    api_response = schemas.tagGenerationOut(
        image_path='1',
        image_tags=str(response)
    )
    return api_response

    

