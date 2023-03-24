from django.shortcuts import render
from products.models import Products, Comment


# Create your views here.
def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def products_view(request):
    if request.method == 'GET':


        products =Products.objects.all()

        context = {
            'products':products
        }
        return render(request, 'products/products.html', context=context)

def product_detail_view(request, id):
    if request.method == 'GET':
        product = Products.objects.get(id=id)

        context = {
            'product': product,
            'comments': product.comment_set.all()
        }

        return render(request, 'products/detail.html', context=context)
