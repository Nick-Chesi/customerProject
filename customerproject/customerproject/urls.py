from django.contrib import admin
from django.urls import path
from .views import homepage, windows95, windows98, windowsxp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('windows95/', windows95, name='windows95'),
    path('windows98/', windows98, name='windows98'),
    path('windowsxp/', windowsxp, name='windowsxp'),
]
