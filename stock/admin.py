from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Group, Sub_Group, Address, Damage, Item, Location,Product, Product_Detail, Product_type, Supplier, Telephone

admin.site.register(Group)
admin.site.register(Sub_Group)
admin.site.register(Damage)
admin.site.register(Item)
admin.site.register(Location)
admin.site.register(Product)
admin.site.register(Product_Detail)
admin.site.register(Product_type)
admin.site.register(Supplier)
admin.site.register(Telephone)

admin.site.register(Address)
