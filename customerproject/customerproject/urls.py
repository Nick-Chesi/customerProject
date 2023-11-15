from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import homepage, windows95, windows98, windowsxp, manage_textboxes, edit_textbox, login_view, logout_view
from .views import windowsVista, windows7, windows8, windows10, windows11, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('windows95/', windows95, name='windows95'),
    path('windows98/', windows98, name='windows98'),
    path('windowsxp/', windowsxp, name='windowsxp'),
    path('windowsVista/', windowsVista, name='windowsVista'),
    path('windows7/', windows7, name='windows7'),
    path('windows8/', windows8, name='windows8'),
    path('windows10/', windows10, name='windows10'),
    path('windows11/', windows11, name='windows11'),
    path('manage_textboxes/', manage_textboxes, name='manage_textboxes'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('textboxes/<int:pk>/edit/', edit_textbox, name='edit_textbox'),
    path('register/', register, name='register'),
]
