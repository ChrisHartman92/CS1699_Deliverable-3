Feature: Error Handling
As a user
I want to be able to run the program with files missing 
So that I can be told what is causing the error 

@invalidnumber
Scenario: Invalid number of questions
	Given a sentence file has been generated from file pers_text.txt
	And the user submits the number of questions as -1 
	When the user runs ask.py
	Then 1 error question about number will be returned

@invalidsentences
Scenario: File without sentences
	Given an invalid sentence file
	When the user runs ask.py
	Then 1 error question about sentences will be returned

#8 is the max amount of pre-generated questions
