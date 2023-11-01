from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .forms import LogInForm

app_name = 'onlinestore'

urlpatterns = [
    path('items/', include('item.urls')),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form = LogInForm), name='login'),
]