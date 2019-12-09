import requests

def reqFunc(event, context):
  r = requests.get("https://ycombinator.com/news")
  return {"Content": r.text}
    