from django.test import TestCase

from TrgovinaApp.models import Card, Transaction


class WebsitePagesTest(TestCase):

    def test_payments_page_uses_base_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base.html')

    def test_new_page_uses_new_template(self):
        response = self.client.get('/new/')
        self.assertTemplateUsed(response, 'new.html')

    def test_new_page_uses_new_template(self):
        response = self.client.get('/history/')
        self.assertTemplateUsed(response, 'history.html')

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


class NewCardTest(TestCase):

    def test_can_save_a_POST_request(self):
        self.client.post('/new/', data={'cardholders_name': 'giggity', 'card_number': '123213123123', 'card_balance': '3222.10'})

        self.assertEqual(Card.objects.count(), 1)
        new_card = Card.objects.first()
        self.assertEqual(new_card.cardholders_name, 'giggity')