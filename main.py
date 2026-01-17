import random

notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

low_e = random.randint(0,11)
a = random.randint(0,11)
d = random.randint(0,11)
g = random.randint(0,11)
b = random.randint(0,11)
high_e = random.randint(0,11)

print(f'{notes[low_e]} |------------------------------------\n{notes[a]} |------------------------------------\n{notes[d]} |------------------------------------\n{notes[g]} |------------------------------------\n{notes[b]} |------------------------------------\n{notes[high_e]} |------------------------------------')

