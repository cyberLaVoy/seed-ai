import random
from midiutil import MIDIFile

# Set up MIDI file
midi = MIDIFile(1)
track = 0
time = 0

# Text prompt
prompt = "Is this a dream?"

# Set tempo
tempo = 120
midi.addTempo(track, time, tempo)

# Choose a random scale to use for the music
scales = ["major", "minor"]
scale = random.choice(scales)

# Create a list of notes to use in the scale
if scale == "major":
    notes = [60, 62, 64, 65, 67, 69, 71, 72]
elif scale == "minor":
    notes = [60, 62, 63, 65, 67, 68, 70, 72]

# Add a melody to the track based on the text prompt
for ch in prompt:
    # Choose a random note from the scale
    note = random.choice(notes)
    # Set the duration based on the character in the prompt
    if ch == " ":
        duration = 1.0
    else:
        duration = 0.5
    # Add the note to the track
    midi.addNote(track, 0, note, time, duration, 100)
    time += duration

# Write the MIDI file to disk
with open("output.mid", "wb") as output_file:
    midi.writeFile(output_file)
