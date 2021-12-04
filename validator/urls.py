from django.urls import path, include
from .api.validator import  ValidatorCPF

urlpatterns = [ 
    path("<str:cpf>/",  ValidatorCPF.as_view(),  name="validator_cpf" )
]
