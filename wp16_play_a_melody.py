import pygame
import time
import os

def play_melody(melody, sound_basedir):
    pygame.mixer.init()
    
    # Mapping sharp notes to their equivalent flat notes
    sharp_to_flat = {
        'C#': 'Db', 'D#': 'Eb', 'F#': 'Gb', 'G#': 'Ab', 'A#': 'Bb'
    }
    
    played_notes = []
    
    for note in melody:
        base_note, octave = note[:-1], note[-1]  # Separate note and octave
        
        # Convert sharp notes to their equivalent flat notes
        if base_note in sharp_to_flat:
            base_note = sharp_to_flat[base_note]
        
        filename = f"{base_note.lower()}{octave}.ogg"
        filepath = os.path.join(sound_basedir, filename)
        
        if os.path.exists(filepath):
            sound = pygame.mixer.Sound(filepath)
            sound.play()
            played_notes.append(filepath)
            time.sleep(0.5)  # Play each note for 400ms
        else:
            print(f"Warning: Sound file {filepath} not found!")
    
    return played_notes

# Example usage
MELODY_HAPPY_BIRTHDAY_TO_YOU = (
    'C4', 'C4', 'D4', 'C4', 'F4', 'E4',
    'C4', 'C4', 'D4', 'C4', 'G4', 'F4',
    'C4', 'C4', 'C5', 'A4', 'F4', 'E4', 'D4',
    'A#4', 'A#4', 'A4', 'F4', 'G4', 'F4',
)
MELODY_I_LOVE_YOU = [
    'G3', 'E3', 'G3', 'G3', 'E3', 'G3',
    'A3', 'G3', 'F3', 'E3', 'D3', 'E3', 'F3',
    'E3', 'F3', 'G3', 'C3', 'C3', 'C3', 'C3', 'C3', 'D3', 'E3', 'F3', 'G3',
    'G3', 'D3', 'D3', 'F3', 'E3', 'D3', 'C3',
    'G3', 'E3', 'G3', 'G3', 'E3', 'G3',
    'A3', 'G3', 'F3', 'E3', 'D3', 'E3', 'F3',
    'E3', 'F3', 'G3', 'C3', 'C3', 'C3', 'C3', 'C3', 'D3', 'E3', 'F3', 'G3',
    'G3', 'D3', 'D3', 'F3', 'E3', 'D3', 'C3',
]

MELODY_PERFECT = (
    'G4', 'A4', 'B4', 'G4', 'E4', 'D4',  # "I found a love"
    'G4', 'A4', 'B4', 'G4', 'E4', 'D4',  # "for me"
    'E4', 'G4', 'A4', 'B4', 'A4', 'G4', 'E4',  # "Darling, just dive right in"
    'D4', 'E4', 'G4', 'A4', 'B4', 'G4', 'E4', 'D4',  # "and follow my lead"
    
    # Chorus (simplified)
    'B4', 'A4', 'G4', 'E4', 'G4', 'B4',  # "I have faith in what I see"
    'B4', 'A4', 'G4', 'E4', 'G4', 'B4',  # "Now I know I have met"
    'A4', 'G4', 'E4', 'D4', 'E4', 'G4', 'A4', 'B4',  # "an angel in person"
    'G4', 'E4', 'D4'  # "and she looks perfect tonight"
)

MELODY_ODE_TO_JOY = (
    'E4', 'E4', 'F4', 'G4', 'G4', 'F4', 'E4', 'D4',
    'C4', 'C4', 'D4', 'E4', 'E4', 'D4', 'D4',
    'E4', 'E4', 'F4', 'G4', 'G4', 'F4', 'E4', 'D4',
    'C4', 'C4', 'D4', 'E4', 'D4', 'C4', 'C4',
)

MELODY_TWINKLE_TWINKLE = (
    'C4', 'C4', 'G4', 'G4', 'A4', 'A4', 'G4',
    'F4', 'F4', 'E4', 'E4', 'D4', 'D4', 'C4',
    'G4', 'G4', 'F4', 'F4', 'E4', 'E4', 'D4',
    'G4', 'G4', 'F4', 'F4', 'E4', 'E4', 'D4',
    'C4', 'C4', 'G4', 'G4', 'A4', 'A4', 'G4',
    'F4', 'F4', 'E4', 'E4', 'D4', 'D4', 'C4',
)

MELODY_MOONLIGHT_SONATA = (
    'Db4', 'E4', 'Ab4', 'Db5', 'E5', 'Ab5', 'Db5', 'Ab5', 'E5', 'Db5', 'Ab4', 'E4',
    'Db4', 'E4', 'Ab4', 'Db5', 'E5', 'Ab5', 'Db5', 'Ab5', 'E5', 'Db5', 'Ab4', 'E4',
    'B3', 'E4', 'Ab4', 'B4', 'E5', 'Ab5', 'B5', 'Ab5', 'E5', 'B4', 'Ab4', 'E4',
    'B3', 'E4', 'Ab4', 'B4', 'E5', 'Ab5', 'B5', 'Ab5', 'E5', 'B4', 'Ab4', 'E4',
    'A3', 'E4', 'A4', 'C5', 'E5', 'A5', 'C5', 'A5', 'E5', 'C5', 'A4', 'E4',
    'A3', 'E4', 'A4', 'C5', 'E5', 'A5', 'C5', 'A5', 'E5', 'C5', 'A4', 'E4'
)


# Call the function with the path to your piano sound files
play_melody(MELODY_RUSH_E, './sounds/piano')
