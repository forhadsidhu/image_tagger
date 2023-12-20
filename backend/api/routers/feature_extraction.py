import torch
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
import io
import json

class ImageFeature():
    """ Class for getting image features using pretrained model(ResNet).
    """

    def __init__(self) -> None:
        self.model = models.resnet18(pretrained=True)
        
    
    # Extract features using some pretrained model.
    def get_image_features(self,image:bytes)->str:
        # convert binary data to PIL Image
        img = Image.open(io.BytesIO(image)).convert('RGB')

        # Define preprocessing transformations
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485,0.456,0.406],std = [0.229,0.224,0.225]),
            ])
        
        # Preprocess the input image.
        img = preprocess(img)
        # Load the model here.
        model = self.model
        
        # Remove the las layer of the model
        model = torch.nn.Sequential( *list(model.children())[:-1])
        # Going in the evaluation mode of the model
        model.eval()
        
        # Make pause other stuff.
        with torch.no_grad():
            features = model(img)
        
        # Converting to 1 dimensional feature vector.
        feature_vector = features.squeeze().numpy()
        
        # Convert the feature vector to list
        feature_list = feature_vector.tolist()

        # Serialize the feature vector for storing.
        serialized_feature = json.dumps(feature_list)
        
        return serialized_feature
      
       



