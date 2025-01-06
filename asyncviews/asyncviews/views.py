import asyncio
import httpx
from django.http import JsonResponse

# Função para chamada assíncrona
async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)

    async with httpx.AsyncClient() as client:
        r = await client.get('https://httpbin.org/')
        print(r)
        
        # Verifica se a resposta foi bem-sucedida
        if r.status_code == 200:
            try:
                return r.json()  
            except ValueError:
                return {"error": "Resposta não é um JSON válido"}
        else:
            return {"error": f"Erro ao acessar a API: {r.status_code}"}

# Função da view assíncrona
async def async_view(request):
    response = await http_call_async()  
    return JsonResponse(response)
