# Django imports
from django.shortcuts import render
# 'reverse' import repaired by Rok
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .forms import CardInputForm, TransactionForm
from .models import Card, Transaction


def payment(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():

            card = form.cleaned_data['card']
            appropriate_card_in_the_database = Card.objects.get(cardholders_name=f"{card}")
            withdraw_amount = form.cleaned_data['withdraw_amount']

            new_transaction_instance = Transaction(card=card, withdraw_amount=withdraw_amount)
            new_transaction_instance.save()

            appropriate_card_in_the_database.card_balance -= withdraw_amount
            appropriate_card_in_the_database.save()

            return HttpResponseRedirect('/')

    else:
        form = TransactionForm()

    return render(request, 'base.html', {'form':form})

def new(request):
    if request.method == 'POST':
        form = CardInputForm(request.POST)
        if form.is_valid():

            cardholders_name = form.cleaned_data['cardholders_name']
            card_number = form.cleaned_data['card_number']
            card_balance = form.cleaned_data['card_balance']

            new_card_instance = Card(cardholders_name=cardholders_name, card_number=card_number, card_balance=card_balance)
            new_card_instance.save()

            return HttpResponseRedirect('/')

    else:
        form = CardInputForm()

    return render(request, 'new.html', {'form':form})

def history(request):
    data = Transaction.objects.all()
    return render(request, 'history.html', {'data':data})
