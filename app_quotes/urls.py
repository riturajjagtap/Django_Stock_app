# APP_QUOTES --> urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('add_stock/', views.add_stock, name='add_stock'),
    path('delete/<stock_id>', views.delete_stock, name='delete_stock'),
    path('delete_stocks_page', views.delete_stocks_page, name='delete_stocks_page'),    
]
