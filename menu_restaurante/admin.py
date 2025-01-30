from django.shortcuts import render
from .models import MenuItem

def menu_view(request):
    starters = MenuItem.objects.filter(category='starter')
    mains = MenuItem.objects.filter(category='main')
    desserts = MenuItem.objects.filter(category='dessert')
    context = {
        'starters': starters,
        'mains': mains,
        'desserts': desserts,
    }
    return render(request, 'menu/menu.html', context)
