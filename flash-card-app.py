import pandas as pd
import random
from tkinter import *

# Constants
BACKGROUND_COLOR = "#B1DDC6"
CSV_FILE = "data/swe-verbs.csv"
LEARN_FILE = "data/words_to_learn.csv"
ASSET_PATH = "assets/"  # Directory for images

# Global variables
to_learn = {}
current_card = {}

# ------------------------ File Handling -----------------------
def load_words():
    """Loads words from a CSV file. Falls back to the original CSV if 'words_to_learn.csv' is missing."""
    global to_learn
    try:
        data = pd.read_csv(LEARN_FILE)
    except FileNotFoundError:
        original_data = pd.read_csv(CSV_FILE)
        to_learn = original_data.to_dict(orient="records")
    else:
        to_learn = data.to_dict(orient="records")

def save_words():
    """Saves the remaining words to the 'words_to_learn.csv' file."""
    pd.DataFrame(to_learn).to_csv(LEARN_FILE, index=False)

# ------------------------ Card Manipulation -------------------
def next_card():
    """Selects a new random card and updates the UI."""
    global current_card
    current_card = random.choice(to_learn)
    update_card("Swedish", current_card["svenska"], "black", card_front_img)

def flip_card(event=None):
    """Flips the current card to show the English translation."""
    update_card("Español", current_card["espanol"] + "\n" + current_card["conjugacion"], "white", card_back_img)

def is_known():
    """Removes the known word and updates the CSV file."""
    to_learn.remove(current_card)
    save_words()
    next_card()

def update_card(title, word, color, image):
    """Updates the flashcard UI with new content."""
    canvas.itemconfig(card_title, text=title, fill=color)
    canvas.itemconfig(card_word, text=word, fill=color)
    canvas.itemconfig(card_background, image=image)

# ------------------------ FlashCard UI Setup -------------------
def setup_ui():
    """Sets up the UI for the flashcard application."""
    global window, canvas, card_title, card_word, card_background, card_front_img, card_back_img, cross_image, check_image

    window = Tk()
    window.title("Flashcard App")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    # Canvas setup
    canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    card_front_img = PhotoImage(file=ASSET_PATH + "card_front.png")
    card_back_img = PhotoImage(file=ASSET_PATH + "card_back.png")
    card_background = canvas.create_image(400, 263, image=card_front_img)
    card_title = canvas.create_text(400, 80, text="Title", font=("Ariel", 40, "italic"))
    card_word = canvas.create_text(400, 263, text="Word", width= 700, font=("Ariel", 60, "bold"))
    canvas.grid(row=0, column=0, columnspan=2)

    # Bind the canvas click event to flip the card
    canvas.tag_bind(card_background, "<Button-1>", flip_card)

    # Buttons with image references held globally
    cross_image = PhotoImage(file=ASSET_PATH + "wrong.png")
    unknown_button = Button(image=cross_image, command=next_card)
    unknown_button.grid(row=1, column=0, sticky="W")

    check_image = PhotoImage(file=ASSET_PATH + "right.png")
    known_button = Button(image=check_image, command=is_known)
    known_button.grid(row=1, column=1, sticky="E")

# ------------------------ Main Program ------------------------
if __name__ == "__main__":
    load_words()   # Load words from file
    setup_ui()     # Initialize the UI
    next_card()    # Show the first card
    window.mainloop()
