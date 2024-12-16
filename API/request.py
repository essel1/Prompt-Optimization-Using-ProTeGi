import requests

url = "http://127.0.0.1:8000/optimize-prompt/"

params = {
    "prompts": ["Optimize this prompt", "Write a creative story"]
}

response = requests.post(url, params=params)
print(response.json())