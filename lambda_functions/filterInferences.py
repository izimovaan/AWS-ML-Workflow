import json

THRESHOLD = 0.93

def lambda_handler(event, context):
    if 'Payload' in event:
        data = event['Payload']
    else:
        data = event

    # The event passed from Step Functions is a Python dictionary.
    inferences = data['inferences']

    # Check if any value in our inferences are above THRESHOLD
    meets_threshold = max(inferences) > THRESHOLD

    # If the threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        return data
    else:
        error_message = {
            "errorType": "THRESHOLD_CONFIDENCE_NOT_MET",
            "errorMessage": f"Confidence score of {max(inferences)} is below the threshold of {THRESHOLD}."
        }
        raise Exception(json.dumps(error_message))