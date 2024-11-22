#from django.contrib import admin
#from django.utils import timezone
from django.urls import path
from . import views

app_name = "manager"

urlpatterns = [
    path('', views.index_view, name="manager_home"),  # Homepage
    path('menu_list_url/', views.menu_list, name="menu_list"),
    path('menu_add_url/', views.menu_add, name="menu_add"), # 메뉴 추가 페이지
    path('add_menu_data/', views.add_menu_data, name="add_menu_data"),  # Add a menu item
    # Menu detal page 작성
    path('detail/<int:menu_id>/', views.menu_detail, name="menu_detail"),
    path('add_option/<int:menu_id>/', views.add_option, name="add_option"),
    path('add_option_data/', views.add_option_data, name="add_option_data"),
]
