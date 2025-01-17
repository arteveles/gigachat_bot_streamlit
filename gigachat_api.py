import json
import uuid

import streamlit as st
import requests
from requests.auth import HTTPBasicAuth

CLIENT_ID = st.secrets["CLIENT_ID"]
SECRET = st.secrets["SECRET"]


def get_access_token() -> str:
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': str(uuid.uuid4())
    }
    payload = {"scope": "GIGACHAT_API_PERS"}
    res = requests.post(
        url=url,
        headers=headers,
        auth=HTTPBasicAuth(CLIENT_ID, SECRET),
        data=payload,
        verify=False
    )
    access_token = res.json()["access_token"]
    return access_token

def get_image():
    pass

def send_prompt(msg: str, access_token: str):

    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    payload = json.dumps({
        "model": "GigaChat",
        "messages": [
            {
                "role": "user",
                "content": msg,
            }
        ],
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.post(
        url,
        headers=headers,
        data=payload,
        verify=False)
    return response.json()["choices"][0]["message"]["content"]

    print(response.text)

def send_prompt_and_get_response():
    pass