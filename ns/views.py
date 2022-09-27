from django.shortcuts import render

# Create your views here.

def promo(request):
    if request.method == 'GET':
        return render(request, 'ns/promo.html')