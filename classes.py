import pyaudio
import numpy as np
import random

notes = ['f', 'f#', 'g', 'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e']
rom = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii']
freq = {'f': 698.46 / 4, 'f#': 739.99 / 4, 'g': 783.99 / 4, 'g#': 830.61 / 4, 'a': 440 / 2, 'a#': 466.16 / 2,
        'b': 493.88 / 2, 'c': 523.25 / 2, 'c#': 554.37 / 2, 'd': 587.33 / 2, 'd#': 622.25 / 2, 'e': 659.25 / 2}
intervals = [2, 2, 1, 2, 2, 2, 1]
romans = {'i': 1, 'ii': 2, 'iii': 3, 'iv': 4, 'v': 5, 'vi': 6, 'vii': 7}
tonic=[1,3,6]
subdom=[2,4]
dom=[5,7]



class note:
    def __init__(self, name):
        self.name = str(name)
        self.frequence = freq[self.name]


def powerchord(note):
    if len(note)==4:
        note=note[0]
    if len(note)==5:
        note=note[0:1]
    return [note, notes[(notes.index(note) + 7) % len(notes)]]


def major(note):
    if len(note)==4:
        note=note[0]
    if len(note)==5:
        note=note[0:1]
    return [note, notes[(notes.index(note) + 4) % len(notes)], notes[(notes.index(note) + 7) % len(notes)]]


def minor(note):
    if len(note)==4:
        note=note[0]
    if len(note)==5:
        note=note[0:1]
    return [note, notes[(notes.index(note) + 3) % len(notes)], notes[(notes.index(note) + 7) % len(notes)]]


def seventh(chord):
    chord.append(notes[(notes.index(chord[0]) + 10) % len(notes)])
    return chord


def majorseventh(chord):
    chord.append(notes[(notes.index(chord[0]) + 11) % len(notes)])
    return chord


def diminished(chord):
    chord[2] = notes[(notes.index(chord[2]) - 1)%len(notes)]
    return chord


def augmented(chord):
    chord[2] = notes[(notes.index(chord[2]) + 1)%len(notes)]
    return chord


class mode:
    gamme = []

    def ionian(self, key='c'):
        self.gamme = []
        self.gamme.append(key)
        note = key
        for i in range(6):
            note = notes[(notes.index(note) + intervals[i]) % len(notes)]
            self.gamme.append(note)

        return self.gamme

    def dorian(self, key='c'):
        self.gamme = []
        self.gamme.append(key)
        note = key
        for i in range(6):
            note = notes[(notes.index(note) + intervals[(i + 1) % len(intervals)]) % len(notes)]
            self.gamme.append(note)

        return self.gamme

    def phrygian(self, key='c'):
        self.gamme = []
        self.gamme.append(key)
        note = key
        for i in range(6):
            note = notes[(notes.index(note) + intervals[(i + 2) % len(intervals)]) % len(notes)]
            self.gamme.append(note)

        return self.gamme

    def lydian(self, key='c'):
        self.gamme = []
        self.gamme.append(key)
        note = key
        for i in range(6):
            note = notes[(notes.index(note) + intervals[(i + 3) % len(intervals)]) % len(notes)]
            self.gamme.append(note)

        return self.gamme

    def mixolydian(self, key='c'):
        self.gamme = []
        self.gamme.append(key)
        note = key
        for i in range(6):
            note = notes[(notes.index(note) + intervals[(i + 4) % len(intervals)]) % len(notes)]
            self.gamme.append(note)

        return self.gamme

    def aeolian(self, key='c'):
        self.gamme = []
        self.gamme.append(key)
        note = key
        for i in range(6):
            note = notes[(notes.index(note) + intervals[(i + 5) % len(intervals)]) % len(notes)]
            self.gamme.append(note)
        return self.gamme

    def locrian(self, key='c'):
        self.gamme = []
        self.gamme.append(key)
        note = key
        for i in range(6):
            note = notes[(notes.index(note) + intervals[(i + 6) % len(intervals)]) % len(notes)]
            self.gamme.append(note)

        return self.gamme

    modes = {'mixolydian': mixolydian, 'lydian': lydian, 'dorian': dorian, 'ionian': ionian, 'aeolian': aeolian,
             'locrian': locrian, 'phrygian': phrygian}

    def recognizemode(self, mode):
        if str.__contains__(mode, "mix"):
            return self.mixolydian
        if str.__contains__(mode, "dor"):
            return self.dorian
        if str.__contains__(mode, "ion"):
            return self.ionian
        if str.__contains__(mode, "aeo"):
            return self.aeolian
        if (str.__contains__(mode, "lyd") and not (str.__contains__(mode, 'mix'))):
            return self.lydian
        if str.__contains__(mode, "phr"):
            return self.phrygian
        if str.__contains__(mode, "loc"):
            return self.locrian

    def commonnotes(self, mode1, mode2):
        a = []
        b = []
        m1 = self.recognizemode(mode1)
        m2 = self.recognizemode(mode2)
        k=list(set(m1('c')) & set(m2('c')))
        return k

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
    chordstoplay = []
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


def playnote(note, time=1,oct=0):  # taken from https://stackoverflow.com/questions/8299303/generating-sine-wave-sound-in-python?fbclid=IwAR2uEmbFYe5TgwHuI8UooLbnhdLumdap7lQF_0mwF_J-O6ZJRkPo-Sbjvkc
    p = pyaudio.PyAudio()
    print(note)

    volume = 0.5  # range [0.0, 1.0]
    fs = 44100  # sampling rate, Hz, must be integer
    duration = float(time)  # in seconds, may be float
    f = (freq[str(note)]) * (1 + oct)  # sine frequency, Hz, may be float #possibility of playing it an octave higher

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


def playchord(chord, times=1, nature='major', fourth=0):
    chordtoplay = []
    if str.__contains__(str.lower(nature), 'maj'):
        chordtoplay = major(str.lower(chord[0]))
    if (str.__contains__(str.lower(nature), 'min') and not(str.__contains__(str.lower(nature),'dim'))):
        chordtoplay = minor(chord[0])
    if str.__contains__(str.lower(nature), 'aug'):
        chordtoplay = augmented(chordtoplay)
    if str.__contains__(str.lower(nature), 'dim'):
        chordtoplay = diminished(chordtoplay)
    if fourth:  # adding the root on top
        chordtoplay.append(chordtoplay[0])
    ind = -1
    for k in range(times):
        octave = 0
        for i in range(len(chordtoplay)):
            if notes.index(chordtoplay[i]) < ind:  # to keep the notes moving up
                octave = 1
            playnote(chordtoplay[i], oct=octave)
            ind = notes.index(chordtoplay[i])


def playprogression(liste,f=1):
    for v in liste:
        if str.isupper(v):
            playchord(v, 1, nature='major', fourth=f)
        if str.islower(v):
            playchord(v, 1, nature='minor', fourth=f)


def playmelody(*args):
    for note in args:
        playnote(notes[note % len(notes)], 1, int(note / len(notes)))

allchords={}
for i in notes:
    new={tuple(major(i)):str.upper(i),tuple(minor(i)):str.lower(i),tuple(diminished(major(i))):str.upper(i)+'dim',tuple(diminished(minor(i))):str.lower(i)+'dim',tuple(augmented(major(i))):str.upper(i)+'aug',tuple(augmented(minor(i))):str.lower(i)+'aug'}
    allchords.update(new)

def identifychord(*args):
    chords=[]
    for i in allchords.keys():
        count=0
        for t in args:
            if t in i:
                count+=1
        if count==len(args):
            chords.append(i)
    results=[]
    for i in chords:
        results.append(allchords[i])
    return results

def chordsfromscale(scale):
    chords=[]
    for i in range(len(scale)):
        chord=[]
        chord.append(scale[i])
        chord.append(scale[(i+2)%len(scale)])
        chord.append(scale[(i+4)%len(scale)])
        chords.append(allchords[tuple(chord)])
    return chords

def semirandomprogression(modetoplay):
    chords=[]
    gamme=mode().recognizemode(modetoplay)()
    chordsavailable=chordsfromscale(gamme)
    r = random.choice(list(set().union(tonic,subdom)))
    for i in range (4):
        print(str(i)+' and the chord is '+str(r))
        if r in tonic:
            print('ton')
            chords.append(chordsavailable[r-1])
            r = random.randint(1, len(chordsavailable))
            continue
        if r in subdom:
            print('sub')
            chords.append(chordsavailable[r-1])
            r= random.choice(dom)
            continue
        if r in dom:
            print('dom')
            chords.append(chordsavailable[r-1])
            r = random.choice(tonic)
            continue

    return chords

def randomprogression(modetoplay):
    chords=[]
    gamme=mode().recognizemode(modetoplay)('c#')
    chordsavailable=chordsfromscale(gamme)
    for i in range (4):
        r = random.randint(1, len(chordsavailable))
        chords.append(chordsavailable[r-1])
    print(chords)
    return chords
