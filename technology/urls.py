
from django.urls import path
from . import views

urlpatterns = [
        path('catagory/<slug:catagory_slug>/',views.store,name='product_by_catagory'),
]
