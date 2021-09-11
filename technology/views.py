from django.shortcuts import render,get_object_or_404
from catagory.models import Catagory
from .models import Technology
from django.core.paginator import Paginator

from AboutMe.models import AboutMe

# Create your views here.
def store(request,catagory_slug=None):
    catagories=None
    products=None
    product_coun=0

    if catagory_slug != None:
        catagories=get_object_or_404(Catagory,slug=catagory_slug)
        products=Technology.objects.filter(catagory=catagories,is_available=True).order_by('id')
        #products_count=products.count()
        paginator=Paginator(products,6)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
        about=AboutMe.objects.all()

    else:
        products=Technology.objects.all().filter(is_available=True).order_by('id')
        #product_count=products.count()
        paginator=Paginator(products,6)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
        about=AboutMe.objects.all()


    context={
    'products':paged_products,
    'about':about,
    #'product_count':product_count,
    }

    return render(request,'index.html',context)
