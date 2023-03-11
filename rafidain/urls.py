"""rafidain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from ordering.views import ordering,myorder,DeleteOrder,SendOrder,delitem
from products.views import main,recom,cat
from accounts.views import user_login,user_logout,myinfo, register
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('addprd/', Addprd ,name="addproduct"),
    path('', main ,name="home"),
    path('best/', recom ,name="recom"),
    path('login/', user_login ,name="login"),
    path('reg/', register ,name="reg"),
    path('sendorder/', SendOrder ,name="sendorder"),
    path('delorder/', DeleteOrder ,name="delorder"),
    path('add/<int:pk>', ordering ,name="add"),
    path('del/<int:pk>', delitem ,name="del"),
    path('logout/', user_logout ,name="logout"),
    path('myorder/',myorder,name="myorder"),
    path('myinfo/',myinfo,name="myinfo"),
    path('cat/<int:pk>',cat,name="cats")

    # path('edit/<int:id>/', editprd ,name="editproduct")
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)