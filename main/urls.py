from django.urls import path
from main.views import *

urlpatterns = [
    path('',index,name = "index"),
    path('accounts/profile/', index , name = "index"),
    path('add', add, name='add'),
    path('update/<int:todo_id>/', update, name='update'),
    path('delete/<int:todo_id>/', delete, name='delete'),
    path('edit/<int:id>/', edit, name='edit')

]