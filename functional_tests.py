
# IMPORTANT: RUN A DJANGO DEVELOPMENT SERVER IN ANOTHER TERMINAL BEFORE RUNNING THIS SCRIPT.
# Failure to do so, will result in address http://localhost:8000 lead to 404 error.
# IMPORTANT#2: PLEASE IGNORE THE 'django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.' ERROR IN THE TERMINAL OUTPUT. THE ERROR DOES NOT IMPAIR THE FUNCTIONALITY OF THIS SCRIPT.
# This script interacts with an older version of Django. I have not found a solution that wouldn't require changes in other files than this one. So I decided to let the errpr remain, because it can be ignored.

# This is a functional test for the Trgovina App.
# It is used in development, as a guidance (when writing a project, this file is written first. Then the actual code is added to meet the requirements of this python script), and as a testing tool.

# This file is also very usable to present the functionalities of the application to other people.
# Functionalities are presented by following a story of a real user.

# From now on, the comments will be used as a story text.

# Bobby Brown, is a hobby programmer.
# During the day he works in the shoe factory, but dedicates his evening to programming.
# This time, he decides to play with an app that he made some time ago.

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

        def add_new_card(Name, CardNumber, CardAmount):
            name_input = self.browser.find_element_by_id('name-input')
            name_input.send_keys(Name)

            card_number_input = self.browser.find_element_by_id('card-number-input')
            card_number_input.send_keys(CardNumber)

            amount_input = self.browser.find_element_by_id('amount-input')
            amount_input.send_keys(CardAmount)

            submit_button_for_new_card = self.browser.find_element_by_id('pop_up')
            submit_button_for_new_card.click()

        def bobbys_transaction(amount):
            choose_card_box = self.browser.find_element_by_id('choose-card-input')
            choose_card_box.click()

            for option in choose_card_box.find_elements_by_tag_name('option'):
                if option.text == 'Bobby Brown':
                    option.click()
                    break

            amount_inputbox = self.browser.find_element_by_id('withdraw-amount-input')
            amount_inputbox.send_keys(f'{amount}')

            submit_button = self.browser.find_element_by_id('submit-button')
            submit_button.click()

        def change_pages_via_tab(tab_name):
            new_tab = self.browser.find_element_by_link_text(f'{tab_name}')
            new_tab.click()


        # Bobby spins up the development server and visits the homepage of his app

        self.browser.get('http://localhost:8000')
        time.sleep(1)

        # He finds himself in the payments tab.

        payments_tab = self.browser.find_element_by_tag_name('a').text
        self.assertIn('Payments', payments_tab)

        # He says to himself "Sure, I want to pay, but with what??"
        # "Well, let's give it a try," Bobby says.

        amount_inputbox = self.browser.find_element_by_id('withdraw-amount-input')
        amount_inputbox.send_keys('1.3')
        time.sleep(1)

        choose_card_box = self.browser.find_element_by_id('choose-card-input')
        choose_card_box.click()
        card_options = self.browser.find_elements_by_tag_name('option')

        if any(card_option.text == 'Bobby Brown' for card_option in card_options):
            # Bobby did find his card in the dropdown list.
            # To run this test successfully you must run it with empty database.
            self.fail('This database has already been used')
        else:
            # Bobby did not find his card listed in the dropdown list.
            pass


        submit_button = self.browser.find_element_by_id('submit-button')
        submit_button.click()

        # Because he submitted the form without supplying all the needen information (card), the form is rejected, and Bobby sees an error message.

        form_error_message = self.browser.find_element_by_id('form-error-message').text
        self.assertIn('Please fill', form_error_message)

        # He switches to the New tab, to add a card.

        change_pages_via_tab('New')
        time.sleep(1)

        # He sees a form.

        new_card_form = self.browser.find_element_by_id('new_card_form')

        # Bobby goes to the toilet. Meanwhile he thinks of what card is he going to create.
        # He adds a cool card that he thought of.

        add_new_card('Bobby Brown', '23329494944', '3.145')
        time.sleep(1)

        # After submitting, the page delights him with the pop-up that reads: "New card added."

        pop_up_message = self.browser.switch_to.alert
        pop_up_message_text = pop_up_message.text

        # He closes the pop-up.
        
        self.assertIn('New card added', pop_up_message_text)

        accept_pop_up_message = pop_up_message.accept()
        time.sleep(1)

        # With his card in place, he goes back to the payments tab to spend some euros.
        change_pages_via_tab('Payments')
        time.sleep(1)

        # Now knowing that he has a card in place, he makes a payment of 2€-

        bobbys_transaction(2)
        time.sleep(1)

        # Bobby feels great satisfaction from making a payment of 2€. So he makes one more of 1.1€.

        bobbys_transaction(1.1)
        time.sleep(1)

        # That was so thrilling!
        # Bobby looked around his room, to check if anyone was looking at him.
        # Then he proceeded to make an astounding payment of 10€.
        
        bobbys_transaction(10)
        time.sleep(1)

        # Bobby has become overwhelmed with the thrill of spending money. He then axed himself with confusion "Wait, did I make three or four payments?".
        # He switched to History tab, where he ran over his spendings.

        change_pages_via_tab('History')
        time.sleep(1)

        transaction_history_table = self.browser.find_element_by_id('transaction_history_table')

        # The card has definetly got negative balance. He quickly goes to 'All cards' tab.
        
        change_pages_via_tab('All cards')
        time.sleep(1)

        # Finds his card in the table:

        bobby_s_card = self.browser.find_element_by_class_name('Bobby')

        # Bobby Brown:"Yes, the balance on his card is -9.955€."

        self.assertIn('-9.955', bobby_s_card.text)

        # This is not good.
        # Now he's going to have to pay for the interest.
        # He is not the kind of person that has a negative balance on his bank account!
        # This is outrageous!
        # Bobby's little nervous eyes notice a 'Delete' button.
        
        delete_button_for_bobbys_card = bobby_s_card.find_element_by_id('delete-button')

        # What if he could just make the debt... go away?
        # That can't be... so easy?

        delete_button_for_bobbys_card.click()
        time.sleep(2)

        # His card immediatly dissapears from the all cards list.
        # He senses relief and says to himself 'Another bullet dodged'.

        # He thinks about how genious a programmer he is to come up with that kind of simple, but effective solution.
        # Satisfied with all his accomplishments, he goes to sleep.


if __name__=='__main__':
    unittest.main(warnings='ignore')
