from django.shortcuts import render
from openai import OpenAI
import os
from dotenv import load_dotenv
from django.http import JsonResponse
from .models import Chat

load_dotenv()
client = OpenAI(api_key=os.environ.get('OPENAI_KEY'))

f = open('context.txt', 'r')
model_instructions = f.read()
f.close()

def index(request):
    Chat.objects.all().delete()
    return render(request, 'index.html')

def response(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')

        chat_hist = Chat.objects.order_by('-create_dtm')
        messages = [
            {"role": "system", "content": model_instructions},
            {"role": "user", "content": message}
        ]
        
        for chat in reversed(chat_hist):
            messages.append({"role": "user", "content": chat.message})
            messages.append({"role": "assistant", "content": chat.response})

        messages.append({"role": "user", "content": message})
        
        completion = client.chat.completions.create(model="gpt-4o", messages=messages)
        answer = completion.choices[0].message.content

        new_chat = Chat(message=message, response=answer)
        new_chat.save()

        return JsonResponse({'response': answer})
    
    return JsonResponse({'response': 'Invalid request'}, status=400)
