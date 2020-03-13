"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from login.views import showLogin, checkLogin 
from dashboard.views import showDashboard
from products.views import addProduct,addP,showProducts,showHome,showCategoryManagemet,addCategory,showProductsClient,showProductPage,saveReview,addtemplate
from invoice.views import showInvoice
from mail.views import showInbox

urlpatterns = [
    path('', showHome),
    path('login/', showLogin),
    path('checkLogin/', checkLogin),
    path('dashboard/', showDashboard),
    path('categoryManagement/',showCategoryManagemet),
    path('addCategory/',addCategory),
    path('addtemplate/',addtemplate),
    path('addProduct/', addProduct),
    path('addP/', addP),
    path('showProducts/', showProducts),
    path('products/',showProductsClient),
    path('productDetail/',showProductPage),
    path('invoice/',showInvoice),
    path('inbox/', showInbox),
    path('saveReview/',saveReview),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
