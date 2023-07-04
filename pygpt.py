
import requests
import os
prompt = [
    input("Chatgpt prompt:"),
    input("file name: ")     
]
api_endpoint = 'https://api.openai.com/v1/completions'
api_key = os.getenv("OPENAI_KEY")
header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + str(api_key),
}
request = {
    "model": "text-davinci-003",
    "prompt": f"write python script for {prompt[0]}",
    "max_tokens": 4000,
    "temperature": 0,
}
response = requests.post(api_endpoint, headers=header, json=request)
if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    print(response_text)
    with open(prompt[1],"w") as file:
        file.write(response_text)
else:
    print(f"Respond failed with error code: {response.status_code}")

'''import openai
apikey = ''
openai.api_key = apikey
openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        xxx
    ]
)'''
