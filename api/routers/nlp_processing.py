import requests
API_URL =""
API_TOKEN = ""
headers = {"Authorization":f"Bearer {API_TOKEN}"}






def get_image_tag(payload):
    '''Function for processing input image and get particular tag for the input image
    '''
    response = requests.post(API_URL,headers=headers,json=payload)
    return response.json()