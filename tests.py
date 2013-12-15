__author__ = 'andrewstern'


from markov import make_transition_matrix
import midi_utils as Midi
import os

def find_files(folder = None, extension = None):

	'''
	Find all of a given extension in a directory
	@param folder:
	@param extension:
	@return: list of files
	'''
	if folder:
		os.chdir(folder)
	else:
		folder = ''
	if extension:
		pass
	else:
		extension = ''

	cur_dir = os.getcwd()
	search_pattern = '{0}/*{1}'.format(cur_dir,extension)

	
	for file in glob.glob(search_pattern):
		yield file


def choose_folder():
	input_var = input("Choose a directory[path]: ")
	if len(input_var) > 0:
		os.chdir(input_var)
		print ("you entered " + input_var)
	else:
		raise ValueError("directory is invalid")




data = ['A', 'B', 'D', 'B', 'D', 'E', 'F', 'D', 'G', 'A', 'E','A', 'B', 'B', 'D', 'F', 'D', 'G', 'A', 'D', 'E', 'G']

x = make_transition_matrix(data,3)


print(x)

