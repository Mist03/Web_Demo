from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import DetailView, ListView, View
from .forms import RegisterForm
from .models import Post, Cart, CartProduct
from .forms import CartAddProductForm
from website.models import Post, CartProduct


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"


def home(request):
    return render(request, 'base.html')


def post_list(request):
    return render(request, 'website/post_list.html')


class AddToCartView(View):
    def post(self, request, post_id):
        product = get_object_or_404(Post, pk=post_id)
        cart, created = Cart.objects.get_or_create(user=request.user, ordered=False)
        cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_product.quantity += 1
            cart_product.save()
        return redirect('cart')




@login_required
def cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Post, pk=product_id)
        cart = Cart.objects.filter(user=request.user, ordered=False).first()
        if cart:
            cart_product = CartProduct.objects.filter(cart=cart, product=product).first()
            if cart_product:
                if cart_product.quantity > 1:
                    cart_product.quantity -= 1
                    cart_product.save()
                else:
                    cart_product.delete()
    cart_products = CartProduct.objects.filter(cart__user=request.user)
    items_data = []
    for item in cart_products:
        item_data = {
            'product': item.product,
            'product_id': item.product_id,
            'quantity': item.quantity,
            'price': item.product.price,
            'images': item.product.image,
            'total_price': item.product.price * item.quantity
        }
        items_data.append(item_data)
    total_price = sum(item['total_price'] for item in items_data)
    return render(request, 'website/cart.html',
                  {'items_data': items_data, 'total_price': total_price})




@login_required
def profile_view(request):
    return render(request, 'website/profile.html')


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            # login(request, user)
            return redirect('profile')
        else:
            return render(request, 'registration/register.html', {'form': form})
