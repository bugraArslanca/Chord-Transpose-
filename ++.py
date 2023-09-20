def transpose_chord(chord, semitones):

    all_chords = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    minor_chords = ['Cm','C#m','Dm','D#m','Em','Fm','F#m','Gm','G#m','Am','A#m','Bm']

    if chord in all_chords:
        chord_index = all_chords.index(chord)
        transposed_index = (chord_index + semitones) % 12
        transposed_chord = all_chords[transposed_index]
    elif chord in minor_chords:
        chord_index = minor_chords.index(chord)
        transposed_index = (chord_index + semitones) % 12
        transposed_chord = minor_chords[transposed_index]
    else:
        return chord
    return transposed_chord
print("__Chords Transpose App__")
def main():
    chord_bundle = input("Enter the chord sequence you want to transpose (for example 'C B Am F'): ")
    semitones = int(input("Enter how many semitones you want to transpose (positive up, negative down): "))

    chords = chord_bundle.split()

    transposed_chords = [transpose_chord(chord, semitones) for chord in chords]

    transposed_bundle = ' '.join(transposed_chords)
    print("Transposed chord sequence:", transposed_bundle)


if __name__ == "__main__":
    main()
