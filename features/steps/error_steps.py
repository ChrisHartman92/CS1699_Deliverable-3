from behave import given, when, then , step
import askfunc
import string

sentences = []
@given('an invalid sentence file')
def set_no_sents(context):
	global sentences
	sentences = []
	pass

@then('1 error question about {text} will be returned')
def set_end(context, text):
	holdarr = []
	if (text=="number"):
		holdarr = askfunc.printQuests(int(-1), [])
		assert holdarr[0] == "Invalid number of questions entered"
	elif (text=="sentences"):
		holdarr = askfunc.getClassification("", sentences)
		assert holdarr[0] == "There were no sentences found"

