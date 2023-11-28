import json
import os
from fastapi import status,HTTPException,Depends,APIRouter,UploadFile,File
from typing import List,Optional
from .nlp_processing  import ImageTagProcessingFacade,CaptionGenerator,NERExtractor,NLTKNer
from dotenv import load_dotenv
from api import schemas
router = APIRouter(prefix='/generation',tags=['Generate'])


API_TOKEN='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'
NLP_API_URL='https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning'





@router.post("/image_tag",status_code=status.HTTP_201_CREATED,response_model=schemas.ResponseText)
async def upload(input_file:UploadFile=File(...)):
    
    # Getting input image from client side
    input_image = await input_file.read()
    
    caption_generator = CaptionGenerator(API_TOKEN,NLP_API_URL)
    nltk_ner = NLTKNer()
    ner_extractor = NERExtractor(ner_strategy=nltk_ner)
    image_tag_processor = ImageTagProcessingFacade(caption_generator=caption_generator,ner_extractor=ner_extractor)
    response = image_tag_processor.process_image_and_extract_ner(input_image=input_image)

    response =  schemas.ResponseText(data=response)

    return response

    

