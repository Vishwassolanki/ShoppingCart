from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil


# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-n//4)

    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - n // 4)
        allProds.append([prod,range(1,nSlides), nSlides])
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    # allprods = [[products, range(1, nSlides), nSlides],
    #            [products, range(1, nSlides), nSlides]]
    params = {'allprods':allProds}
    return render(request, 'layout/index.html', params)
# def index(request):
#     products= Product.objects.all()
#     allProds=[]
#     catprods= Product.objects.values('category', 'id')
#     cats= {item["category"] for item in catprods}
#     for cat in cats:
#         prod=Product.objects.filter(category=cat)
#         n = len(prod)
#         nSlides = n // 4 + ceil((n / 4) - (n // 4))
#         allProds.append([prod, range(1, nSlides), nSlides])
#
#     params={'allProds':allProds }
#     return render(request,"layout/index.html", params)
def about(request):
    return render(request, 'layout/about.html')

def contact(request):
    if request.method == "POST":
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        number1 = request.POST.get('number')
        desc1 = request.POST.get('desc')
        contact0 = Contact(name=name1, email=email1, number=number1, desc=desc1)
        contact0.save()
        """Contact is model name 
            contact0 is one type of variable name we can any name to it
            name with orange color is came form database(or our model)
            and name with white color is as above we fetch data form user side in variable name name
            the name with 'name' is came from our html template or said user side input
             """
    return render(request, 'layout/contact.html')

def tracker(request):
    return render(request, 'layout/tracker.html')

def login(request):
    return HttpResponse("login page")

def products(request,myid):
    #fetch the product with id
    prod = Product.objects.filter(id=myid)
    return render(request, 'layout/prod_view.html',{'product':prod[0]})

def search(request):
    return HttpResponse("search page")

def cart(request):
    return HttpResponse("cart page")

def wishlist(request):
    return HttpResponse("wishlist page")

def orders(request):
    return HttpResponse("orders page")