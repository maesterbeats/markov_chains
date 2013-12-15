__author__ = 'andrewstern'


from markov import make_transition_matrix
import midi_utils as Midi






folder = '/Users/andrewstern/midi'
playlist = Midi.find_files(folder)


roar_melody = Midi.midi_parse(playlist.get('katy_perry-roar'),'note')
rhythms = Midi.midi_parse(playlist.get('katy_perry-roar'),'duration')

roar_melody = Midi.select_highest_notes(roar_melody)
roar_rhythms = Midi.select_highest_notes(rhythms)


melody_matrix = make_transition_matrix(roar_melody,1)
rhythm_matrix = make_transition_matrix(roar_rhythms,1)

print(rhythm_matrix)
