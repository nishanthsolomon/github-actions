import hmac
import uvicorn
import json
import os

from pyngrok import ngrok
from fastapi import FastAPI, Request

app = FastAPI()
KEY = os.environ.get('GITHUB_SECRET')


@app.post("/payload")
async def github_callback(request: Request):
    signature = request.headers.get(
        'X-Hub-Signature-256')

    payload_body = await request.body()

    if verify_signature(payload_body, signature):
        print(json.loads(payload_body))


def verify_signature(payload_body, signature):
    signature = signature.replace('sha256=', '')

    input_hmac = hmac.new(
        key=KEY.encode(),
        msg=payload_body,
        digestmod="sha256"
    )

    return hmac.compare_digest(
        input_hmac.hexdigest(),
        signature
    )


if __name__ == '__main__':
    public_url = ngrok.connect(8000).public_url
    print(public_url)
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
