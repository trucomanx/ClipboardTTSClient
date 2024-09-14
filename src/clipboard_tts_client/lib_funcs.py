#!/usr/bin/python3

from langdetect import detect
import requests

def tts_play(text):
    # Retorna uma string com base no texto passado
    if text.strip()=="":
        return "";
    
    SERVER_URL = 'http://localhost:5000'
    DATA={
        "text": text, 
        "language": detectar_linguagem(text),
        "split_pattern": [".", "\n\n"], 
        "speed":1.25 
    }
    ret_str=send_json_from_dict(SERVER_URL,DATA);
    
    return ret_str;

def detectar_linguagem(texto):
    try:
        linguagem = detect(texto)
        return linguagem
    except Exception as e:
        return "en";


def send_json_from_dict(server_url,data):
    # Enviar solicitação POST ao servidor
    response = requests.post(f'{server_url}/add_task', json=data)

    if response.status_code == 200:
        print(f"Task sent successfully! ID: {response.json()['id']}")
        return response.json()['id'];
    else:
        print("Error submitting task.")
        return None
