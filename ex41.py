import random
from urllib import request
import sys
Word_url = "http://learncodethehardway.org/words.txt"
Words = []
Phrases = {
	"class %%%(%%%):":
	"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)" :
	"class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
	"class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
	"Set *** to an instance of class %%%.",
	"***.***(@@@)":
	"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
	"From *** get the *** attribute and set it to '***'."
}
#do they want to drill phrases first
if len(sys.argv) ==2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False
for word in request.urlopen(Word_url).readlines():
	#print(word.strip())
	Words.append(word.strip())
def convert(snippet, phrase):
	class_names = [w.capitalize() for w in random.sample(Words, snippet.count("%%%"))]
	print("class_names:",class_names)
	other_names = random.sample(Words, snippet.count("***"))
	print("other_names:", class_names)
	results = []
	param_names = []
	for i in range(0,snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join("%s" %id for id in random.sample(Words, param_count)))
		print("param_names:", param_names)
	for sentence in snippet, phrase:
		result = sentence[:]
		for word in class_names:
			#print("class_name:", word)
			result = result.replace("%%%", "%s"%word, 1)
		for word in other_names:
			#print("other_name:", word)
			result = result.replace("***", "%s"%word, 1)
		for word in param_names:
			#print("param_name:", word)
			result = result.replace("@@@", "%s"%word, 1)
		results.append(result)
	return results

try:
	while True:
		snippets =list(Phrases.keys())
		random.shuffle(snippets)
		for snippet in snippets:
			phrase = Phrases[snippet]
			question, answer = convert(snippet, phrase)
			print("question1:", question)
			if PHRASE_FIRST:
				question, answer = answer, question
			print("question2:", question)
			input(">>")
			print("ANSWER:%s\n\n" % answer )
except EOFError:
	print("\n Bye")
		