from django.contrib import admin
from . models import Category, Product, MyCart, Payment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'image')

#django always adds an 'id' so you must always add it.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'price', 'max','image', 'description', 'featured', 'latest', 'available', 'women_dress', 'women_blouse', 'boy_shirt', 'boy_pant', 'men_jacket', 'men_trench', 'girl_dress', 'girl_skirt', 'min', 'max')

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'basket_no', 'quantity', 'paid_order')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'basket_no', 'pay_code', 'paid_order', 'first_name', 'last_name', 'phone', 'address', 'city', 'state', 'country')    
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin) 
admin.site.register(MyCart,ShopCartAdmin)   
admin.site.register(Payment,PaymentAdmin)           