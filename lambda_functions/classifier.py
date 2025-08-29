import json
import sagemaker
import base64
from sagemaker.predictor import Predictor
from sagemaker.serializers import IdentitySerializer

ENDPOINT = "image-classification-2025-08-28-10-49-35-302"


def lambda_handler(event, context):

    if 'Payload' in event:
        data = event['Payload']
    else:
        data = event
    # Decode the image data from the previous function's output
    image = base64.b64decode(data['image_data'])

    # Instantiate a Predictor
    predictor = Predictor(ENDPOINT)

    # For this model the IdentitySerializer needs to be "image/png"
    predictor.serializer = IdentitySerializer("image/png")

    # Make a prediction:
    inferences = predictor.predict(image)

    # Decode the inferences from bytes to a Python list
    inferences_list = json.loads(inferences.decode('utf-8'))

    # Add the inferences to the event object
    data["inferences"] = inferences_list

    # Return the updated event object.
    return data
