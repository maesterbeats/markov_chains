__author__ = 'andrewstern'

import re
import itertools
import collections
from markov_generators import markov



def make_transition_matrix(phrase,order):

	if type(phrase) == str:
		notes = re.findall('[A-Z]+', phrase.upper())
	elif type(phrase) == list:
		notes = phrase
	else:
		raise ValueError("phrase must be either string or list")

	series = markov(notes,order)
	t_matrix = collections.Counter()
	for pattr in series:
		t_matrix[pattr] += 1
	return t_matrix






data = ['A', 'B', 'D', 'B', 'D', 'E', 'F', 'D', 'G', 'A', 'E','A', 'B', 'B', 'D', 'F', 'D', 'G', 'A', 'D', 'E', 'G']

x = make_transition_matrix(data,3)


print(x)




