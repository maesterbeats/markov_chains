__author__ = 'andrewstern'

import MIDI
import math

from collections import OrderedDict


def open_midi(file):
	b_file = open(file, 'rb')
	midi_data = b_file.read()
	score = MIDI.midi2score(midi_data)
	return score


def filter_duplicates_from_score(score, filter, sort_value, return_params):
	new_score = {}
	omit_channels = {10}			# channel 10 is percussion for GM
	iTrack = 1   					# skip 1st element which is ticks
	while iTrack < len(score):
		for event in score[iTrack]:
			channel_index = MIDI.Event2channelindex.get(event[0], False)
			if event[0] == filter:
				if channel_index and (event[channel_index] not in omit_channels):
					key = event[sort_value]
					value = event[return_params]
					if key in new_score.keys():
						new_score[key].add(value)
					else:
						new_score[key] = {value}
		iTrack += 1
	return new_score


def midi_parse(midi_file):
	score = open_midi(midi_file)
	ticks_per_beat = score[0]
	filtered_score = filter_duplicates_from_score(score, 'note', 1, 4)
	sorted_filtered_score = OrderedDict(sorted(filtered_score.items(), key=lambda t: t[0]))

	return sorted_filtered_score, ticks_per_beat




def notes_from_measure(score, ticks_per_beat = None, measure = None):
	'''
			Get all the notes in a measure
	---------------------------------------------------------------------

	@param score:			see MIDI.py
	@param ticks_per_beat:	int
	@param measure:			int (1 thru end of file)
	@return:				beat to note dict

	'''

	if ticks_per_beat:
		measure_len = ticks_per_beat * 4
	else:
		raise ValueError("ticks_per_beat requires int value")

	if measure:
		select_measure = measure - 1
	else:
		raise ValueError("measure requires int value")

	return {k: score[k] for k in score.keys() if (math.floor(k / measure_len)) == select_measure}, measure_len


def ticks_to_beats(measure, measure_lenth):

	return {int(((beat % measure_lenth)/measure_lenth * 16) + 1) :measure[beat] for beat in measure}







def get_measure_from_midi(midi_file, measure):
	"""
						Get the notes in a measure
	---------------------------------------------------------------------

	TODO:

		add optional parameters:		measure_range(int)
										tracks(list[int])
										omit_channels(list[int])

	---------------------------------------------------------------------


	@param midi_file:		a midi file
	@param measure: 		int (1 - end of song)
	@return:				notes(dict), measure_len, ticks_per_beat

	"""

	score,t_p_b = midi_parse(midi_file)

	sc , m_len = notes_from_measure(score,t_p_b,measure)
	parsed_measure = ticks_to_beats(sc,m_len)

	return parsed_measure
