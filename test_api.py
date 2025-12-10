import requests

# URL of your local API
url = "http://127.0.0.1:5000/sentiment"

# Text you want to analyze
data = {"text": "I love this product!"}

# Send POST request
response = requests.post(url, json=data)

# Print the response from the API
print(response.json())

