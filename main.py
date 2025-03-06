import requests
import json

url = "https://www.chatbase.co/api/chat/cj8-h1spWC3gfNi97nW5v"

payload = json.dumps({
  "conversationId": "abc123xyz",
  "message": "Who is Owner of this website?",
  "sessionId": "1234567890",
  "chatbotId": "cj8-h1spWC3gfNi97nW5v",
  "timezone": "Asia/Kolkata",
  "clientInitialMessages": [
    "Hi",
    "How are you?"
  ]
})
headers = {
  'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate, br, zstd',
  'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8',
  'Cache-Control': 'public, max-age=0, must-revalidate',
  'Content-Type': 'application/json',
  'Origin': 'https://www.chatbase.co',
  'Referer': 'https://www.chatbase.co/chatbot-iframe/cj8-h1spWC3gfNi97nW5v',
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
  'DNT': '1',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-GPC': '1'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
