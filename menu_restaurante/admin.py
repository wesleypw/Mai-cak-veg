from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_promotion', 'promotional_price', 'discount_percentage')
    list_filter = ('category', 'is_promotion')
    search_fields = ('name', 'description')
    list_editable = ('is_promotion', 'promotional_price', 'discount_percentage')
    
    # Campos organizados em grupos no formulário de edição
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'category', 'description', 'image')
        }),
        ('Preços', {
            'fields': ('price',)
        }),
        ('Promoção', {
            'fields': ('is_promotion', 'promotional_price', 'discount_percentage'),
            'description': 'Marque "is_promotion" para exibir o produto na seção de promoções'
        }),
    )

admin.site.register(MenuItem, MenuItemAdmin)
