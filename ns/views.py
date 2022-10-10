from django.shortcuts import render
from ns.models import My_image

# Create your views here.

def promo(request):
    images_slider = My_image.objects.all()
    print(images_slider)
    for i in images_slider:
        print(i.cover)
        print(i.title)
        print(i.cover.url)
        print()
    if request.method == 'GET':
        return render(request, 'ns/promo.html', {'imgs': images_slider})

def test(request):
    if request.method == 'GET':
        return render(request, 'ns/test.html')