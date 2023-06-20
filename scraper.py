from key import API_KEY
import requests
import json

def gpt_get_message(question):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_model = "gpt-3.5-turbo"

    body_message = {
        "model": id_model,
        "messages": [{"role": "user", "content": question}]
    }

    body_message = json.dumps(body_message)

    requisicao = requests.post(link, headers=headers, data=body_message)
    resposta = requisicao.json()
    mensagem = resposta["choices"][0]["message"]["content"]
    print(mensagem)

def atuar_area(acao, objeto, _):
    executado = False

    if acao == "área" and objeto in ["região nordeste", "região sudeste", "região sul", "região centro-oeste", "região norte"]:  
        executado = True
        
        print(f"É claro! Aqui estão informações sobre a área da {objeto} do Brasil...")
        gpt_get_message(f"Qual a área da {objeto} do Brasil?")

    return executado

def atuar_flora(acao, objeto, _):
    executado = False

    if acao == "flora" and objeto in ["região nordeste", "região sudeste", "região sul", "região centro-oeste", "região norte"]:  
        executado = True
        
        print(f"É claro! Aqui estão informações sobre a flora da {objeto} do Brasil...")
        gpt_get_message(f"Me dê informações sobre a flora da {objeto} do Brasil?")

    return executado

def atuar_fauna(acao, objeto, _):
    executado = False

    if acao == "fauna" and objeto in ["região nordeste", "região sudeste", "região sul", "região centro-oeste", "região norte"]:  
        executado = True
        
        print(f"É claro! Aqui estão informações sobre a fauna da {objeto}...")
        gpt_get_message(f"Me dê informações sobre a fauna da {objeto} do Brasil?")

    return executado

def atuar_afluentes(acao, objeto, _):
    executado = False

    if acao == "afluentes" and objeto in ["região nordeste", "região sudeste", "região sul", "região centro-oeste", "região norte"]:  
        executado = True
        
        print(f"É claro! Aqui estão informações sobre os principais afluentes da {objeto}...")
        gpt_get_message(f"Quais os principais afluentes da {objeto} do Brasil?")

    return executado

def atuar_clima(acao, objeto, _):
    executado = False

    if acao == "clima" and objeto in ["região nordeste", "região sudeste", "região sul", "região centro-oeste", "região norte"]:  
        executado = True
        
        print(f"É claro! Aqui estão informações sobre o clima da {objeto}...")
        gpt_get_message(f"Como é o clima da {objeto} do Brasil?")

    return executado

def atuar_população(acao, objeto, _):
    executado = False

    if acao == "população" and objeto in ["região nordeste", "região sudeste", "região sul", "região centro-oeste", "região norte"]:  
        executado = True
        
        print(f"É claro! Aqui estão informações sobre a população da {objeto}...")
        gpt_get_message(f"Qual a população da {objeto} do Brasil?")

    return executado