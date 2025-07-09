from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
from django.contrib import messages

# Create your views here.

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Product created successfully.")
            return redirect('product_list')

    else:
        form = ProductForm()
    return render(request,'product_form.html',{'form':form})

def update_product(request,pk):
    product = get_object_or_404(Product,pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            messages.success(request,'Product updated successfully!.')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})
