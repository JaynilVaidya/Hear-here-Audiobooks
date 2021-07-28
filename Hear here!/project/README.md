Hear here!

!!THE PHOTOS OF THE RUNNING PROJECT IS PLACED IN THE 'running_project.pdf' IN THE ZIP FILE.PLEASE REFER TO THAT!!	

What is Hear here?
It is an app for audiobooks.
Having trouble sleeping? Cant find time to read your kids bedtime stories? Like stories but think reading is too lame for you? Wanna read books but are too busy and dont have time to stay static for an extended period of time? Wanna Hear books?
5 PROBLEMS ONE SOLUTION : Hear here!

Now that you know 'what it is' lets walk you through 'how it is what it is':-

DESCRIPTION:-

The base of this project is  text to speech conversion. We have a nice collection of mini-stories (ALL IN TEXT FORMAT!!) and we use the pyttsx3 library to convert those text files to audiofiles and make it available to the users.

We have used tkinter to create our ravishing user interface to present the users with the best possible service.

PREREQUISITES:-
Before you can run the project, you will have to install a few things:-
open command prompt (Win key + r ,enter cmd,ENTER  or https://www.ionos.com/digitalguide/server/tools/open-command-prompt/)
1.pyttsx3
	-pip install pyttsx3

2.tkinter
	-pip install tk

3.pillow
	-pip install pillow

4.numpy
	-pip install numpy

**ALL THE INSTALLATION AND WORKING INSTRUCTIONS IN THIS FILE ARE MEANT FOR WINDOWS USERS


HOW TO RUN THE THING:-
1.In order to run this, the file to look for is 'loginpage.py'.
	-You could double click on the file to make it run.(Less preferable)
	-You could use the windows command prompt to run the file (No command line args are required)(Most preferable)
	 Steps:-
		1.open command prompt (Win key + r ,enter cmd,ENTER  or https://www.ionos.com/digitalguide/server/tools/open-command-prompt/)
		2.navigate to the file where the zip file of the project is extracted
		3.Enter:' python loginpage.py 'in the command proompt
	(All these steps are mentioned under the assumption that your device has python installed and added to PATH, if not refer this link to do so:- 	https://docs.python.org/3/using/windows.html)

2.When the login page runs it will ask for a username and password, if you are a new user click on 'Sign Up'.

3.At the signup page, enter the details and hit 'Submit' at the bottom right. If the entered details are valid the page will close, if not, a message will be displayed   at the bottom right of your page.

4.Assuming that the signup was succesfull i.e. the signup window closed, now u ll find yourself in front of the loginpage again, here, enter the credentials you   created your account with at the signup page. If the credentials match-up you will be logged in.

5.Upon successfull login you will find yourself on the homepage of our main window,this window has a topnav consisiting of 3 pages: home,search and profile   (information about each page are provided further below(in this README file) in the features and working section)

6.Click on any of the books (in home or search page) and it will take you to a personalised 'play' page where you will find information about the book and 2 clickable    play buttons.On clicking the pink or black play button an mp3 player will open up playing your audiobook in female or male voice respectively.

Now that you know the how to run it, lets get into the nitty gritties:-

FEATURES AND WORKING:-

The Tkinter library is used to create the GUI.

Login page:-
The login page requires you to enter a username and password to log in, which uses the tkinter labels, buttons, message and entry tags in its integration.
It will display a self destroying message on the top incase you enter incorrect credentials.

Signup page:-
The signup page requires the new user a number of details to sign them in which are stored in the creds.txt text file. Even here a self destroying message will be displayed on the bottom-right of the screen in case you enter invalid or unexpected data (Even if you do not enter any data, i mean common, those fields are mandatory).

Now the home page, it consist of a top navigation bar which provides you the ability to navigate through 3 different pages: home,search and profile.

Fasten your seatbelt because here comes the good part: when you switch between these 3 pages the window doesnt destroy and create another one for the other page. IT JUST SWITCHES!! well this was done with the object oriented programming part of python where we destroyed only a certain number of not-required child frames and passed the other frames as parameters and used them as a base file and hence, there was no need to destroy the whole page( In lamen terms,using a notebook page as a metaphor we are using the same page and heading but everytime you switch a page we erase the contents of that page and rewrite the appropriate content).

Home AND Search Page:-
The home page offers you the top 5 books that we picked for you (PS: They are just 5 randomly chosen books)(numpy randomchoice is used to directly pick random lines from the txt file).And the search page offers you the whole collection of books.
These pages have the top navigation bar and installation of the scrollbar as two of the top features.
The clickable buttons direct you to the personalised play page (which is the part of the play.py file).

The top navigation bar isn a static navbar which sticks to the top of the screen switching colors depicting your current page.

Now onto the scroll bar, tkinter does not really give an option to scroll through a whole frame so inorder to do that i have installed a canvas onto which the scrollbar and a few other child frames are placed to scroll through them.  

Profile Page:-
The profile page offers the user with their information and gives them an option to change a few information if they wish to do so.The information is updated (if valid) on clicking the submit button. And yes, we provide the self destroying messages here as well for any invalid information entered.

Play page:-
This page offers the personalized description of the book button clicked upon.It has two play buttons,pink and black on the right side of the page for female and male voices respectively. When clicked upon any of these play buttons, the pyttsx.py file is called which reads the text from the text file of the book (stories/). This page also have a personalised background image for each book(stories/images/), and details about the book(stories/description.txt) and a short summary for the user to get a headsup on whats to come(stories/summaries/).

pyttsx.py:-
The code in this file is what runs the show. Here, we use the pyttsx3 library of python to convert our text to speech. This code reads the text from the appropriate file and converts it into an audio file which is saved as audio.mp3 file which on completion of task is deleted (The mp3 file is deleted to preserve the text-to-speech feature of this project). 

ERRORS YOU MIGHT ENCOUNTER:-
1.The audio file might not play when clicked upon:-
Possible reasons:-
	-Your device might not support mp3 files.
	-Your device might not have vlc media player or windows media player as the default media player.
	-Your device media player might not allow external applications to run it.
2.Uneven placement of widgets (buttons,labels etc)
Possible reasons:-
	-Your device screensize being abnormally small
	-You might not have downloaded all the required libraries

 