from api import key
import requests
def chat1(chat):
    messages=[] #contains all msg
    system_message="You are an AI bot your name is Stark"
    message={"role":"user","parts": [{"text": system_message +" "+ chat}]  }
    messages.append(message)
    data={"contents":messages}
    url="https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response=requests.post(url,json=data )
    t1=response.json()
    #print(t1)
    t2=t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    print(t2)

chat=input("Enter the Query: ")
chat1(chat)