from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
# Create your views here.

def product_list(request) :
    products = Product.objects.all()
    # return HttpResponse("hello its product list") 
    return render(request, 'inventory_app/product_list.html', {'products': products})

def product_create(request) :
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product-list')
    # return HttpResponse("hello product form ")
    return render(request, 'inventory_app/product_form.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product-list')
    return render(request, 'inventory_app/product_form.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product-list')
    return render(request, 'inventory_app/confirm_delete.html', {'product': product})