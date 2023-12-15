from django.urls import path 
from . import views

urlpatterns = [
    path('', views.root,name='home'),
    path('process_money/', views.users_gold,name="url_process_money"),
    path('destroy_session',views.destroy_session,name="destroy_gold"),
    
]