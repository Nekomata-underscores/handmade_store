from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('orders', views.orders, name="Orders"),
    path('log_in', views.log_in, name="Log_in"),
    path('catalogue', views.catalogue, name="Catalogue"),
    path('about_us', views.about_us, name="About_us"),
    path('my_profile', views.my_profile, name="My_profile"),
    path('our_products', views.our_products, name="Our_products"),
    path('contact_us', views.contact_us, name="Contact_us"),
    path('custom_order', views.custom_order, name="Custom_order"),
    path('add_product', views.add_product, name="add_product"),
    path('register', views.register, name="Register"),
    path('log_out', views.log_out, name="Log_out"),
    path('basket', views.basket, name="Basket"),
    path('add_to_basket/<int:product_id>', views.add_to_basket, name="Add_to_basket")
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )