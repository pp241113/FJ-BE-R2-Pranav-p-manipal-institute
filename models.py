from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.amount} - {self.description}"

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.amount} - {self.description} ({self.category})"

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    # Removed month, year, and category since they are not part of the model now
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Budget: {self.name} (Limit: {self.limit}, Amount: {self.amount})"
