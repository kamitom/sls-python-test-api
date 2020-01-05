import json
from faker import Faker


def hellofunc(event, context):

    # fakeTest = Faker("zh_TW")
    fakeTest = Faker(['it_IT', 'en_US', 'ja_JP', 'zh_TW'])

    # japanDramaRoleName = "生田斗真"
    japanDramaRoleName = fakeTest.name()

    body = {
        "message": "hi, " + japanDramaRoleName,
        # "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
