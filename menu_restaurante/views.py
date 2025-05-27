from django.shortcuts import render
from .models import MenuItem

def menu_view(request):
    # Busca produtos em promoção
    promotion_items = MenuItem.objects.filter(is_promotion=True)
    
    # Busca todos os produtos para o cardápio principal, organizados por categoria
    starters = MenuItem.objects.filter(category='starter')
    mains = MenuItem.objects.filter(category='main')
    desserts = MenuItem.objects.filter(category='dessert')
    
    context = {
        'promotion_items': promotion_items,
        'starters': starters,
        'mains': mains,
        'desserts': desserts,
        'nome': 'Wesley'  # Mantendo o contexto original
    }
    
    return render(request, 'menu.html', context)
