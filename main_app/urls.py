from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finch_detail, name='detail'),
    path('finches/create', views.FinchCreate.as_view(),name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('cats/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('hats/', views.HatList.as_view(), name='hats_index'),
    path('hats/<int:pk>/', views.HatDetail.as_view(), name='hats_detail'),
    path('hats/create/', views.HatCreate.as_view(), name='hats_create'),
    path('hats/<int:pk>/update/', views.HatUpdate.as_view(), name='hats_update'),
    path('hats/<int:pk>/delete/', views.HatDelete.as_view(), name='hats_delete'),
    path('hats/<int:finch_id>/assoc_hat/<int:hat_id>/', views.assoc_hat, name='assoc_hat')
] 
