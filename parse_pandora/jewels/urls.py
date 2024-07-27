from django.urls import path

# from products.views import ProductsListView, basket_add, basket_remove
from jewels.views import index

app_name = "jewels"

urlpatterns = [
    path("", index, name="index"),
]
