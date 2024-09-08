from django.urls import path
from . import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:user_id>/', views.delete, name='delete'),
    path('update/<int:user_id>/', views.update, name='update'),
]