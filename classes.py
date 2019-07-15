notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
intervals = [2, 2, 1, 2, 2, 2, 1]
romans = {'i': 1, 'ii': 2, 'iii': 3, 'iv': 4, 'v': 5, 'vi': 6, 'vii': 7}


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


def progression(a, b, c, d):  # gotta implement flat/sharp
    arguments = locals()
    min = [j for i, j in arguments.items() if str.islower(j)]
    maj = [j for i, j in arguments.items() if str.isupper(j)]
    notes = mode().ionian('c')
    chords = []
    for j in reversed(list(arguments.values())):
        print(j)
        if j in min:
            print(minor(notes[romans[j] - 1]))
        if j in maj:
            print(major(notes[romans[str.lower(j)] - 1]))
