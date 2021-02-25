from django.shortcuts import render,redirect
from . import connectionadmin
import hashlib
from django.http import HttpResponseRedirect, JsonResponse

permission = {}

# Create your views here.
def index(request):
    if 'staff_id' in request.session:
        return render(request,'adminpages/index.html')    
    else:
        return redirect('loginadmin')

def staffInfor(request):
    if 'staff_id' in request.session:
        id = request.session['staff_id']
        getinfor = connectionadmin.getStaffMainInfo(id)
        return render(request,'adminpages/staffinfor.html',{'myaccount': getinfor})    
    else:
        return redirect('loginadmin')

def getUser(request):
    if 'staff_id' in request.session:
        # check permission
        if 'selectStaff' in request.session['staff_permission'].values():    
            # get product
            getUser = connectionadmin.getAllUser()
            return render(request,'adminpages/user.html',{'user': getUser})
        else:
            return redirect('indexadmin')    
    else:
        return redirect('loginadmin')

def getRole(request):
    if 'staff_id' in request.session:
        # check permission
        if 'selectGroup' in request.session['staff_permission'].values(): 
            # get product
            getRole = connectionadmin.getAllRole()
            return render(request,'adminpages/role.html',{'role': getRole}) 
        else:
            return redirect('indexadmin')    
    else:
        return redirect('loginadmin')

def getPermission(request):
    if 'staff_id' in request.session:
        # check permission
        if 'selectPermission' in request.session['staff_permission'].values(): 
            # get product
            getPermission = connectionadmin.getAllPermission()
            return render(request,'adminpages/permission.html',{'permission': getPermission})    
        else:
            return redirect('indexadmin') 
    else:
        return redirect('loginadmin')

def order(request):
    if 'staff_id' in request.session:
        # check permission
        if 'selectOrder' in request.session['staff_permission'].values(): 
            # get product
            getorder = connectionadmin.getOrder()
            return render(request,'adminpages/order.html',{'order': getorder})     
        else:
            return redirect('indexadmin') 
          
    else:
        return redirect('loginadmin')

def orderDetail(request,order_id):
    if 'staff_id' in request.session:
        # check permission
        
        # get orderdetail
        getorderdetail = connectionadmin.getOrderDetailInOrder(order_id)
        statuslist = connectionadmin.getAllStatus()
        orderStatus = connectionadmin.getOrderStatus(order_id)
        return render(request,'adminpages/orderdetail.html',{'orderstatus': orderStatus,'status': statuslist,'orderdetail': getorderdetail, 'permission' : permission})    
    else:
        return redirect('loginadmin')

def updateStatus(request):
    statusid = request.POST.get('status')
    orderid = request.POST.get('orderid')
    userid = request.session['staff_id']
    connectionadmin.updateStatus(orderid, statusid, userid)
    return JsonResponse({"instance": "del"}, status=200)
    

def manufactory(request):
    if 'staff_id' in request.session:
        # check permission
        if 'selectManufactory' in request.session['staff_permission'].values(): 
            # get product
            manufactory = connectionadmin.getManufactory()
            return render(request,'adminpages/manufactory.html',{'manufactory': manufactory})   
        else:
            return redirect('indexadmin') 
           
    else:
        return redirect('loginadmin')

def supplier(request):
    if 'staff_id' in request.session:
        # check permission
        if 'selectSupplier' in request.session['staff_permission'].values(): 
            # get product
            supplier = connectionadmin.getSupplier()
            return render(request,'adminpages/supplier.html',{'supplier': supplier})   
        else:
            return redirect('indexadmin')
           
    else:
        return redirect('loginadmin')

def category(request):
    if 'staff_id' in request.session:
        # check permission
        
        # get product
        getcategory = connectionadmin.getCategory()
        return render(request,'adminpages/category.html',{'category': getcategory, 'permission' : permission})    
    else:
        return redirect('loginadmin')


def product(request):
    if 'staff_id' in request.session:
        # check permission
        
        # get product
        product = connectionadmin.selectProduct()
        return render(request,'adminpages/product.html',{'product': product, 'permission' : permission})    
    else:
        return redirect('loginadmin')
    
def productAdd(request):
    if 'staff_id' in request.session:
        getcate = connectionadmin.getCategory()
        getmanu = connectionadmin.getManufactory()
        getsup = connectionadmin.getSupplier()
        # check permission
        print(permission)
        if 'insertProduct' in permission.values():
            # get request
            if request.method == 'POST':
                # get post
                productName = request.POST.get('productname')
                price = request.POST.get('price')
                category = request.POST.get('category')
                manufactory = request.POST.get('manufactory')
                supplier = request.POST.get('supplier')
                description = request.POST.get('description')
                # add
                connectionadmin.insertProduct(productName,category,manufactory,supplier,price,description)
                return redirect('productadmin')
            else:
                return render(request,'adminpages/productadd.html', {'category' : getcate, 'manufactory': getmanu, 'supplier': getsup})    
        else:
            return redirect('indexadmin')
        
    else:
        return redirect('loginadmin')

def productEdit(request,product_id):
    if 'staff_id' in request.session:
        getcate = connectionadmin.getCategory()
        getmanu = connectionadmin.getManufactory()
        getsup = connectionadmin.getSupplier()
        # check permission
        print(permission)
        if 'updateProduct' in permission.values():
            # get request
            if request.method == 'POST':
                # getpost
                productName = request.POST.get('productname')
                price = request.POST.get('price')
                category = request.POST.get('category')
                manufactory = request.POST.get('manufactory')
                supplier = request.POST.get('supplier')
                description = request.POST.get('description')
                
                # update
                connectionadmin.updateProduct(productName,category,manufactory,supplier,price,description,product_id)
                return redirect('productadmin')
            else:
                # get product
                product = connectionadmin.getProductMainInfo(product_id)
                return render(request,'adminpages/productedit.html',{'product': product, 'category' : getcate, 'manufactory': getmanu, 'supplier': getsup})    
        else:
            return redirect('indexadmin')
        
           
    else:
        return redirect('loginadmin')

def productDelete(request):
    product_id = request.POST.get('id')
    connectionadmin.deleteProduct(product_id)
    return JsonResponse({"instance": "del"}, status=200)

def login(request):
    if request.method == 'POST':
        getUserName = request.POST.get("emailstaff")
        getPassword = request.POST.get("passwordstaff")
        hashpass = hashlib.md5(getPassword.encode('utf8')).hexdigest()
        #check user
        check = connectionadmin.loginStaff(getUserName,hashpass)
        if check == None:
            #false
            # return render(request, 'pages/index.html') 
            print("We have no staff")   
            testmess = "Your user or password is incorrect"
            return render(request,'adminpages/login.html',{'mess':testmess})
        else: 
            print("we have this staff")           
            request.session['staff_id'] = check[0]
            
            # get permission to dictionary
            listpermision = connectionadmin.getStaffPermission(check[0])
            for i in listpermision:
                permission[i.permissionID] = i.permissionDetail
            request.session['staff_permission'] = permission
            print(permission)
            # get user Name
            user = connectionadmin.getStaffMainInfo(check[0])
            print(user[1])
            request.session['staff_name'] = user[1]
            return redirect('indexadmin')
            
        
    else:
        return render(request, 'adminpages/login.html')

def logout(request):
    del request.session['staff_id']
    del request.session['staff_name']
    del request.session['staff_permission']
    permission.clear()
    return redirect('loginadmin')

