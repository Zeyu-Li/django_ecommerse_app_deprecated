"""andrew_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, 
    PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView,
)
from login import views as user_views
from shop import views as shop_views
from shop.views import (
    ItemsView, ItemDetailView, add_to_cart
)

# TODO: 404 errors

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('home/', user_views.home_redirect, name='home_redirect'),
    path('register/', user_views.register, name="register"),
    path('profile/', user_views.profile, name='profile'),
    path('profile/edit/', user_views.edit_profile, name='edit_profile'),
    path('profile/password/', user_views.changepassword, name='changepassword'),
    path('login/', LoginView.as_view(template_name='login/login.html', redirect_authenticated_user=True), name="login"),
    path('logout/', LogoutView.as_view(template_name='login/home.html'), {'extra_context':{'message':'True','message_title':'Logout','message_text':'You have logged out successfully'}}, name="logout"),
    path('reset_password/', PasswordResetView.as_view(template_name='login/resetpassword.html', email_template_name='login/reset_password_email.html'), name="password_reset"),
    path('reset_password/done/', PasswordResetDoneView.as_view(template_name='login/text.html'), name="password_reset_done"),
    path('reset_password/complete/', PasswordResetCompleteView.as_view(template_name='login/home.html'), name="password_reset_complete"),
    path('reset_password/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='login/resetpassword.html'), name="password_reset_confirm"),

    # shop
    path('shop/', ItemsView.as_view(), name='item_list'),
    path('shop/product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('shop/checkout/', shop_views.checkout, name='checkout'),
    path('shop/add-to-cart/', shop_views.add_to_cart, name='add-to-cart'),

]
