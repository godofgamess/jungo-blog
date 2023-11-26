from django.contrib import admin
from .models import Product, News, Author

class ProductAdmin(admin.ModelAdmin):
    list_display = ('price', 'name')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'updated_at' )

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')

admin.site.register(Product, ProductAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Author, AuthorAdmin)
