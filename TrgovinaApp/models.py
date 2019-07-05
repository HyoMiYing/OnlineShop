# encoding= utf-8
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Transaction(models.Model):
    card = models.ForeignKey('Card')
    withdraw_amount = models.FloatField()

class Card(models.Model):
    cardholders_name = models.CharField(max_length=30)
    card_number = models.BigIntegerField(validators=[MaxValueValidator(9999999999999999), MinValueValidator(0)])
    card_balance = models.FloatField()

    def __str__(self):
        return self.cardholders_name