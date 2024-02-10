from django.shortcuts import render, redirect
from main.models import User, Cart, Product

def  cypher_the_password(password):
    result = ""
    for char in password:
        if 'a' <= char <= 'z':  # для маленьких латинских букв
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':  # для больших латинских букв
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        elif 'а' <= char <= 'я':  # для маленьких русских букв
            result += chr((ord(char) - ord('а') + 13) % 32 + ord('а'))
        elif 'А' <= char <= 'Я':  # для больших русских букв
            result += chr((ord(char) - ord('А') + 13) % 32 + ord('А'))
        else:
            result += char
    return result

def authenticate(username, password):
    try:
        user = User.objects.get(name=username)
        if user.syphered_password == cypher_the_password(password):
            return user
        else:
            return None
    except User.DoesNotExist:
        return None
def login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    return render(request, 'login.html')
def add_to_cart(request, product_id, user_id):
    product = Product.objects.get(id=product_id)
    user = User.objects.get(id=user_id)
    # cart = Cart(user=user, product=product, quantity=1).save()
    cart = Cart.objects.create(user=user, product=product, quantity=1)
    return redirect('index')

def cart(request, user_id):
    # get cart by user
    data = dict()
    User.objects.get(id=user_id)
    all_carts = Cart.objects.filter(user__id=user_id)
    #get all products in cart
    products = []
    for cart in all_carts:
        products.append(cart.product)
    print(products)
    data['products'] = products
    data['user'] = User.objects.get(id=user_id)

    # Render the HTML template index.html
    return render(request, 'cart.html', data)
def index(request):
    # Render the HTML template index.html
    if request.method == 'GET':
        return redirect('login')
    
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        if user is None:
            return redirect('login')
        data = dict()
        products = Product.objects.all()
        data["products"] = products
        data["user"] = user

        return render(request, 'index.html', data)
