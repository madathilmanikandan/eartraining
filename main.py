

# ear_training.py
import pygame
import random
import time
import os

# Initialize pygame mixer
pygame.mixer.init()

# Specify the folder where your music files are stored
music_folder = './music'

# List all files in the music folder
music_files = os.listdir(music_folder)

# Create a mapping from file names to keys
notes = {file.replace('.mp3', ''): os.path.join(music_folder, file) for file in music_files}

noteMap = {
    "1": "S",
    "2": "R",
    "3": "G",
    "4": "M",
    "5": "P",
    "6": "D",
    "7": "N"
}

# Function to play a random note
def play_random_note(last_played_note=None):
    if last_played_note is not None:
        # Play the last played note again
        note = last_played_note
        print("playing again")
    else:
        # Play a random note if there's no last played note
        note = random.choice(list(notes.keys()))
        print("playing random")

    pygame.mixer.music.load(notes[note])
    pygame.mixer.music.play()

    # Wait for the music to finish playing
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(30)  # Adjust the value to control the waiting time

    # Clear the mixer event queue
    pygame.mixer.music.stop()

    return note


# Main loop for the ear training exercise
def ear_training():
    last_played_note = None
    num_rounds = 10  # You can adjust the number of rounds as needed
    correct_answers = 0
    incorrect_patterns = []

    for _ in range(num_rounds):
        correct_note = play_random_note(last_played_note)
        user_guess = input("Your guess (enter the note or 'R' to repeat): ").upper()

        if user_guess == "R":
            # Repeat the last played note
            last_played_note =correct_note;
            continue  # Skip the rest of the loop

        pattern = [noteMap[char] for char in correct_note if char.isdigit()]
        swaras = ''.join(pattern)

        if user_guess == correct_note:
            print("Correct!")
            correct_answers += 1
            last_played_note = None
        else:
            print(f"Incorrect. The correct note was {swaras}")
            incorrect_patterns.append(swaras)
            last_played_note = None


    print(f"\nGame Over!\nCorrect Answers: {correct_answers}/{num_rounds}")

    if incorrect_patterns:
        print("Incorrect Patterns:")
        for pattern in incorrect_patterns:
            print(pattern)

# Uncomment the line below if you want to run this module independently
if __name__ == "__main__":
    ear_training()
