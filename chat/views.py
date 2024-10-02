import openai
from django.shortcuts import render
from django.conf import settings

def chat_view(request):
    response = ""
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        if user_input:
            openai.api_key = settings.OPENAI_API_KEY
            try:
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Você é um assistente útil."},
                        {"role": "user", "content": user_input},
                    ],
                    max_tokens=150,
                    n=1,
                    stop=None,
                    temperature=0.7,
                )
                response = completion.choices[0].message['content'].strip()
            except Exception as e:
                response = f"Ocorreu um erro: {str(e)}"
    return render(request, "chat/chat.html", {"response": response})
