import os
import urllib
import itertools

def alphabetize(word):
	word = list(itertools.chain(word))
	word.sort()
	return ''.join(word)

# Let's use SIL's wordlist
if not 'vocab.txt' in os.listdir('.'):
	urllib.urlretrieve('http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt', 'wordsEn.txt')
	infile = open('wordsEn.txt','r')
	outfile = open('vocab.txt','w')
	for line in infile.readlines():
		outfile.write(alphabetize(line.rstrip()) + '\t' + line.rstrip() + '\n')
	infile.close()
	outfile.close()

prompt = 'Type in a scrambled word >'

scrambled = raw_input(prompt).lower()

while scrambled != '' and scrambled != 'quit' and scrambled != 'exit':
	scrambled = alphabetize(scrambled)
	for candidate in open('vocab.txt','r').readlines():
		candidate = candidate.rstrip().split('\t')
		if scrambled == candidate[0]:
			print candidate[1]
	scrambled = raw_input(prompt).lower()

