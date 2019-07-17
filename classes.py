import pyaudio
import numpy as np

notes = ['f', 'f#', 'g', 'g#','a', 'a#', 'b','c', 'c#', 'd', 'd#', 'e']
rom=['i','ii','iii','iv','v','vi','vii']
freq = {'f': 698.46/2, 'f#': 739.99/2, 'g': 783.99/2, 'g#': 830.61/2,'a': 440, 'a#': 466.16, 'b': 493.88, 'c': 523.25, 'c#': 554.37, 'd': 587.33, 'd#': 622.25, 'e': 659.25}
intervals = [2, 2, 1, 2, 2, 2, 1]
romans = {'i': 1, 'ii': 2, 'iii': 3, 'iv': 4, 'v': 5, 'vi': 6, 'vii': 7}


class note:
    def __init__(self, name):
        self.name = str(name)
        self.frequence = freq[self.name]


def powerchord(note):
    return [note, notes[(notes.index(note) + 7) % len(notes)]]


def major(note):
    return [note, notes[(notes.index(note) + 4) % len(notes)], notes[(notes.index(note) + 7) % len(notes)]]


def minor(note):
    return [note, notes[(notes.index(note) + 3) % len(notes)], notes[(notes.index(note) + 7) % len(notes)]]


def seventh(chord):
    chord.append(notes[(notes.index(chord[0]) + 10) % len(notes)])
    return chord


def majorseventh(chord):
    chord.append(notes[(notes.index(chord[0]) + 11) % len(notes)])
    return chord


def diminished(chord):
    chord[2] = notes(notes.index(chord[2]) - 1)


def augmented(chord):
    chord[2] = notes(notes.index(chord[2]) + 1)


class mode:
    gamme = []

    def ionian(self, key):
        self.gamme = []
        self.gamme.append(key)
        note = key
        for i in range(6):
            note = notes[(notes.index(note) + intervals[i]) % len(notes)]
            self.gamme.append(note)

        return self.gamme

    def dorian(self, key):
        self.gamme = []
        self.gamme.append(key)
        note = key
        for i in range(6):
            note = notes[(notes.index(note) + intervals[(i + 1) % len(intervals)]) % len(notes)]
            self.gamme.append(note)

        return self.gamme

    def phrygian(self, key):
        self.gamme = []
        self.gamme.append(key)
        note = key
        for i in range(6):
            note = notes[(notes.index(note) + intervals[(i + 2) % len(intervals)]) % len(notes)]
            self.gamme.append(note)

        return self.gamme

    def lydian(self, key):
        self.gamme = []
        self.gamme.append(key)
        note = key
        for i in range(6):
            note = notes[(notes.index(note) + intervals[(i + 3) % len(intervals)]) % len(notes)]
            self.gamme.append(note)

        return self.gamme

    def mixolydian(self, key):
        self.gamme = []
        self.gamme.append(key)
        note = key
        for i in range(6):
            note = notes[(notes.index(note) + intervals[(i + 4) % len(intervals)]) % len(notes)]
            self.gamme.append(note)

        return self.gamme

    def aeolian(self, key):
        self.gamme = []
        self.gamme.append(key)
        note = key
        for i in range(6):
            note = notes[(notes.index(note) + intervals[(i + 5) % len(intervals)]) % len(notes)]
            self.gamme.append(note)
        return self.gamme

    def locrian(self, key):
        self.gamme = []
        self.gamme.append(key)
        note = key
        for i in range(6):
            note = notes[(notes.index(note) + intervals[(i + 6) % len(intervals)]) % len(notes)]
            self.gamme.append(note)

        return self.gamme

def ismajor(chord):
    if chord[1] in major(chord[0]):
        return True
    else:
        return False
def isminor(chord):
    if chord[1] in minor(chord[0]):
        return True
    else:
        return False


def progression(a, b, c, d):  # gotta implement maj/min
    arguments = locals()
    chordstoplay=[]
    min = [j for i, j in arguments.items() if str.islower(j)]
    maj = [j for i, j in arguments.items() if str.isupper(j)]
    gamma = mode().ionian('c')
    chords = []
    for j in reversed(list(arguments.values())):
        if str.islower(j):
            if j in romans:
                chordstoplay.append(minor(gamma[romans[j] - 1]))
            if j in notes:
                chordstoplay.append(minor(j))
        if str.isupper(j):
            if str.lower(j) in romans:
                chordstoplay.append(major(gamma[romans[str.lower(j)] - 1]))
            if str.lower(j) in notes:
                chordstoplay.append(major(str.lower(j)))
    return chordstoplay


def playnote(note, time=1, oct=0):
    p = pyaudio.PyAudio()
    print(note)

    volume = 0.5  # range [0.0, 1.0]
    fs = 44100  # sampling rate, Hz, must be integer
    duration = float(time)  # in seconds, may be float
    f = (freq[str(note)])*(1+oct)  # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively)
    stream.write(volume * samples)

    stream.stop_stream()
    stream.close()

    p.terminate()


def playchord(chord,nature='major',time=1):
    chordtoplay=[]
    if str.lower(nature).__contains__('maj'):
        chordtoplay=major(chord)
    if str.lower(nature).__contains__('min'):
        chordtoplay=minor(chord)
    if str.lower(nature).__contains__('sev'):
        chordtoplay=seventh(chordtoplay)
    ind=-1
    octave=0
    for i in range(len(chordtoplay)):
        print(chordtoplay[i])
        if notes.index(chordtoplay[i])<ind: #to keep the notes moving up
            octave=1
        playnote(chordtoplay[i], oct=octave)
        ind=notes.index(chordtoplay[i])
