import requests

url = requests.get("https://isro.vercel.app/api/spacecrafts")
response = url.json()
print(response)