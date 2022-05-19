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
The plan for this program is to have three classes, the player, puzzle and terminal_service classes, to be called upon by the director class which will call upon by the main file to run the program. 

<p>&nbsp;</p>
The first class is the director class. This class will call upon other classes to retrieve information from its parent classes. 

Director
---------------------------

| - word
| - displayPlayer
| - guess
| - lives
----------------------------
| + start_game()
| + get_inputs()
| + do_outputs()
----------------------------

<p>&nbsp;</p>
The second class is the player class. This class will send player visuals to its child class to display the jumper character.

Player
---------------------------

| - NEED
----------------------------
| + NEED()
----------------------------

<p>&nbsp;</p>
The third class is the puzzle class. This class will choose a word from a list utilizing the random library and send the word information the child class to display and perform needed actions upon.

Puzzle
---------------------------

| - words
| - value
| - pickedWord
----------------------------
| + list_of_words()
| + get_value()
| + get_words()
----------------------------

<p>&nbsp;</p>
The fourth class is the terminal_service class. This class will provide input and output operations to the child class.

Terminal_Service
---------------------------

| - NEED
----------------------------
| + NEED()
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
- Create the Puzzle Private Class
  - Contains the Functions:
    - List of the words: (list_of_words)
    - Get Value: (get_value)
    - Get list of Words: (get_words)

* Contributed three to four words to puzzle class word list.

Manuel Cipriano
* Contributed three to four words to puzzle class word list.

Chinemerem Ukeje (Cole)
- Create the Terminal Service Class
* Contributed three to four words to puzzle class word list.
---
*Shane Cook is the author of this document*