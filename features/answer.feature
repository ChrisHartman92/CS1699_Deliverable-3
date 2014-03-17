Feature: Answer Questions
As a user
I want to be able to run the program in answer mode
So that I can get the answers to the questions generated

@noask
Scenario: No answers requested
	Given the user enters an article with category person
	And does not specify the argument -a
	And a sentence file has been generated from pers_text.txt
	And the article is about Randy Pausch 
	When the user runs ask.py
	Then questions from the category person will be returned
	And there will be 0 answers returned

@ask
Scenario: Answers are requested
	Given the user enters an article with category person
	And specifies the argument -a
	And a sentence file has been generated from pers_text.txt
	And the article is about Randy Pausch 
	When the user runs ask.py
	Then questions from the category person will be returned
	And the answers to those questions will be returned