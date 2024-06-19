# sam-app

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- hello_world - Code for the application's Lambda function.
- events - Invocation events that you can use to invoke the function.
- tests - Unit tests for the application code. 
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.


## Setup python
```
mkdir ~/dev/python/envs -p
python -m venv ~/dev/python/envs/aws
source ~/dev/python/envs/aws/bin/activate.fish
pip install --upgrade pip
pip install -r hello_world/requirements.txt
```

## Testing locally

1. local start

```shell
#start lambda
sam local start-lambda --host 0.0.0.0 --log-file /dev/stdout

#Running Hello World
aws lambda invoke --function-name "HelloWorldFunction" --endpoint-url "http://127.0.0.1:3001"
 --no-verify-ssl /dev/stdout

#Running ChildFnFunction
aws lambda invoke --function-name "ChildFnFunction" --endpoint-url "http://127.0.0.1:3001"
 --no-verify-ssl /dev/stdout
```


## sam init params

```shell
sam init
...
Which template source would you like to use?
    1 - AWS Quick Start Templates
    2 - Custom Template Location
Choice: 1

Choose an AWS Quick Start application template
    1 - Hello World Example
    2 - Multi-step workflow
    3 - Serverless API
    4 - Scheduled task
    5 - Standalone function
    6 - Data processing
    7 - Hello World Example With Powertools
    8 - Infrastructure event management
    9 - Serverless Connector Hello World Example
    10 - Multi-step workflow with Connectors
    11 - Lambda EFS example
    12 - DynamoDB Example
    13 - Machine Learning
Template: 1

Use the most popular runtime and package type? (Python and zip) [y/N]: y

Would you like to enable X-Ray tracing on the function(s) in your application?  [y/N]: ENTER

Would you like to enable monitoring using CloudWatch Application Insights?
For more info, please view https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html [y/N]: ENTER
					
Would you like to set Structured Logging in JSON format on your Lambda functions?  [y/N]: ENTER

Project name [sam-app]: ENTER
```