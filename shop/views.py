from django.db.models import F
from django.shortcuts import render, redirect

from shop.models import Product, Customer, Comment, Category, Review

products = Product.objects.all()
customers = Customer.objects.all()


def main_page(request):
    context = {
        'products': products,
        'customers': customers,
        'title': 'Home',
    }
    return render(request, 'index.html', context)


def wishlist(request):
    context = {
        'title': 'Wishlist',
    }
    return render(request, 'wishlist.html', context)


def error(request):
    context = {
        'title': 'Error',
    }
    return render(request, '404.html', context)


def account(request):
    context = {
        'title': 'Account',
    }
    return render(request, 'account.html', context)


def blog1(request):
    context = {
        'products': products[:9],
        'title': 'Blog-Archive',
    }

    return render(request, 'blog-archive.html', context)


def blog2(request):
    context = {
        'products': products[:9],
        'title': 'Blog-Archive2',
    }
    return render(request, 'blog-archive-2.html', context)


def blogsingle(request, pk):
    product = Product.objects.get(pk=pk)
    try:
        l_page = Product.objects.get(pk=int(pk) - 1).id
    except:
        l_page = Product.objects.get(pk=pk).id
    try:
        n_page = Product.objects.get(pk=int(pk) + 1).id
    except:
        n_page = Product.objects.get(pk=pk).id

    if request.method == 'POST':
        Comment.objects.create(
            name=request.POST['author'],
            email=request.POST['email'],
            website=request.POST['url'],
            comment=request.POST['comment'],
            product_id=product.id,
        )
        return redirect(f'/blogsingle/{pk}')
    comments = Comment.objects.all().filter(product_id=pk)
    count = len(comments)

    context = {
        'comments': comments,
        'count': count,
        'product': product,
        'n_page': n_page,
        'l_page': l_page,
        'title': 'Blog-Single',
    }
    return render(request, 'blog-single.html', context)


def cart(request):
    context = {
        'title': 'Cart',
    }
    return render(request, 'cart.html', context)


def checkout(request):
    context = {
        'title': 'Checkout',
    }
    return render(request, 'checkout.html', context)


def contact(request):
    context = {
        'title': 'Contact',
    }
    return render(request, 'contact.html', context)


def product(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'title': 'Product',
        'categories': categories,
    }
    return render(request, 'product.html', context)


def sort_product(request, category_id):
    products = Product.objects.all().filter(category_id=category_id)
    categories = Category.objects.all()
    context = {
        'products': products,
        'title': 'Product',
        'categories': categories,
    }
    return render(request, 'product.html', context)


def productdetail(request, pk):
    if request.method == "POST":
        Review.objects.create(
            name=request.POST['review_name'],
            email=request.POST['review_email'],
            review=request.POST['review_text'],
            rating=3,
            product_id=pk
        )
        return redirect(f'/productdetail/{pk}')

    p = Product.objects.get(pk=pk)
    p.watch += 1
    p.save()
    context = {
        'watch': p.watch,
        'one_product': Product.objects.get(pk=pk),
        'products': products[:7],
        'customers': customers,
        'title': 'Detail',
        'reviews': Review.objects.all().filter(product_id=pk),
    }
    return render(request, 'product-detail.html', context)
