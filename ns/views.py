from django.shortcuts import render
from ns.models import My_image, SortableMy_image

# Create your views here.

def promo(request):
    images_slider = My_image.objects.all()
    all_images = list()
    for image in images_slider:
        image_sl = SortableMy_image.objects.all().filter(title=image)
        images = [img.image.url for img in image_sl]
        image_id = '{}_{}'.format(image.title, image.id)
        nav_image_id = 'nav_{}_{}'.format(image.title, image.id)
        if image.cover:
            cover = 'url("{}")'.format(image.cover.url)
        else:
            cover = '#507D2A'
        data_image = {
            'title': image.title,
            'cover': cover,
            'image_id': image_id,
            'nav_image_id': nav_image_id,
            'images': images

        }
        all_images.append(data_image)

    return render(request, 'ns/promo.html', {'imgs': all_images})


# def test(request):
#     if request.method == 'GET':
#         return render(request, 'ns/test.html')