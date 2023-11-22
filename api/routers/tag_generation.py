import json
import requests
from fastapi import status,HTTPException,Depends,APIRouter,UploadFile,File
from typing import List,Optional
from nlp_processing import ImageTagProcessingFacade,CaptionGenerator,NERExtractor,NLTKNer


router = APIRouter(prefix='/generation',tags=['Generate'])

@router.post("/image_tag",status_code=status.HTTP_201_CREATED)
def upload(input_file:UploadFile=File(...)):
    
    # Getting input image from client side
    input_image = input_file.read()
    
    caption_generator = CaptionGenerator()
    nltk_ner = NLTKNer()
    ner_extractor = NERExtractor(ner_strategy=nltk_ner)
    image_tag_processor = ImageTagProcessingFacade(caption_generator=caption_generator,ner_extractor=ner_extractor)
    response = image_tag_processor.process_image_and_extract_ner(input_image=input_image)
    

