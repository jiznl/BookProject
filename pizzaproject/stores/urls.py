from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.PizzariaListAPIView.as_view(),name="pizzeria_list"),
    path('<int:id>/',views.PizzariaRetrieveAPIView.as_view(),name="pizzeria_detail"),
    path('create/',views.PizzeriaCreateAPIView.as_view(),name = "pizzeria_create"),
    path('update/<int:id>/',views.PizzariaRetrieveUpdateAPIView.as_view(),name='pizzeria_update'),
    path('delete/<int:id>/',views.PizzariaDestroyAPIView.as_view(),name='pizzeria_delete'),
]