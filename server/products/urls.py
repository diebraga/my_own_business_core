from django.urls import path
from products.views import ProductListView, ProductFeaturedView, ProductView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<sku>', ProductView.as_view()),
    path('featured', ProductFeaturedView.as_view()),
]
