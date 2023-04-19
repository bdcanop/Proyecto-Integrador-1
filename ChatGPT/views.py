# import openai
# from django.shortcuts import render
# from django.http import JsonResponse

# def chat(request):
#     if request.method == 'POST':
#         input_text = request.POST.get('input_text')
#         openai.api_key = "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"
#         response = openai.Completion.create(
#             engine="text-davinci-003",
#             prompt=input_text,
#             max_tokens=1024
#         )
#         output_text = response.choices[0].text.strip()
#         return JsonResponse({'response': output_text})
#     return render(request, 'chat.html')

import openai
from openai import Completion
from django.shortcuts import render
from django.http import JsonResponse


def chat(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        openai.api_key = "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"
        """response = openai.Completion.create(
            engine="text-davinci-003", #text-gpt3-5-turb-0301
            prompt=input_text,
            max_tokens=1024,
            n = 1,
            stop = None,
            temperature = 0.7,
        )"""
        completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generar respuesta de chat a partir del siguiente texto: {input_text}\n",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
        #response = openai.Completion.create(engine="text-davinci-002", prompt=input_text, max_tokens=2000, ...)
        output_text = completions.choices[0].text
        return JsonResponse({'response': output_text})
    return render(request, 'chat.html')
# Create your views here.