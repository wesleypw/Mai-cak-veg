from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('starter', 'Entradas'),
        ('main', 'Pratos Principais'),
        ('dessert', 'Sobremesas'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=255, blank=True)  # Caminho para imagem do produto
    is_promotion = models.BooleanField(default=False)  # Indica se está em promoção
    promotional_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # Preço promocional
    discount_percentage = models.IntegerField(null=True, blank=True)  # Percentual de desconto

    def __str__(self):
        return self.name