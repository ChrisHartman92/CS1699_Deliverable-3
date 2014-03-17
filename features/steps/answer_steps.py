from behave import given, when, then , step
import askfunc
import string

@given('does not specify the argument -a')
def set_noarg(context):
	pass

@given('specifies the argument {arg}')
def set_arg(context, arg):
	if (arg == "-a"):
		askfunc.answers = True

@then('there will be {d} answers returned')
def set_end(context, d):
	ansarr = []
	ansarr = askfunc.answerQuests(int(d))
	assert len(ansarr) == int(d)

@then('the answers to those questions will be returned')
def set_end(context):
	sentences = []
	holder = []
	questarr = []
	ansarr = []
	sentences = open("pers_text.txt.sentences").read().split('\n')
	holder = askfunc.getClassification("pers_text.txt", sentences)
	questarr = askfunc.printQuests(5, holder)
	ansarr = askfunc.answerQuests(len(questarr))
	assert (len(ansarr) == len(questarr))
