from google import genai
from google.genai import errors

chave = "xxxx"

#https://aistudio.google.com/api-keys

print("Agora vou me conectar no Gemini uhuuu!")
try:
    cliente = genai.Client(api_key=chave)
    resposta = cliente.models.generate_content(
        model="gemini-3.5-flash",
        contents="O professor já passou a lista?"
    )
    print("Resposta: ", resposta.text)
except errors.ServerError as erro:
    if erro.code == 503:
        print("Gemini está temporarimante fora")
        print("Tente mais tarde")
    else:
        print("Erro no servidor: ", erro)

