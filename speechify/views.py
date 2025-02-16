from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
from django.http import JsonResponse

def generate_speech(request):
    # Your speech generation logic here
    return JsonResponse({'message': 'Speech generated'})
