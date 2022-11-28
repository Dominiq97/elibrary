from django.urls import path

from customer.views import Create, CustomerListView 

urlpatterns = [
    path('signup/', Create.as_view(), name='signup_customer'),
    path('customers_list/', CustomerListView.as_view(), name='customers_list'),

]
