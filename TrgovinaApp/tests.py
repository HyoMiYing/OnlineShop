from django.test import TestCase
from django.http import HttpRequest
from django.utils.html import escape

from TrgovinaApp.models import Card, Transaction
from TrgovinaApp.views import all_cards

from TrgovinaApp.forms import (
    INVALID_CARD_ERROR, EMPTY_FORM_ERROR,
    TransactionForm, CardInputForm,
)


class WebsitePagesTest(TestCase):

    def test_payments_page_uses_base_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base.html')

    def test_new_page_uses_new_template(self):
        response = self.client.get('/new/')
        self.assertTemplateUsed(response, 'new.html')

    def test_history_page_uses_history_template(self):
        response = self.client.get('/history/')
        self.assertTemplateUsed(response, 'history.html')

    def test_all_cards_page_uses_all_cards_template(self):
        response = self.client.get('/all_cards/')
        self.assertTemplateUsed(response, 'all_cards.html')
        
class PaymentCardModelTest(TestCase):

    def test_saving_and_retrieving_payment_card_information(self):
        first_card = Card()
        first_card.cardholders_name = "First Firstman"
        first_card.card_number = "1111222233334444" 
        first_card.card_balance = "100"
        first_card.save()

        second_card = Card()
        second_card.cardholders_name = "Second Secondman"
        second_card.card_number = "4444555522221111" 
        second_card.card_balance = "56"
        second_card.save()

        saved_cards = Card.objects.all()
        self.assertEqual(saved_cards.count(), 2)


        first_saved_card = saved_cards[0]
        second_saved_card = saved_cards[1]
        self.assertEqual(first_saved_card.cardholders_name, 'First Firstman')
        self.assertEqual(second_saved_card.cardholders_name, 'Second Secondman')

class FormsTest(TestCase):

    def test_payments_page_uses_transaction_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], TransactionForm)

    def test_new_page_uses_card_input_form(self):
        response = self.client.get('/new/')
        self.assertIsInstance(response.context['form'], CardInputForm)

class TransactionFormTest(TestCase):

    def test_form_validation_for_blank_card_input(self):
        form = TransactionForm(data={'card': '', 'withdraw_amount': '2.4'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['card'], [EMPTY_FORM_ERROR])

    def test_form_validation_for_blank_withdraw_input(self):
        first_card = Card()
        first_card.cardholders_name = "First Firstman"
        first_card.card_number = "1111222233334444" 
        first_card.card_balance = "100"
        first_card.save()

        form = TransactionForm(data={'card': 'First Firstman', 'withdraw_amount': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['withdraw_amount'], [EMPTY_FORM_ERROR])

        first_card.delete()


class NewCardFormTest(TestCase):

    def test_can_add_a_new_card(self):
        self.client.post('/new/', data={'cardholders_name': 'Loyd', 'card_number': '123213123123', 'card_balance': '3222.10'})

        self.assertEqual(Card.objects.count(), 1)
        new_card = Card.objects.first()
        self.assertEqual(new_card.cardholders_name, 'Loyd')

    def test_for_invalid_input_with_no_name_doesnt_save_but_shows_errors(self):
        response = self.client.post('/new/', data={'cardholders_name': '', 'card_number': '12222233', 'card_balance': '3222.10'})

        self.assertEqual(Card.objects.count(), 0)
        self.assertContains(response, escape(EMPTY_FORM_ERROR))

    def test_for_invalid_input_with_no_card_number_doesnt_save_but_shows_errors(self):
        response = self.client.post('/new/', data={'cardholders_name': 'Loyd', 'card_number': '', 'card_balance': '3222.10'})

        self.assertEqual(Card.objects.count(), 0)
        self.assertContains(response, escape(EMPTY_FORM_ERROR))

    def test_for_invalid_input_with_no_card_balance_doesnt_save_but_shows_errors(self):
        response = self.client.post('/new/', data={'cardholders_name': 'Loyd', 'card_number': '12222233', 'card_balance': ''})

        self.assertEqual(Card.objects.count(), 0)
        self.assertContains(response, escape(EMPTY_FORM_ERROR))

    def test_duplicate_cardholder_names_invalid(self):
        response1 = self.client.post('/new/', data={'cardholders_name': 'Loyd', 'card_number': '111222333', 'card_balance': '12'})
        response2 = self.client.post('/new/', data={'cardholders_name': 'Loyd', 'card_number': '888888888', 'card_balance': '22'})

        self.assertEqual(Card.objects.count(), 1)
        self.assertContains(response2, escape(INVALID_CARD_ERROR))

    def test_duplicate_card_numbers_invalid(self):
        response1 = self.client.post('/new/', data={'cardholders_name': 'Benny', 'card_number': '888888888', 'card_balance': '12'})
        response2 = self.client.post('/new/', data={'cardholders_name': 'Loyd', 'card_number': '888888888', 'card_balance': '22'})

        self.assertEqual(Card.objects.count(), 1)
        self.assertContains(response2, escape(INVALID_CARD_ERROR))



# class ItemModelTest(TestCase):


#     def test_item_is_related_to_list(self):
#         list_ = List.objects.create()
#         item = Item()
#         item.list = list_
#         item.save()
#         self.assertIn(item, list_.item_set.all())


#     def test_cannot_save_empty_list_items(self):
#         list_ = List.objects.create()
#         item = Item(list=list_, text='')
#         with self.assertRaises(ValidationError):
#             item.save()
#             item.full_clean()


#     def test_duplicate_items_are_invalid(self):
#         list_ = List.objects.create()
#         Item.objects.create(list=list_, text='bla')
#         with self.assertRaises(ValidationError):
#             item = Item(list=list_, text='bla')
#             item.full_clean()


#     def test_CAN_save_same_item_to_different_lists(self):
#         list1 = List.objects.create()
#         list2 = List.objects.create()
#         Item.objects.create(list=list1, text='bla')
#         item = Item(list=list2, text='bla')
#         item.full_clean()  # should not raise


#     def test_list_ordering(self):
#         list1 = List.objects.create()
#         item1 = Item.objects.create(list=list1, text='i1')
#         item2 = Item.objects.create(list=list1, text='item 2')
#         item3 = Item.objects.create(list=list1, text='3')
#         self.assertEqual(
#             list(Item.objects.all()),
#             [item1, item2, item3]
#         )


#     def test_string_representation(self):
#         item = Item(text='some text')
#         self.assertEqual(str(item), 'some text')
