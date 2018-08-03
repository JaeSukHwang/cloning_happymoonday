"""happymoon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/pad/', views.product_list),
    path('store/pad/<int:pk>/', views.product_detail),
    path('subscription/', include('subscription.urls')),
    path('subscription_detail/', include('subscription.urls')),
    #     subscription_detail/이부분에 HM-A, HM-B 이렇게 생기는데 이거 어떻게 하지?

]