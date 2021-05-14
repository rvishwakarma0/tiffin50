from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('',views.index, name="index"),
    path('kitchens/', views.kitchens, name="kitchens"),
    path('kitchens/<int:kid>', views.kitchen, name="kitchen"),
    path('kitchens/<int:kid>/<int:tid>', views.tiffin, name="tiffin")
]