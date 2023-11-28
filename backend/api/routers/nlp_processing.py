

import requests
from dotenv import load_dotenv
import os
dotenv_path = '.env'
from typing import List,AnyStr
from io import BytesIO
import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk.data import find
from abc import ABC,abstractmethod
from nltk import download as nltk_download

try:
    find('tokenizers/punkt')
except LookupError:
    nltk_download('punkt')

try:
    find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk_download('averaged_perceptron_tagger')




Image = BytesIO

class ImageTagProcessingFacade:

    """Facade patttern for processing the input image 
    First extract tag then processed this using NLP.
    """

    def __init__(self,caption_generator:'CaptionGenerator',ner_extractor:'NERExtractor') -> None:
        self.caption_generator = caption_generator
        self.ner_extractor = ner_extractor

    # Interface for processing the input image using api and NLP
    def process_image_and_extract_ner(self,input_image:Image)->List[str]:
        response_caption = self.caption_generator.generate_caption(input_image)
        response_ner = self.ner_extractor.extract_ner(response_caption)
        return response_ner


class CaptionGenerator:
    """Image caption generation class based on API.
    """
    def __init__(self,api_token,api_url) -> None:
        self.API_TOKEN = api_token
        self.API_URL = api_url

    # Function for generating image caption based on pretrained NLP api.
    def generate_caption(self,input_image:Image)->str:
        headers = {"Authorization": f"Bearer {self.API_TOKEN}"}
        api_response = requests.post(self.API_URL, headers=headers, data=input_image)
        response = api_response.json()
        image_caption = response[0]['generated_text']
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
    



    