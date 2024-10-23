from django.urls import path
from .views import SportListView, SportUpdateView, SportDetailView, SportDeleteView, SportCreateView
urlpatterns = [
    path('<int:pk>/edit/', SportUpdateView.as_view(), name='sport_edit'), 
    path('<int:pk>/', SportDetailView.as_view(), name='sport_detail'), 
    path('<int:pk>/delete/', SportDeleteView.as_view(), name='sport_delete'),
    path('', SportListView.as_view(), name='sport'),
    path('new/', SportCreateView.as_view(), name='sport_new'), 
]