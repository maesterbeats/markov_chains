__author__ = 'andrewstern'


from markov import make_transition_matrix


data = ['A', 'B', 'D', 'B', 'D', 'E', 'F', 'D', 'G', 'A', 'E','A', 'B', 'B', 'D', 'F', 'D', 'G', 'A', 'D', 'E', 'G']

x = make_transition_matrix(data,3)


print(x)