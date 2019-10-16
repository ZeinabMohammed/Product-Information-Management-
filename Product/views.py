from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy,reverse
from .models import Category,Product
from .serializers import CategorySerializer,ProductSerializer
from .forms import CategoryForm,ProductForm
from rest_framework import permissions,viewsets
from rest_framework.decorators import permission_classes
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
#*** DRF ENDPOINTS***

class CategoryList(viewsets.ModelViewSet):
	permission_classes = (permissions.AllowAny,)
	queryset	     = Category.objects.all()
	serializer_class = CategorySerializer
	filterset_fields = '__all__'
	search_fields 	 = '__all__'
	ordering   		 = ['name']

class ProductList(viewsets.ModelViewSet):
	permission_classes = (permissions.AllowAny,)
	queryset	       = Product.objects.all()
	serializer_class   = ProductSerializer
	filterset_fields   = '__all__'
	search_fields 	   = '__all__'
	ordering   		   = ['name']


#****TEMPLATE VIEWS***************
class CategoryView(ListView):
	template_name= "product/index.html"
	def get_queryset(self):
		return Category.objects.all()
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = CategoryForm
		return context
	def post(self, request, *args, **kwargs):
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			self.object_list = self.get_queryset()
			context = super().get_context_data(**kwargs)
			context['form'] = CategoryForm
			return self.render_to_response(context=context)
		else:
			context = super().get_queryset(**kwargs)
			context['form'] = CategoryForm
			return self.render_to_response(context=context)
class CategroyDetailView(ListView):
	model 		  = Product
	template_name ="product/detail.html"
	paginate_by   = 5

	def get_queryset(self):
		category_name = get_object_or_404(Category, name=self.kwargs.get('name'))
		return Product.objects.filter(category = category_name)
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = ProductForm
		return context
	def post(self, request, *args, **kwargs):
		form = ProductForm(request.POST)

		if form.is_valid():
			form.save()
			self.object_list = self.get_queryset()
			context = context = super().get_context_data(**kwargs)
			context['form'] = ProductForm
			return self.render_to_response(context=context)
		else:
			self.object_list = self.get_queryset()
			context = super().get_context_data(**kwargs)
			context['form'] = ProductForm

			return self.render_to_response(context=context)

	

class CategoryCreate(CreateView):
	model  = Category
	fields = ["name"]
	template_name='product/category_form.html'

class ProductCreate(CreateView):
	model  = Product
	fields = "__all__"
	template_name='product/product_form.html'
	success_url = reverse_lazy("Product:category-list")

class ProductUpdate(UpdateView):
	model  = Product
	fields = '__all__'

	template_name='product/product_update.html'

	success_url = reverse_lazy("Product:category-list")
class ProductDelete(DeleteView):
	model       = Product
	template_name='product/product_delete.html'
	success_url = reverse_lazy("Product:category-list")