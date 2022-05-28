# Jumper Game Design Documentation
---
[Please refer to the README.md file for game design specification](README.md)

---
## Principals used in the program
* Encapsulation
  * Created various private classes to be used inside the director class which is used inside of the main.py file. This allows for access control and restriction to parent classes on child class.
* Version Control System (VCS)
  * Each team member used git to stage and commit changes to the program while similtaneously pulling changes to keep the program
  * Github was used to house the public repository(see "Read Me" link above for design specifications)
---
## The Plan
The plan for this program is to have three classes, the word, check and displayPlayer classes, to be called upon by the director class which will call upon by the main file to run the program.

<p>&nbsp;</p>
The first class is the <strong>director</strong> class. This class will call upon other classes to retrieve information from its parent classes and direct the flow of the program. 

Director
---------------------------

| - play
| - lives
| - displayPlayer
| - check
| - word
| - guess
| - guesses
| - playAgain
----------------------------
| + start_game()
| + play()
| + play_again()
----------------------------

<p>&nbsp;</p>
The second class is the <strong>word</strong> class. This class will choose a word from a list utilizing the random library and send the word string to the child class to display and perform needed actions upon.

Word
---------------------------
| - library
----------------------------
| + pickWord()
----------------------------

<p>&nbsp;</p>
The third class is the <strong>check</strong> class. This class will determine if a player guess is correct or not.

Check
---------------------------

| - check
----------------------------
| + checkGuess()
----------------------------

<p>&nbsp;</p>
The fourth class is the <strong>displayPlayer</strong> class. This class will store and append the jumper visuals list.

displayPlayer
---------------------------

| - jumperDisplay
----------------------------
| + displayJumper()
----------------------------

---

## Team Responsibilities

Shane Cook
* Contributed three to four words to puzzle class word list.(Flamingo, Boutique, Taco, Salad)
* DESIGNDOC.md documentation
* README.md documentation
* initializer method in the Director() class
* start_game method in the Director() class

Antonio Saucedo
* DESIGNDOC.md "Plan" & "Principles" section
* get_inputs method for the director class.
* do_outputs method for the director class.
* Contributed three to four words to puzzle class word list.(Parachute, Escalator, Hurricane, Freezing.)

Godwin Iyip
* Create the Word Private Class
* Contributed three to four words to puzzle class word list.

Manuel Cipriano
* Designing and creating the displayPlayer class.
* Contributed with four words for the list of words to be guessed.(Courage, Continue, Counts, Churchill.)

Chinemerem Ukeje (Cole)
* Create the Check Class
* Contributed three to four words to puzzle class word list.

---
*Shane Cook is the author of this document*