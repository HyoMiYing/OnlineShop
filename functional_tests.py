# This is a functional test for the Trgovina App.



from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'Trgovina.settings'


class NewCardTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()

    def test_can_add_a_new_payment_card(self):
        # Bobby visits the website.
        self.browser.get('http://localhost:8000')

        # He sees the navigation bar, which contains three tabs: 'Payment', 'New', and 'History'
        # He is currently on the 'Payment' site.
        self.assertIn('Payments', self.browser.title)

        # Because he has no registered credit cards yet, he switches to 'New' page by clicking the appropriate button in the navbar.
        button_to_page_named_new = self.browser.find_element_by_id('page_new_id')
        button_to_page_named_new.send_keys(Keys.ENTER)

        time.sleep(1)

        # There, he finds a form to register a new credit card. (Name of the cardholder, card number and amount of money that the card has)
        self.assertIn('New', self.browser.title)

        # He enters the next data: 'Bobby Brown', '2345 5324 5323 4322' and '100'.
        name_field = self.browser.find_element_by_id('name_id')
        card_number_field = self.browser.find_element_by_id('card_number_id')
        amount_field = self.browser.find_element_by_id('amount_id')

        name_field.send_keys('Bobby Brown')
        card_number_field.send_keys('2345 5324 5323 4322')
        amount_field.send_keys('100')

        # He presses the button 'Submit' at the end of the form.
        submit_button = self.browser.find_element_by_id('submit_button')
        submit_button.send_keys(Keys.ENTER)

        # The card is successfully registered.

            

# Now he navigates to the 'Payment' page.

# There a page is telling him to choose a credit card.

# He chooses the his card, the 'Bobby Brown' one.

# Then the page invites him to deduct a random amount of money from his card.

# Even though he knows he only has 100 in his bank account, he is a pinhead, so he tells the website to issue his card for '9348.44'.

# The page informs him, that his page has not enough assets for that big of an amount.

# So he tries again with '93.44'.

# The transaction is successfull.

# He the proceeds to make three more transactions: '1.3', '3.7' and '2.3'

# Bobby now estimates that his card balance may be low. So he decides to check the balance of his card.

# The page displays all the transactions up to date. (Balance before and after each of the transaction, amount charged to the card, time and date of the payment, anc current balance)

# Satisfied with his payments, he turns off his computer and goes to eat a big dinner.

if __name__=='__main__':
    unittest.main()