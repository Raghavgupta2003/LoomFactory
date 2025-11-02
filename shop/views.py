from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Q
from .models import Category, Product, CartItem, Order

def home(request):
    categories = Category.objects.all()
    featured_products = Product.objects.filter(featured=True)[:8]
    
    # Get unique fabric and weave types for filters
    fabric_types = Product.objects.values_list('fabric_type', flat=True).distinct().exclude(fabric_type='')
    weave_types = Product.objects.values_list('weave_type', flat=True).distinct().exclude(weave_type='')
    
    context = {
        'categories': categories,
        'featured_products': featured_products,
        'fabric_types': fabric_types,
        'weave_types': weave_types,
    }
    return render(request, 'shop/home.html', context)

def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    
    # Filter handling
    fabric_type = request.GET.get('fabric_type')
    weave_type = request.GET.get('weave_type')
    
    if fabric_type:
        products = products.filter(fabric_type=fabric_type)
    if weave_type:
        products = products.filter(weave_type=weave_type)
    
    context = {
        'category': category,
        'products': products,
        'fabric_types': Product.objects.values_list('fabric_type', flat=True).distinct().exclude(fabric_type=''),
        'weave_types': Product.objects.values_list('weave_type', flat=True).distinct().exclude(weave_type=''),
    }
    return render(request, 'shop/category.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'shop/product_detail.html', context)

def search_products(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(
        Q(name__icontains=query) | 
        Q(description__icontains=query) |
        Q(category__name__icontains=query)
    )
    
    context = {
        'products': products,
        'query': query,
    }
    return render(request, 'shop/search_results.html', context)

def cart_view(request):
    # Always use session key since we don't have user authentication for cart
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    
    cart_items = CartItem.objects.filter(session_key=session_key)
    total = sum(item.get_total_price() for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'shop/cart.html', context)

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Always use session key for cart
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    
    cart_item, created = CartItem.objects.get_or_create(
        product=product, 
        session_key=session_key,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        cart_count = CartItem.objects.filter(session_key=session_key).count()
        return JsonResponse({'success': True, 'cart_count': cart_count})
    
    return redirect('cart')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart')

def checkout(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        order_notes = request.POST.get('order_notes', '')
        
        # Get cart items using session key
        session_key = request.session.session_key
        cart_items = CartItem.objects.filter(session_key=session_key)
        
        total_price = sum(item.get_total_price() for item in cart_items)
        
        # Create order
        order = Order.objects.create(
            customer_name=customer_name,
            phone=phone,
            email=email,
            address=address,
            total_price=total_price,
            order_notes=order_notes
        )
        
        # Clear cart
        cart_items.delete()
        
        return render(request, 'shop/order_success.html', {'order': order})
    
    # For GET request, show checkout form with cart items
    session_key = request.session.session_key
    if not session_key:
        return redirect('cart')
    
    cart_items = CartItem.objects.filter(session_key=session_key)
    total = sum(item.get_total_price() for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'shop/checkout.html', context)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')