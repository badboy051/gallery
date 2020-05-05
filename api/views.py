from django.shortcuts import render


# Create your views here.

def handler404(request, exception):
    context = {}
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response
