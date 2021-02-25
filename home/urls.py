from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index.html', views.index, name = 'index'),
    path('product/pages/<int:pages>', views.product, name='product'),
    path('checkout.html', views.checkout, name='checkout'),
    path('product/category/<int:pages>/<int:category_id>', views.productCategory, name='productCategory'),
    path('single/<int:product_id>', views.single, name='detail'),
    path('login.html', views.login, name='login'),
    path('signup.html', views.signup, name='signup'),
    path('addcart', views.addCart, name='addCart'),
    path('postcart', views.postcart, name='postCart'),
    path('logout', views.logout, name='logout'),
    path('myaccount.html', views.getMyAccountInfo, name='myAccount'),
    path('search/<int:pages>', views.searchProduct, name='search'),
    path('searchfilter', views.filter, name='filter'),
    path('delcart', views.delCart, name='delcart'),
    path('delcartitem', views.delCartItem, name='delcartitem'),
]