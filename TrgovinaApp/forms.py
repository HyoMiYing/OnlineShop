# Django imports
from django.utils.translation import ugettext_lazy as _
from django import forms
# Project imports
from .models import Card, Transaction

class CardInputForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('cardholders_name', 'card_number', 'card_balance',)
        labels = {
            'cardholders_name': _('Full name:'),
            'card_number': _('Card number:'),
            'card_balance': _('Amount of currency (in €):'),
        }
        error_messages = {
            'card_number': {
                'unique': _("This card is already registered."),
            },
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('card', 'withdraw_amount',)
        labels = {
            'card': _('Choose your name:'),
            'withdraw_amount': _('Withdraw amount (in €):'),
        }
