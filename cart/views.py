from django.shortcuts import render, redirect, reverse, get_object_or_404

def view_cart(request):
    return render(request, "cart.html")


def add_to_cart(request, id):
    quantity=int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart    
    return redirect(reverse('index'))


def adjust_cart(request, id):
    quantity=int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart    
    return redirect(reverse('view_cart'))