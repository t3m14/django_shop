from django.contrib import admin
from main.models import User, Cart, Product

class userAdmin(admin.ModelAdmin):
    change_form_template = 'encript.html'

admin.site.register(User, userAdmin)
admin.site.register(Cart)
admin.site.register(Product)

# Register your models here
