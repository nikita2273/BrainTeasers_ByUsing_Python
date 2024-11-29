import tkinter as tk
from tkinter import messagebox, ttk
from quiz_data import quiz_data  # Ensure quiz_data is imported correctly

# Window setup
root = tk.Tk()
root.title("BrainTeasers")
root.geometry('800x600')  # Adjusted size for better fit
root.configure(bg="lightblue")

# Global variables
name = ""
current_question = 0
score = 0
correct_answers = 0

# Function to clear all widgets from the root window
def clear_widgets():
    for widget in root.winfo_children():
        widget.destroy()

# Function to display the final score
def display_score():
    clear_widgets()
    tk.Label(root, text="SCORE BOARD", font=("Arial", 45, "bold"), bg="lightblue").pack(pady=20)
    tk.Label(root, text=f"Your Name: {name}", font=("Arial", 40, "italic", "bold"), bg="lightblue").pack(pady=10)
    tk.Label(root, text=f"Your Score: {score}/{len(quiz_data)}", font=("Arial", 35, "italic", "bold"), bg="lightblue").pack(pady=10)
    tk.Label(root, text="Thank you for participating!", font=("Arial", 40, "bold"), bg="lightblue").pack(pady=20)

    # Home button to go back to the start page
    home_button = tk.Button(root, text="Home", font=("Arial", 20), command=show_home_page, bg="lightgreen")
    home_button.pack(pady=10)

# Function to show the home page
def show_home_page():
    clear_widgets()
    tk.Label(root, text="BrainTeaser", font=("Arial", 50, "bold"), bg="lightblue").pack(pady=20)

    # Name entry
    tk.Label(root, text="Enter Your Name:", font=("Arial", 30), bg="lightblue").pack(pady=10)
    global name_entry
    name_entry = tk.Entry(root, font=("Arial", 30))
    name_entry.pack(pady=10)

    # Start quiz button
    start_button = tk.Button(root, text="Start Quiz", font=("Arial", 25), command=start_quiz_handler, bg="lightgreen")
    start_button.pack(pady=20)

# Function to handle start quiz and initialize name
def start_quiz_handler():
    global name
    name = name_entry.get()
    if not name.strip():
        messagebox.showerror("Error", "Please enter your name to start the quiz!")
        return
    clear_widgets()
    initialize_quiz()

# Function to initialize the quiz interface
def initialize_quiz():
    global qs_label, choice_btns, feedback_label, score_label, next_btn, current_question, score

    root.config(bg="lavender")

    # Create the question label
    qs_label = ttk.Label(
        root,
        anchor="center",
        wraplength=500,
        padding=10,
        background="lavender"
    )
    qs_label.pack(pady=10)

    # Create the options frame
    options_frame = tk.Frame(root, bg="lavender")
    options_frame.pack(pady=30)

    # Create the choice buttons within the options frame
    choice_btns = []
    for i in range(4):
        button = ttk.Button(
            options_frame,
            command=lambda i=i: check_answer(i),
            width=25
        )
        button.grid(row=i // 2, column=i % 2, padx=10, pady=10)
        choice_btns.append(button)

    # Create the feedback label
    feedback_label = ttk.Label(
        root,
        anchor="center",
        padding=10,
        background="lavender"
    )
    feedback_label.pack(pady=10)

    # Initialize the score
    score = 0

    # Create the score label
    score_label = ttk.Label(
        root,
        text="Score: 0/{}".format(len(quiz_data)),
        anchor="center",
        padding=10,
        background="lavender"
    )
    score_label.pack(pady=10)

    # Create the next button
    next_btn = ttk.Button(
        root,
        text="Next",
        command=next_question,
        state="disabled"
    )
    next_btn.pack(pady=10)

    # Initialize the current question index
    current_question = 0

    # Show the first question
    show_question()

# Function to show the current question and choices
def show_question():
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    # Display the choices in the options frame
    for i, button in enumerate(choice_btns):
        button.config(text=question["choices"][i], state="normal")

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Function to check the selected answer and provide feedback
def check_answer(choice):
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")

    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to move to the next question
def next_question():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        # If there are more questions, show the next question
        show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        display_score()

# Start the main event loop
show_home_page()
root.mainloop()
