# test
Rok, 5.7.
Pisal bom v angleščini zaradi lažjega izražanja glede programerkih izrazov.

I have finished my first assignment. 

----Revision
I haven't spent much time on the visual aspect of the site, but I nevertheless used bootstrap.

If there is any thing that would need more of my attention any further would be the unittest and functional tests. 

Unittests all pass, but they do not test everything that should be tested.

Functional tests (they are the reason that 'Selenium' is in requirements.txt) do not pass. The problem is not in the web app, but in the tests themselves.
 I need more knowledge to write out tests beforehand writing the main code itself. I still left the file there. I will maybe need it in the assignments #2 and #3.

-------
-------

23.7.
Oddajam drugi del

V zavihku "All Cards" sem dodal AJAX klic.

V zavihku new sem dodal JQuery pop-up.

Komentar po prvem pull requestu je bil tudi, naj dodam kodiranje v forms.py. Če prav razumem, je cilj to, da se prepreči vnos
nenavadnih znakov v obrazec. Glede na to, da se s tem prej še nikoli nisem srečal sem prevzel rešitev iz StackOveflowa rešitev,
da je v HTML <form> dodan accept-charset="UTF-8". Je ta rešitev pravilna, in ali sem sploh prav razumel težavo?

Do konca je spisan tudi functional_tests.py, ki deluje. Navodila za uporabo so napisana v datoteki.