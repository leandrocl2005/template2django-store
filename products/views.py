from django.shortcuts import render
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger

from products.models import Category, Product


# Create your views here.
def home(request):
  categories = Category.objects.all()
  new_products = Product.objects.all().order_by('-created_at')[:4]
  popular_products = Product.objects.filter(popular=True)[:4]
  context = {
      'categories': categories,
      'new_products': new_products,
      'popular_products': popular_products
  }
  return render(request, 'index.html', context)


def product_detail(request, pk):
  categories = Category.objects.all()
  product = Product.objects.get(id=pk)
  recommended_products = Product.objects.filter(recommended=True)[:4]
  context = {
      'categories': categories,
      "product": product,
      "recommended_products": recommended_products
  }
  return render(request, 'productdetail.html', context)


def products_list(request):
  products = Product.objects.all()

  category_name = request.GET.get('category', None)
  page_number = request.GET.get('page', None)
  search_term = request.GET.get('search', None)

  if category_name is not None:
    products = products.filter(category__name=category_name)

  if search_term is not None:
    products = products.filter(name__icontains=search_term)

  paginator = Paginator(products, 2)
  if page_number is not None:
    try:
      products = paginator.page(page_number)
    except EmptyPage:
      products = paginator.page(paginator.num_pages)
    except Exception:
      products = paginator.page(1)
  else:
    products = paginator.page(1)

  categories = Category.objects.all()
  context = {
      "products": products,
      "categories": categories,
      "category_name": category_name,
      "search_term": search_term
  }
  return render(request, 'products.html', context)
