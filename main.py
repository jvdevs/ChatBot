import re

def responder_pergunta(pergunta):
    respostas = {
        "oi": "Olá! Como posso te ajudar?",
        "qual é o seu nome": "Sou um chatbot simples!",
        "como você está": "Estou bem, obrigado por perguntar!",
        "adeus": "Tchau! Tenha um ótimo dia!",
        "qual é a capital do Brasil": "A capital do Brasil é Brasília.",
        "qual é a capital de portugal": "A capital de Portugal é Lisboa."
    }

    pergunta = pergunta.lower()
    
    for chave in respostas:
        if re.search(chave, pergunta):
            return respostas[chave]
    
    return "Desculpe, não entendi. Poderia reformular a pergunta?"


print("Chatbot iniciado! Digite 'sair' para encerrar.")
while True:
    usuario = input("Você: ")
    if usuario.lower() == "sair":
        print("Chatbot: Até mais!")
        break
    resposta = responder_pergunta(usuario)
    print(f"Chatbot: {resposta}")
