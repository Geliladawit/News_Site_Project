from django.urls import path
from .views import SignUpView
from . import views
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('', views.home, name='home'),  
    path('news/', views.news, name='news'),  
    path('sport/', views.sport, name='sport'),
]
