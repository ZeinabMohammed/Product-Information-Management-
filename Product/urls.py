from django.urls import path, include
from rest_framework import routers
from .views import (ProductList,CategoryList,
					CategoryView,CategroyDetailView,
					CategoryCreate,ProductCreate,
					ProductDelete,ProductUpdate)
app_name='Product'

router = routers.DefaultRouter()
router.register('Categories', CategoryList)
router.register('Products',ProductList)

urlpatterns = [
	path('', include(router.urls)),
	path('categories/',CategoryView.as_view(),name='category-list'),
	path('category/<str:name>',CategroyDetailView.as_view(),name='category-detail'),
	path('category/add',CategoryCreate.as_view(),name='category-create'),
	path('product/add',ProductCreate.as_view(),name='product-add'),
	path('product/<pk>/delete',ProductDelete.as_view(),name='product-delete'),
	path('product/update/<pk>',ProductUpdate.as_view(),name='product-update'),
	]