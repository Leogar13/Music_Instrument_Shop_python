from django.urls import path
from django.views.generic import TemplateView
from administ import views

urlpatterns = [
    path('', views.login, name='loginadmin'),
    path('index.html', views.index, name = 'indexadmin'),
    path('maininfor.html', views.staffInfor, name = 'maininforadmin'),
    path('login.html', views.login, name='loginadmin'),
    path('logout.html', views.logout, name='logoutadmin'),
    path('manufactory.html', views.manufactory, name='manufactoryadmin'),
    # test
    path('manufactoryadd', views.productAdd, name='manufactoryaddadmin'),
    path('manufactoryedit/<int:manufactory_id>', views.productEdit, name='manufactoryeditadmin'),
    path('manufactorydelete', views.productDelete, name='manufactorydeleteadmin'),
    # 
    path('supplier.html', views.supplier, name='supplieradmin'),
    # test
    path('supplieradd', views.productAdd, name='supplieraddadmin'),
    path('supplieredit/<int:supplier_id>', views.productEdit, name='suppliereditadmin'),
    path('supplierdelete', views.productDelete, name='supplierdeleteadmin'),
    # 
    path('category.html', views.category, name='categoryadmin'),
    # test
    path('categoryadd', views.productAdd, name='categoryaddadmin'),
    path('categoryedit/<int:category_id>', views.productEdit, name='categoryeditadmin'),
    path('categorydelete', views.productDelete, name='categorydeleteadmin'),
    # 
    path('product.html', views.product, name='productadmin'),
    path('productadd', views.productAdd, name='productaddadmin'),
    path('productedit/<int:product_id>', views.productEdit, name='producteditadmin'),
    path('productdelete', views.productDelete, name='productdeleteadmin'),
    path('order.html', views.order, name='orderadmin'),
    path('orderdetail.html/<int:order_id>', views.orderDetail, name='orderdetailadmin'),
    path('updatestatus', views.updateStatus, name='updatestatusorderadmin'),
    path('user.html', views.getUser, name='useradmin'),
    path('role.html', views.getRole, name='roleadmin'),
    path('permission.html', views.getPermission, name='permissionadmin'),
]