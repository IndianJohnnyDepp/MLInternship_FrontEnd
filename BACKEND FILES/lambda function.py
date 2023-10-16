import json
import boto3
import base64

endpoint_name = 'MLInternship-PneumoniaDetection'

sagemaker_runtime_client = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print(event)
    image = base64.b64decode(event["image"])
    print(image)
    return _predictPneumonia(image)
  
def _predictPneumonia(image):
    response = sagemaker_runtime_client.invoke_endpoint(EndpointName = endpoint_name,
                                                        ContentType = "application/x-image",
                                                        Body = image)
    result = response['Body'].read()
    
    #Deserialize the byte array
    result = json.loads(result)
    print("Result:",result)
    
    #Identifying whether the x-ray has pneumonia infection or not
    predicted_class = 0 if result[0]>result[1] else 1
    toSend = result[0] if result[0]>result[1] else result[1]
    
    toSend = round(toSend,2)*100
    
    if predicted_class == 0:
        return f"No pneumonia infection detected in the uploaded image. I am predicting this with {toSend} % probability"
    else:
        return f"PNEUMONIA DETECTED in the uploaded image. I am predicting this with {toSend} % probability"