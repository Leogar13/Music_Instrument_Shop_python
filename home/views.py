from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . import connection
from home.models import Categories
import hashlib 
import json

# Create your views here.
cart = {}

def index(request):
    objGet = connection.getCate()
    return render(request, 'pages/index.html',{'Categories':objGet})

def logout(request):
    del request.session['user_id']
    del request.session['user_name']
    objGet = connection.getCate()
    return render(request, 'pages/index.html',{'Categories':objGet})

def getMyAccountInfo(request):
    id = request.session['user_id']
    objGet = connection.getCate()
    accountInfo = connection.getCustomerMainInfo(id)
    myBills = connection.getCustomerOrders(id)
    return render(request, 'pages/myaccount.html',{'Categories':objGet, 'myaccount':accountInfo, 'myBills': myBills})

def login(request):
    objGet = connection.getCate()
    if request.method == 'POST':
        getUserName = request.POST.get("username")
        getPassword = request.POST.get("password")
        hashpass = hashlib.md5(getPassword.encode('utf8')).hexdigest()
        
        # Check info user
        
        check = connection.login(getUserName,hashpass)
        if check == None:
            #false
            # return render(request, 'pages/index.html') 
            print("none is true")   
            testmess = "Your user or password is incorrect"
            return render(request,'pages/login.html',{'mess':testmess})
        else: 
            print("we have this customer")           
            request.session['user_id'] = check[0]
            request.session['user_name'] = connection.getCustomerMainInfo(check[0]).customerName
            return render(request, 'pages/index.html',{'Categories':objGet})


        # return render(request, 'pages/index.html')
    elif request.method == 'GET':
        return render(request, 'pages/login.html',{'Categories':objGet})

def signup(request):
    objGet = connection.getCate()
    if request.method == 'POST':
        name= request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email').lower()
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            hashpass = hashlib.md5(password1.encode('utf8')).hexdigest()
            result = connection.createCustomer(name, email, phone, address, hashpass)
            try:
                if result.ErrorNumber == 2627:
                    print(result.ErrorMessage)
                    return render(request, 'pages/signup.html',{'Categories':objGet, 'mess': result.ErrorMessage})
                else:
                    print('Its ok')
                    return redirect('login')
            except Exception as identifier:
                print(identifier)
                return redirect('login')
        else:
            return render(request, 'pages/signup.html',{'Categories':objGet, 'mess': "your password is not correct"})

    else:
        return render(request, 'pages/signup.html',{'Categories':objGet})  

def filter(request):
    objGet = connection.getCate()
    min = request.POST.get('min')
    max = request.POST.get('max')
    product = connection.getProductPrice(1, min, max)
    jsonlist = {}
    for i in product:
        jsonlist[i.productID] = {"name" : i.productName, "price": i.retailPrice, 'image': i.imageAddress, 'productID': i.productID}
    return JsonResponse({"instance": jsonlist}, status=200)

def searchProduct(request,pages):
    objGet = connection.getCate()
    if request.is_ajax():
        getParameter = request.POST.get('parametes')
        request.session['searchText'] = getParameter
        pages = int(request.POST.get('pages'))
        productSearch = connection.searchProduct(pages,getParameter)
        pageside = [pages-1,pages,pages+1]
        return render(request, 'pages/search.html',{'Categories':objGet, 'page': pageside, 'product': productSearch})  
    else:
        search = request.session['searchText']
        productSearch = connection.searchProduct(pages,search)
        pageside = [pages-1,pages,pages+1]
        return render(request, 'pages/search.html',{'Categories':objGet , 'SearchFor': search, 'page': pageside,'product': productSearch })  

def product(request,pages):
    cate = connection.getCate()
    product = connection.getProduct(pages)
    pageside = [pages-1,pages,pages+1]
    pageType = str(request.resolver_match.func.__name__)
    return render(request, "pages/product.html",{'page': pageside,'Categories':cate, 'product':product, 'pagetype': pageType})

def productCategory(request,pages,category_id):
    cate = connection.getCate()
    product = connection.getProductCate(pages,category_id)
    pageside = [pages-1,pages,pages+1]
    return render(request, "pages/productcategory.html",{'page': pageside,'Categories':cate, 'product':product, 'id': category_id})

def single(request,product_id):
    cate = connection.getCate()
    objGet = connection.getProductMainInfo(product_id)
    specification = connection.getProductSpecifications(product_id)
    listimg = connection.getProductImageList(product_id)
    return render(request, "pages/single.html",{'product':objGet, 'Categories': cate, 'specification': specification, 'imagelist': listimg})

def delCartItem(request):
    id= request.POST.get('id')
    try:
        del cart[id]
        request.session['cart']=cart
        return JsonResponse({"instance": "del"}, status=200)
    except Exception as e: # work on python 3.x
        print('Failed to upload to ftp: '+ str(e))
        return JsonResponse({"instance": "del"}, status=400)
    
    
def checkout(request):
    cate = connection.getCate()
    user = connection.getCustomerMainInfo(request.session['user_id'])
    return render(request, "pages/checkout.html",{'Categories': cate, 'user':user})

def postcart(request):
    if 'cart' in request.session:
        address = request.POST.get('addressShipping')
        payby = request.POST.get('payby')
        description = request.POST.get('description')
        myID = request.session['user_id']
        # create orders
        connection.createOrders(myID,address,description,payby)
        #get key to list

        listkey = [*request.session['cart']]
        for target_list in listkey:
            id = request.session['cart'].get(target_list).get('id')
            price = str(request.session['cart'].get(target_list).get('price'))
            number = request.session['cart'].get(target_list).get('number')
            connection.createOrdersDetail(id,myID,number,price)

        print('done')
        # del your cart
        cart.clear()
        request.session['cart'] = cart

        return redirect('index')
        # for value in request.session['cart']:
        #     for target_list in value:
        #         print(target_list)
    else:
        print('null')
        
    

def delCart(request):
    del request.session['cart']
    cart.clear()
    return JsonResponse({"instance": "del"}, status=200)

def addCart(request):
    if request.is_ajax():
        id= request.POST.get('id')
        num = request.POST.get('num')
        productInfo = connection.getProductMainInfo(id)
        if productInfo.counts == 0:
            print('not enough')
            return JsonResponse({"instance": "not enough"}, status=400)
        else:
            print('enough')
            if id in cart.keys():
                print("add")
                itemcart = {
                    'id':id,
                    'name':productInfo.productName,
                    'price':float(productInfo.retailPrice),
                    'number': int(cart[id]['number'])+1
                }
            else:
                print("new")
                itemcart = {
                    'id':id,
                    'name':productInfo.productName,
                    'price':float(productInfo.retailPrice),
                    'number': num
                }

            cart[id]=itemcart
            request.session['cart']=cart
            print(cart)
            return JsonResponse({"instance": "ENOUGH"}, status=200)


        


