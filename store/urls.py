from django.urls import path
from . import views  

urlpatterns = [
    path('',views.product_all,name='product_all'),
    path('<slug:category_slug>',views.product_all,name='product_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',views.product_detail_page, name='product_details'),
    path('search/', views.search_view, name='search'),

]
