from django.contrib import admin
from django.urls import path
from .views import homepage, windows95

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('windows95/', windows95, name='windows95'),

]
