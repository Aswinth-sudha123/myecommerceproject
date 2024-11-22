from . import views
from django.urls import path



urlpatterns=[
    path("",views.homepage,name="homepage"),
    path('loginpage',views.loginpage,name="loginpage"),
    path("registerpage",views.registerpage,name="registerpage"),
    path("login",views.login,name="login"),
    path("register",views.register,name="register"),
    path("logout",views.logout,name="logout"),
    path("userhome",views.userhome,name="userhome"),
    path("userlogout",views.userlogout,name="userlogout"),

    path("admin_home",views.admin_home,name="admin_home"),
    path('add_cata',views.add_cata,name='add_cata'),
    path('cata',views.cata,name="cata"),
    path('cata_detail',views.cata_detail,name="cata_detail"),
    path('edit_cata/<int:pk>',views.edit_cata,name="edit_cata"),
    path('edit_catagery/<int:pk>',views.edit_catagery,name="edit_catagery"),
    path('delect_cata/<int:pk>',views.delect_cata,name="delect_cata"),
    path('customer_detail',views.customer_detail,name="customer_detail"),
    path('Delete_customer/<int:pk>',views.Delete_customer,name="Delete_customer"),
    # product
    path("add_product",views.add_product,name="add_product"),
    path('product',views.product,name="product"),
    path("show_product",views.show_product,name="show_product"),
    path("edit_product_page/<int:pk>",views.edit_product_page,name="edit_product_page"),
    path("edit_product/<int:pk>",views.edit_product,name="edit_product"),
    path('delect_product/<int:pk>',views.delect_product,name="delect_product"),

    # user home
    path("userprofile",views.userprofile,name='userprofile'),
    path("change_password",views.change_password,name="change_password"),
    path("category_list/<int:pk>",views.category_list,name="category_list"),
    path('edit_profilepage/<int:pk>',views.edit_profilepage,name="edit_profilepage"),
    path("edit_profile/<int:pk>",views.edit_profile,name="edit_profile"),
    path("cart_list",views.cart_list,name="cart_list"),
    path("view_pro/<int:pk>",views.view_pro,name="view_pro"),
    path("add_to_cart/<int:pk>",views.add_to_cart,name="add_to_cart"),
    path("Increase_quantity/<int:id>",views.Increase_quantity,name="Increase_quantity"),
    path("Decrease_quantity/<int:id>",views.Decrease_quantity,name="Decrease_quantity"),
    path("remove_cart/<int:pk>",views.remove_cart,name="remove_cart"),
    path("Buy_now/<int:pk>",views.Buy_now,name="Buy_now"),
]