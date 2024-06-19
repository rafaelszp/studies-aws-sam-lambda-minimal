import json
import boto3
import json
import os

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    
    if os.environ.get("AWS_SAM_LOCAL"):
        LAMBDA_CLIENT = boto3.client('lambda',endpoint_url='http://172.17.0.1:3001')
    else:
        LAMBDA_CLIENT = boto3.client('lambda')

    encoded_payload = json.dumps({'first_name': 'rafael'}).encode('utf-8')

    invoke_resp = LAMBDA_CLIENT.invoke(
        FunctionName='ChildFnFunction',
        InvocationType='RequestResponse',
        Payload=encoded_payload
    )

    status_code = invoke_resp['StatusCode']
    if status_code != 200:
        raise RuntimeError('Call target lambda function failed =[')
    
    results = {}
    if invoke_resp['Payload']:
        payload = invoke_resp['Payload']
        results = json.loads(payload.read())
    print('--------------------------------------------------------------------------------')
    print('Results from child function: ')
    print(results)
    print('--------------------------------------------------------------------------------')

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "childResponse": results
        }),
    }
