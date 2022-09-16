from django.contrib import admin
from .models import Product, User
from django.contrib.auth.models import Group


admin.site.register(Product)
admin.site.register(User)
admin.site.unregister(Group)


admin.site.site_header = "ECommerce Admin"
admin.site.site_title = "ECommerce Admin Portal"
admin.site.index_title = "Welcome to ECommerce Researcher Portal"
