from django.shortcuts import render,redirect,get_object_or_404
from app.models import CatageryModel,productModel,CustomerModel,cartModel
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.conf import settings
from django.db import transaction




# Create your views here.
def homepage(request):
    return render(request,"home.html")

def userhome(request):
    catagary=CatageryModel.objects.all()
    product=productModel.objects.all()
    return render(request,"user_home.html",{'product':product,'catagery':catagary})

def userlogout(request):
    return redirect("homepage")


def admin_home(request):
    return render(request,"adminhome.html")

def loginpage(request):
    return render(request,"login.html")

def login(request):
        if request.method=="POST":
            username=request.POST["username"]
            password=request.POST["password"]

            user=auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                if(user.is_superuser):
                    return redirect("admin_home")
                else:
                    request.session['uid']=user.id
                    return redirect("userhome")
            else:
                messages.info(request,"Invalid username and password")
                return redirect("loginpage")
        else:
            return redirect("loginpage")

def registerpage(request):
    catagery=CatageryModel.objects.all()
    return render(request,"register.html",{'catagery':catagery})

def logout(request):
    auth.logout(request)
    return redirect("homepage")

def register(request):
     if request.method=="POST":
        # auth user table
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        cpassword=request.POST["cpassword"]
        # customer table
        f_name=request.POST["full_name"]
        address=request.POST["address"]
        age=request.POST["age"]
        phone=request.POST["phone"]
        image=request.FILES.get('file')


        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "This username is already exist, try new")
                return redirect("registerpage")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This email is already taken, try new!")
                return redirect("registerpage")
            else:
                user = User.objects.create_user(first_name=first_name,
                                                last_name=last_name,
                                                username=username,
                                                email=email,
                                                password=password)
                user.save()
                
                data = User.objects.get(id=user.id)
                custmer=CustomerModel(customer_name=f_name,
                                        customer_age=age,
                                        customer_phone=phone,
                                        Image=image,
                                        customer_address=address,
                                        customer=data)
                custmer.save()
                messages.success(request, "Registration successful, Please Login")
                return redirect("loginpage")

        else: 
            messages.info(request, "Password does not match!")
            return redirect("registerpage")
     
     else:

        return redirect("registerpage")
# catagery

def add_cata(request):
    return render(request,"add_catagory.html")


def cata(request):
    if request.method=='POST':
        cty_name=request.POST["catagery_name"]
        catagery=CatageryModel(Catagery=cty_name)
        catagery.save()
        messages.success(request,"Created Catagery!")
        return redirect("cata_detail")

def cata_detail(request):
    categery=CatageryModel.objects.all()
    return render(request,"catagory_detail.html",{'catagery':categery})

def delect_cata(request,pk):
    catagery=CatageryModel.objects.get(id=pk)
    catagery.delete()
    messages.success(request,"Catagery Removed!")
    return redirect("cata_detail")



def edit_cata(request,pk):
    catagery=CatageryModel.objects.get(id=pk)
    return render(request,"edit_cata.html",{'catagery':catagery})


def edit_catagery(request,pk):
    if request.method=='POST':
        catagery=CatageryModel.objects.get(id=pk)
        catagery.Catagery=request.POST['catagery_name']

        catagery.save()
        messages.success(request,"Updated details!")
        return redirect("cata_detail")
    

# product add, edit ,delete, show

def add_product(request):
    catagery=CatageryModel.objects.all()
    return render(request,"add_product.html",{'catagery':catagery})


def product(request):
    if request.method=='POST':
        pname=request.POST["product_name"]
        description=request.POST["description"]
        quantity=request.POST["quantity"]
        price=request.POST["price"]

        select=request.POST["select"]
    
        image=request.FILES.get("file") 

        if image==None:
            image="image/imgg.png"



        catagory=CatageryModel.objects.get(id=select)   

        product=productModel(Product_name=pname,
                               Description=description,
                               Price=price,
                               Quantity=quantity,
                               Image=image,
                               catagery=catagory)
        print("save data")
        product.save()
        messages.info(request,"product successfully Added!")
        return redirect("show_product")
    
def show_product(request):
    product=productModel.objects.all()
    return render(request,"product_detail.html",{'product':product})


def edit_product_page(request,pk):
    product=productModel.objects.get(id=pk)
    catagery=CatageryModel.objects.all()
    return render(request,"edit_product.html",{'product':product,'catagery':catagery})

def edit_product(request,pk):
    if request.method=='POST':
        product=productModel.objects.get(id=pk)

        product.Product_name=request.POST.get("product_name")
        product.Description=request.POST.get("description")
        product.Quantity=request.POST.get("quantity")
        product.Price=request.POST.get("price")

        old=product.Image
        new=request.FILES.get("file")

        if old!=None and new==None:
            product.Image = old
        else: 
            product.Image = new

        select = request.POST["select"]
        catagery = CatageryModel.objects.get(id=select)
        product.catagery = catagery

        product.save()
        messages.success(request,"details updated!")
        return redirect("show_product")


def delect_product(request,pk):
    product=productModel.objects.get(id=pk)
    product.delete()
    messages.success(request,"removed product details!")
    return redirect('show_product')


def customer_detail(request):
    customer=CustomerModel.objects.all()
    return render(request,"customer_detail.html",{'customer':customer})



def Delete_customer(request,pk):
    user=User.objects.get(id=pk)
    user.delete()
    return redirect("customer_detail")

# user home profile,cart,addtocart

def customer_nav(request,productID):
    catagery=CatageryModel.objects.all()
    return render(request,"customer_nav.html",{'catagery':catagery})

def userprofile(request):
    if 'uid' in request.session:
        userId = request.session['uid']
       
        user = CustomerModel.objects.get(customer=userId)
        return render(request,'customer_profile.html',{'user':user})
    else:
        return redirect('loginpage')

def edit_profilepage(request,pk):
    user=CustomerModel.objects.get(customer=pk)
    return render (request,"edit_profile.html",{'user':user})

def edit_profile(request,pk):
    user=User.objects.get(id=pk)
    customer=CustomerModel.objects.get(customer=pk)

    if request.method=='POST':
        # authtable
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.username = request.POST["username"]
        user.email = request.POST["email"]
      
        # usertable
        customer.customer_name=request.POST["full_name"]
        customer.customer_age=request.POST["age"]
        customer.customer_address=request.POST["address"]
        customer.customer_phone=request.POST["phone"]

        old = customer.Image
        new = request.FILES.get("file")

        if old != None and new == None:
          customer.Image = old
        else:
          customer.Image = new

        user.save()
        customer.save()
        return redirect('userprofile')
    
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

@login_required
def change_password(request):
    if request.method == "POST":
        old_password = request.POST["old_password"]
        new_password = request.POST["new_password"]
        confirm_new_password = request.POST["confirm_new_password"]

        user = request.user

        if not user.check_password(old_password):
            messages.error(request, "Incorrect old password. Please try again.")
            return redirect("change_password")

        if new_password != confirm_new_password:
            messages.error(request, "New passwords do not match. Please try again.")
            return redirect("change_password")
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user) 

        messages.success(request, "Password changed successfully.")
        return redirect("userprofile")

    return render(request,"changepass.html")



def view_pro(request,pk):
    product = get_object_or_404(productModel, id=pk)
    category = product.catagery

    context = {
        'product': product,
        'category': category,
    }

    return render(request, "viewpro.html", context)

def Buy_now(request, pk):
    product = get_object_or_404(productModel, id=pk)
    category = product.catagery 
    customer = CustomerModel.objects.filter(customer=request.user).first()  
    
    context = {
        'product': product,
        'category': category,
        'customer': customer, 
    }

    return render(request, "buy.html", context)



def cart_list(request):
    cat=CatageryModel.objects.all()
    cart_list=cartModel.objects.filter(user=request.user).select_related('product')
    total_price= sum(item.total_price() for item in cart_list)
    return render(request,'addcart.html',{"cart_list":cart_list,"total_price":total_price, 'cat':cat})



def add_to_cart(request, pk):
    product = productModel.objects.get(id=pk)
    cart_item, created = cartModel.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        cart_item.product_quantity += 1
        cart_item.save()
        
    return redirect("cart_list")


def Increase_quantity(request,id):
    cart_item=cartModel.objects.get(product_id=id,user=request.user)
    cart_item.product_quantity += 1
    cart_item.save()
    with transaction.atomic():
        cart_item.product.Quantity -=1
        cart_item.product.save()
    return redirect('cart_list')


def Decrease_quantity(request,id):
    cart_item=cartModel.objects.get(product_id=id,user=request.user)
    cart_item.product_quantity -=1
    cart_item.save()
    with transaction.atomic():
        cart_item.product.Quantity +=1
        cart_item.product.save()
    return redirect("cart_list")

def remove_cart(request,pk):
    product=productModel.objects.get(id=pk)
    cart_item=cartModel.objects.filter(user=request.user,product=product).first()

    if cart_item:
        cart_item.delete()
        return redirect("cart_list")
    
def category_list(request,pk):
    category=CatageryModel.objects.filter(id=pk)
    if category.exists():
        category=category.first()
        product=productModel.objects.filter(catagery=category)
        return render(request, 'cata_list.html', {'category': [category], 'product': product})
    else:
        return render(request, 'user_home.html')
    

