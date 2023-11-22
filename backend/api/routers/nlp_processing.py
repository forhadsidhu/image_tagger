

import requests
from dotenv import load_dotenv
import os
dotenv_path = '../.env'
from typing import List,AnyStr
from io import BytesIO
import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk.data import find
from abc import ABC,abstractmethod

# nltk dataset download
try:
    find('tokenize/punkt')
except LookupError:
    nltk.download('punkt')



Image = BytesIO
load_dotenv(dotenv_path)
API_URL = os.getenv('NLP_API_URL')
API_TOKEN = os.getenv('API_TOKEN')



class ImageTagProcessingFacade:

    """Facade patttern for processing the input image 
    First extract tag then processed this using NLP.
    """

    def __init__(self,caption_generator:'CaptionGenerator',ner_extractor:'NERExtractor') -> None:
        self.caption_generator = caption_generator
        self.ner_extractor = ner_extractor

    # Interface for processing the input image using api and NLP
    def process_image_and_extract_ner(self,input_image:Image)->List[str]:
        response_caption = self.caption_generator(input_image)
        response_ner = self.ner_extractor(response_caption)
        return response_ner


class CaptionGenerator:
    """Image caption generation class based on API.
    """

    # Function for generating image caption based on pretrained NLP api.
    def generate_caption(self,input_image:Image)->str:
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        api_response = requests.post(API_URL, headers=headers, data=input_image)
        image_caption = api_response[0]['generated_text']
        return image_caption

class NERStrategy():
    @abstractmethod
    def extract_ner(self,input_text:str)->str:
        pass


class NLTKNer(NERStrategy):
    """Strategy class for NLTK NER Processing"""

    def extract_ner(self, input_text: str) -> str:
        tokens = word_tokenize(input_text)
        tagged_tokens = pos_tag(tokens=tokens)
        #List comprehension for getting the entity in list of string.
        keywords = [word for word,pos in tagged_tokens if pos in ['NN','NNS','JJ']]
        keyword_sting = ','.join(keywords)
        return keyword_sting

        
class NERExtractor:
    """NER extraction class for extracting entity names using Factory Strategy pattern.
    """

    def __init__(self,ner_strategy:NERStrategy) -> None:
        self.ner_strategy = ner_strategy
    
    # Function for return ner based on strategy
    def extract_ner(self,input_text:str)->str:
        response = self.ner_strategy.extract_ner(input_text=input_text)
        return response
    



    