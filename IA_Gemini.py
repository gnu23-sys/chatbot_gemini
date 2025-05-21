import requests

GEMINI_API_KEY = "SUA_API_KEY_AQUI"

def perguntar_gemini(pergunta):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }
    body = {
        "contents": [
            {
                "parts": [
                    {
                        "text": pergunta
                    }
                ]
            }
        ]
    }

    resposta = requests.post(url, headers=headers, json=body)

    if resposta.status_code == 200:
        conteudo = resposta.json()
        return conteudo["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"Erro: {resposta.status_code} - {resposta.text}"

# Loop do chatbot
print("🤖 Chatbot Gemini Ativo (digita 'sair' pra fechar)")
while True:
    user_input = input("Tu: ")
    if user_input.lower() in ["sair", "exit", "quit"]:
        print("Bot: Até já, truta 🤜🤛")
        break

    resposta = perguntar_gemini(user_input)
    print(f"Bot: {resposta}")
