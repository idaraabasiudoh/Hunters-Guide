# Import necessary libraries
from openai import OpenAI
import os
from dotenv import load_dotenv
from tkinter import Tk, Label, ttk, Text, Toplevel, Scrollbar

# Load api_key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Get cover letter standards information
with open("cover_letter_standards.txt", "r") as file:
    cover_letter_standards = file.read()


# Get refining information
with open("refining.txt", "r") as file_2:
    refine = file_2.read()

with open("refining_2.txt", "r") as file_3:
    refine_2 = file_3.read()

with open("grade_resume_prompt.txt", "r") as file_4:
    grade_prompt = file_4.read()


# Function to generate cover letter based on user input
def generate_cover_letter(resume_text_widget, job_description_text_widget):
    try:
        # Retrieve resume and job description from text widgets
        resume = resume_text_widget.get("1.0", "end-1c")
        job_description = job_description_text_widget.get("1.0", "end-1c")

        # Generate response using OpenAI API
        response_1 = client.chat.completions.create(
        model="gpt-4o",
        messages=[
        {"role": "system", "content": f"Given this resume: \n\n {resume} \n\n and this job description: \n\n {job_description}\n\n Write a suitable cover letter using the following standards: \n\n{cover_letter_standards}"}
        ])

        # Rewrite response using OpenAI API
        response_2 = client.chat.completions.create(
        model="gpt-4o",
        messages=[
        {"role": "system", "content": f"Rewrite this cover letter by {refine}: \n\n{response_1.choices[0].message.content}"}
        ])

        # Rewrite response using OpenAI API
        response_3 = client.chat.completions.create(
        model="gpt-4o",
        messages=[
        {"role": "system", "content": f"Rewrite this cover letter by {refine_2}: \n\n{response_2.choices[0].message.content}"}
        ])

        # Update GUI elements based on successful response
        result_label.config(text="Result Generated")
        style.configure("Rounded.TFrame", background="green", relief="groove")

        # Display generated cover letter in a new window
        show_response_in_window(response_3.choices[0].message.content, "Generated Cover Letter")

    except Exception as e:
        # Handle exceptions and update GUI elements
        result_label.config(text="Generation Failed")
        style.configure("Rounded.TFrame", background="red", relief="groove")


# Function to tailor resume
def tailor_resume(resume_text_widget, job_description_text_widget):
    try:
        # Retrieve resume and job description from text widgets
        resume = resume_text_widget.get("1.0", "end-1c")
        job_description = job_description_text_widget.get("1.0", "end-1c")

        # Generate response using OpenAI API
        response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
        {"role": "system", "content": f"Given this resume: \n\n {resume} \n\n and this job description: \n\n {job_description}\n\n{grade_prompt}"}
        ])

        # Update GUI elements based on successful response
        result_label.config(text="Result Generated")
        style.configure("Rounded.TFrame", background="green", relief="groove")

        # Display generated cover letter in a new window
        show_response_in_window(response.choices[0].message.content, "Resume Insights")

    except Exception as e:
        # Handle exceptions and update GUI elements
        result_label.config(text="Generation Failed")
        style.configure("Rounded.TFrame", background="red", relief="groove")


# Function to generate interview questions
def interview_questions(job_description_text_widget):
    try:
        # Retrieve job description from text widgets
        job_description = job_description_text_widget.get("1.0", "end-1c")

        # Generate response using OpenAI API
        response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "system", "content": f"Given this job description: \n\n {job_description}\n\nGive me at least 15 interview non-technical questions and 15 interview technical questions for this job"}
        ])

        # Update GUI elements based on successful response
        result_label.config(text="Result Generated")
        style.configure("Rounded.TFrame", background="green", relief="groove")

        # Display generated cover letter in a new window
        show_response_in_window(response.choices[0].message.content, "Interview Questions")

    except Exception as e:
        # Handle exceptions and update GUI elements
        result_label.config(text="Generation Failed")
        style.configure("Rounded.TFrame", background="red", relief="groove")



# Function to display the generated content in a new window
def show_response_in_window(response_text, title):
    response_window = Toplevel(root)
    response_window.title(title)
    response_window.geometry("600x400")

    response_label = Text(response_window, wrap="word")
    response_label.insert("1.0", response_text)
    response_label.pack(expand=True, fill='both', padx=10, pady=10)

    # Add a scrollbar to the Text widget
    scrollbar = Scrollbar(response_window, command=response_label.yview)
    scrollbar.pack(side="right", fill="y")
    response_label.config(yscrollcommand=scrollbar.set)

    # Button to copy content
    copy_button = ttk.Button(response_window, text="Copy", command=lambda: response_window.clipboard_append(response_text))
    copy_button.pack(pady=10)

# Function to display guide
def guide():
    # Update GUI elements 
    result_label.config(text="Instructions:\n1. Paste your resume and the targeted job description into the respective input fields.\n2. Select 'Generate Cover Letter' to create a sample cover letter.\n3. Select 'Grade Resume' to get insights on resume.\n4. Select 'Generate Interview Questions' to get 30 potential interview questions.")
    style.configure("Rounded.TFrame", background="yellow", relief="groove")

# Create main Tkinter window
root = Tk()
root.title("Hunter's Guide")
root.configure(bg="#1d1e1f")

# Set up the GUI layout
header = Label(root, text="WELCOME TO HUNTER'S GUIDE", bg="#1d1e1f", fg="white", font=('FixedSys', 18, 'bold'))
header.pack(pady=5)

version = Label(root, text="Version 2.0.1", bg="#1d1e1f", fg="red", font=('FixedSys', 10, 'bold'))
version.pack(pady=5)

Label(root, text="Paste your resume below", bg="#1d1e1f", fg="white").pack()
resume_entry = Text(root, wrap="word", width=60, height=10)
resume_entry.pack(pady=5)

Label(root, text="Enter job description below", bg="#1d1e1f", fg="white").pack()
job_description_entry = Text(root, wrap="word", width=60, height=10)
job_description_entry.pack(pady=5)

# Result label frame
result_label_frame = ttk.Frame(root, style="Rounded.TFrame")
result_label = Label(result_label_frame, text="", bg="#131313", fg="white", wraplength=400, font=('FixedSys', 12))
result_label_frame.pack(pady=10)
result_label.pack(padx=10, pady=5)

# Buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=5)

generate_cover_letter_button = ttk.Button(button_frame, text="Generate Cover Letter", command=lambda: generate_cover_letter(resume_entry, job_description_entry))
generate_cover_letter_button.grid(row=0, column=0, padx=5, pady=5)

tailor_resume_button = ttk.Button(button_frame, text="Grade Resume", command=lambda: tailor_resume(resume_entry, job_description_entry))
tailor_resume_button.grid(row=0, column=1, padx=5, pady=5)

generate_questions_button = ttk.Button(button_frame, text="Generate Interview Questions", command=lambda: interview_questions(job_description_entry))
generate_questions_button.grid(row=0, column=2, padx=5, pady=5)

guide_button = ttk.Button(root, text="Guide", command=guide)
guide_button.pack(pady=5)

exit_button = ttk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=5)

# Configure GUI styles
style = ttk.Style()
style.configure("Rounded.TFrame", background="#131313", relief="groove")
style.configure("TButton", font=('FixedSys', 13), foreground='white')

# Start the Tkinter event loop
root.mainloop()