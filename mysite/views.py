from django.http import HttpResponse
from django.shortcuts import render ,redirect
from app.models import Slider,Banner,Main_Category,Product,Category,Color,Brand
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Max, Min , Sum
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
def home(request):
    slider = Slider.objects.all()
    banner = Banner.objects.all()
    main_category = Main_Category.objects.all()
    product = Product.objects.all()
    data = {
        'slider':slider,
        'banner':banner,
        'main_category':main_category,
        'product':product,
    }
    return render (request,'home.html',data)


def ABOUT(request):
    return render (request,'about.html')


def CONTACT(request):
    return render (request,'contact.html')


def PRODUCT(request):
    product = Product.objects.all()
    category = Category.objects.all()
    min_price = Product.objects.all().aggregate(Min('price'))
    max_price = Product.objects.all().aggregate(Max('price'))
    color = Color.objects.all()
    FilterPrice = request.GET.get('FilterPrice')
    ColorID = request.GET.get('colorID') 
    brand = Brand.objects.all()
    if FilterPrice:
        Int_FilterPrice = int(FilterPrice)
        product = Product.objects.filter(price__lte = Int_FilterPrice)
    elif ColorID:
        product = Product.objects.filter(color = ColorID)
    else:
        product = Product.objects.all()  

    data = {
        'product':product,
        'category':category,
        'min_price':min_price,
        'max_price':max_price,
        'FilterPrice':FilterPrice,
        'color':color,
        'brand':brand,
    }

    return render (request,'product/product.html',data)


def PRODUCT_DETAIL(request,slug):
    product = Product.objects.filter(slug = slug)
   
    if product.exists():
        product = Product.objects.get(slug = slug)
    else:
        return redirect ("error404")  

    


    


    data = {
        'product':product,
        
    }

    return render (request,'product_detail.html',data)

def LOGIN(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username,password = password)

        if user is not None:
            login(request,user)
            return redirect ('home')
        else:
            messages.success(request,'There was a error plz try again')
            return redirect ('login')
    return render (request,'registration/login.html')

def REGISTER(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User(username = username,email = email)

        user.set_password(password)

        user.save()

    return render (request,'registration/login.html')
    
            

def LOGOUT(request):
    logout(request)
    return redirect ('home')


def ERROR404(request):
    return render (request,'error404.html')





def filter_data(request):
    category = request.GET.getlist('category[]')
    brands = request.GET.getlist('brand[]')

    all_products = Product.objects.all().order_by('-id').distinct()

    if category:
        all_products = all_products.filter(category__id__in=category)

    if brands:
        all_products = all_products.filter(brand__id__in=brands)

    # Render the product HTML template
    html_content = render_to_string('ajax/product.html', {'product': all_products})

    return JsonResponse({'data': html_content})

















@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    cart = request.session.get('cart')
    packing_cost = sum(i['packing_cost']for i in cart.values() if i)
    tax = sum(i['tax'] for i in cart.values() if i)
   
    data = {
        'packing_cost':packing_cost,
        'tax':tax,
    }
    return render(request, 'cart/cart.html',data)


def CHECKOUT(request):
    return render (request,'checkout.html')








