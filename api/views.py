from django.shortcuts import render
from django.http import JsonResponse

def test(request):
    data = {
        'data': 'success'
    }
    return JsonResponse(data)
