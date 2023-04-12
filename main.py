import tkinter as tk
import random

# List of random cat jokes
cat_jokes = [
    "Why did the cat join the Red Cross? Because she wanted to be a first-aid kit",
    "What do you get when you cross a cat with a lemon? A sourpuss",
    "Why don't cats play poker in the jungle? Too many cheetahs",
    "What do you call a cat who likes to eat lemons? A sourpuss",
    "Why did the cat run away from the tree? It was afraid of the bark",
    "What do you get when you cross a cat with a bottle of vinegar? A sourpuss with claws",
    "Why don't cats like online shopping? They prefer a cat-alogue",
    "What do you call a cat who loves to bowl? An alley cat",
    "Why did the cat go to medical school? To become a purramedic"
]

# Define a function to display a random cat joke
def display_joke():
    # Clear the screen
    canvas.delete("all")
    # Choose a random joke
    joke = random.choice(cat_jokes)
    # Display the joke
    cat_img = tk.PhotoImage(file="resources/cat.png")
    canvas.create_image(400, 400, image=cat_img)
    canvas.create_text(400, 700, text=joke, font=("Arial", 12))
    canvas.pack()
    x1, y1, x2, y2 = canvas.bbox(joke)
    width = x2 - x1
    height = y2 - y1

# Create the main window
root = tk.Tk()
root.title("Cat Jokes")
cat_img = tk.PhotoImage(file="resources/cat.png")
# Create a canvas to display the cat face
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()

canvas.create_image(400, 400, image=cat_img)

# Create a button to display a random joke
button = tk.Button(root, text="Purress Here", fg="white", bg="green", font=("Arial", 12), command=display_joke)
button.pack()

# Start the main event loop
root.mainloop()



