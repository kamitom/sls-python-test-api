import requests
import json


def reqFunc(event, context):
    # r = requests.get("https://ycombinator.com/news")
    r = requests.get("https://postman-echo.com/get?foo1=bar1&foo2=bar2")
    return {"Content": (r.text)}
