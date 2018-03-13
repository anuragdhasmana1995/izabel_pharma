from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Products


# Create your views here.
# def index(request):
#     products = Products.objects.all()
#     html = ''
#     for product in products:
#         url = str(product.id) + '/'
#         html += '<a href = " ' + url + '">' + product.product_type + '</a><br>'
#     return HttpResponse(html)

# def index(request):
#     products = Products.objects.all()
#     template = loader.get_template('medicines/index.html')
#     context = {
#         'all_products': products,
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    products = Products.objects.all()
    context = {'all_products': products}
    return render(request, 'medicines/index.html', context)


def product_list(request, product_id):
    try:
        product = Products.objects.get(pk=product_id)
    except Products.DoesNotExist:
        raise Http404("The contents of this product does not exist")

    return render(request, 'medicines/product_list.html', {'product': product})


