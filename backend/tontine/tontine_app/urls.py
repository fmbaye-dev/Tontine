from django.urls import path
from .import views

urlpatterns = [
    path('ajout_versement/', views.createVersement),   #* Create
    path('versements/', views.list_versement),  #* Read
    path('modsupp_versement/<uuid:pk>', views.DetailsUpdateDeleteVersement)  #* Update Delete
]