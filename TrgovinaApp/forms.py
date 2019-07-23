# -*- coding: utf-8 -*-

# Django imports
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms
# Project imports
from .models import Card, Transaction

INVALID_CARD_ERROR = 'This name or card number had already been used'
EMPTY_FORM_ERROR = 'Please fill the empty fields in the form'

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
                'unique': INVALID_CARD_ERROR,
                'required': EMPTY_FORM_ERROR,
            },
            'cardholders_name': {
                'unique': INVALID_CARD_ERROR,
                'required': EMPTY_FORM_ERROR,
            },
            'card_balance':  {
                'required': EMPTY_FORM_ERROR,
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
        error_messages = {
            'card': {
                'required': EMPTY_FORM_ERROR,
                },
            'withdraw_amount': {
                'required': EMPTY_FORM_ERROR,
            }
        }