# Blockchain Presence Independent Study
This repository is part of the independent study with Blockchain Presence at the University of Zurich.

In order to run the application, please clone this repository locally on your machine and upload the entire content in your Google Drive account in the root folder (under My Drive).

Then, navigate to car-damage-project\car-damage-detection-notebooks and run the demo.ipynb in Google Colab.

The application is built with FastAPI and a uvicorn server will be running on your localhost. Since the Google Colab's notebook IP cannot be accessed directly, ngrok is used to create a public URL for the server via a tunnel. In order to navigate to the app, use the public URL that was exposed with ngrok.
