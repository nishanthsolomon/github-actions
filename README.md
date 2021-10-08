# GitHub Webhook

## Starting the server

1. Install required packages in requirements.txt
2. export the github secret

        export GITHUB_SECRET=<githubSecret>

3. Start the server

        python server.py

4. Copy the public url.

## Configure the GitHub webhook

https://docs.github.com/en/developers/webhooks-and-events/webhooks

1. Open GitHub repository settings.
2. Click on Webhooks -> Add Webhook.
3. Set the Payload URL = \<public url> + /payload

    eg. http://2ef7-2601-140-8a80-a010-5b7a-82e7-226d-85d.ngrok.io/payload

4. Set the Secret same as \<githubSecret>
5. Configure Which events would you like to trigger this webhook?
