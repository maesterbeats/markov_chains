__author__ = 'andrewstern'


class MarkovGenOrder1:

	def __init__(self, sequence):
		self.sequence = sequence

	def __iter__(self):
		self.a = 0
		self.b = 1
		return self

	def __next__(self):
		if self.b > len(self.sequence) - 1:
			raise StopIteration
		note1 = self.sequence[self.a]
		note2 = self.sequence[self.b]
		pair = (note1,note2)
		self.a, self.b = self.b, self.b + 1
		return pair


class MarkovGenOrder2:

	def __init__(self, sequence):
		self.sequence = sequence

	def __iter__(self):
		self.a = 0
		self.b = 1
		self.c = 2
		return self

	def __next__(self):
		if self.c > len(self.sequence) - 1:
			raise StopIteration
		note1 = self.sequence[self.a]
		note2 = self.sequence[self.b]
		note3 = self.sequence[self.c]
		tripple = ((note1,note2),note3)
		self.a, self.b, self.c = self.b, self.c, self.c + 1
		return tripple

class MarkovGenOrder3:

	def __init__(self, sequence):
		self.sequence = sequence

	def __iter__(self):
		self.a = 0
		self.b = 1
		self.c = 2
		self.d = 3
		return self

	def __next__(self):
		if self.d > len(self.sequence) - 1:
			raise StopIteration
		note1 = self.sequence[self.a]
		note2 = self.sequence[self.b]
		note3 = self.sequence[self.c]
		note4 = self.sequence[self.d]
		quad = ((note1,note2,note3),note4)
		self.a, self.b, self.c, self.d = self.b, self.c, self.d, self.d  + 1
		return quad



markov_orders = {
	1 : MarkovGenOrder1,
	2 : MarkovGenOrder2,
	3 : MarkovGenOrder3
}

def markov(sequence,order):
	return markov_orders.get(order)(sequence)