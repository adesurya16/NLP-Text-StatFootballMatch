import nltk, spacy

def dump(obj, nested_level=0):
	spacing = '   '
	if type(obj) == dict:
		print('%s{' % ((nested_level) * spacing))
		for k, v in obj.items():
			if (hasattr(v, '__iter__') and not(isinstance(v, str))):
				print('%s%s:' % ((nested_level + 1) * spacing, k))
				dump(v, nested_level + 1)
			else:
				print('%s%s: %s' % ((nested_level + 1) * spacing, k, v))
		print('%s}' % (nested_level * spacing))
	elif type(obj) == list:
		print('%s[' % ((nested_level) * spacing))
		for v in obj:
			if hasattr(v, '__iter__'):
				dump(v, nested_level + 1)
			else:
				print('%s%s' % ((nested_level + 1) * spacing, v))
		print('%s]' % ((nested_level) * spacing))
	else:
		print('%s%s' % (nested_level * spacing, obj))


def ie_preprocess(document):
	sentences = nltk.sent_tokenize(document)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]
	return sentences

def extract_team(team_name):
	ret = []
	file_name = "teams/" + team_name + ".team"
	file = open(file_name, "r")
	fl = file.readlines()
	for l in fl:
		ret.append(l.rstrip())
	return ret

def extract_match(match_file):
	ret = []
	file_name = "matches/" + match_file + ".match"
	file = open(file_name, "r")
	fl = file.readlines()
	for l in fl:
		ret.append(l.rstrip())
	return ret

# doc = "GOOOOOAAAALLLL!!! MUSTAFI GIVES ARSENAL THE LEAD! Well, a bit of controversy at the Emirates, as - from the free-kick that never really was - the Germany defender heads home Ozil’s cross."
# doc = "Another chance for Tottenham, who are starting to show their quality now. Kane latches onto a looping cross from the right wing, generating enough power on his header to force Cech into an instinctive save."
# doc = "High and wide from Sanchez who, after latching onto a pinpoint pass from Ozil - tries his luck from the edge of the area."
# doc = "A second substitution from Arsenal. Mesut Ozil, who has been superb today, gets a standing ovation as he goes off, with Alex Iwobi coming on."
# doc = "The Gunners have won their last 10 Premier League games at the Emirates, while Tottenham have won only two of their last 32 away league visits to Arsenal, winning 3-1 at Highbury in May 1993 and 3-2 in November 2010."
# doc = "KICK-OFF! The rain is coming down at the Emirates, making the conditions ideal for a feisty derby, and Eriksen gets proceedings underway!"
# doc = "RED CARD! Huge call by the referee! Willian darts into the Qarabag penalty area and gets the better of Sadygov as he tries to take on Sehic. He then goes down under a challenge from behind by the captain, leaving him with no choice but to point to the spot and show a red card to the hosts' captain."
# doc = "Chelsea quickly win the ball back from the restart and work their way down the right wing on a determined attacking move. Fabregas takes over from Zappacosta and fires a cross over to Pedro, who unleashes a volley from the edge of the penalty area but can only send his strike comfortably wide of the goal."

team_name_1 = input("Input name of home team: ")
team_name_2 = input("Input name of away team: ")
match_file = input("Input match file: ")

team1 = extract_team(team_name_1)
team2 = extract_team(team_name_2)
doc = extract_match(match_file)

print(team1)
print(team2)

doc = match_file

# Using NLTK
# sentences = ie_preprocess(doc)
# print(sentences)

# chunked_sentences = nltk.ne_chunk_sents(sentences, False)
# print(chunked_sentences)

# for sent in chunked_sentences:
# 	print(sent)
# 	iob_tagged = nltk.chunk.tree2conlltags(sent)
# 	print(iob_tagged)
# 	for kata in sent:
# 		print(kata)
# END NLTK

# Using spacy
nlp = spacy.load('en')
doc = nlp(doc)

dump(doc.print_tree())
# print(doc.vector)

print()

# for entity in doc.ents:
# 	print(entity.text, entity.label_)

# print()

for t in doc:
	print(t.text, t.tag_, t.ent_iob_, t.ent_type_)
# END spacy


# [[('GOOOOOAAAALLLL', 'NN'), ('!', '.'), ('!', '.'), ('!', '.')], [('MUSTAFI', 'NNP'), ('GIVES', 'NNP'), ('ARSENAL', 'NNP'), ('THE', 'NNP'), ('LEAD', 'NNP'), ('!', '.')], [('Well', 'RB'), (',', ','), ('a', 'DT'), ('bit', 'NN'), ('of', 'IN'), ('controversy', 'NN'), ('at', 'IN'), ('the', 'DT'), ('Emirates', 'NNP'), (',', ','), ('as', 'IN'), ('-', ':'), ('from', 'IN'), ('the', 'DT'), ('free-kick', 'JJ'), ('that', 'IN'), ('never', 'RB'), ('really', 'RB'), ('was', 'VBD'), ('-', ':'), ('the', 'DT'), ('Germany', 'NNP'), ('defender', 'NN'), ('heads', 'NNS'), ('home', 'VBP'), ('Ozil', 'NNP'), ('’', 'NNP'), ('s', 'NN'), ('cross', 'NN'), ('.', '.')]]
# [[('Another', 'DT'), ('chance', 'NN'), ('for', 'IN'), ('Tottenham', 'NNP'), (',', ','), ('who', 'WP'), ('are', 'VBP'), ('starting', 'VBG'), ('to', 'TO'), ('show', 'VB'), ('their', 'PRP$'), ('quality', 'NN'), ('now', 'RB'), ('.', '.')], [('Kane', 'NNP'), ('latches', 'NNS'), ('onto', 'IN'), ('a', 'DT'), ('looping', 'JJ'), ('cross', 'NN'), ('from', 'IN'), ('the', 'DT'), ('right', 'JJ'), ('wing', 'NN'), (',', ','), ('generating', 'VBG'), ('enough', 'JJ'), ('power', 'NN'), ('on', 'IN'), ('his', 'PRP$'), ('header', 'NN'), ('to', 'TO'), ('force', 'VB'), ('Cech', 'NNP'), ('into', 'IN'), ('an', 'DT'), ('instinctive', 'JJ'), ('save', 'NN'), ('.', '.')]]