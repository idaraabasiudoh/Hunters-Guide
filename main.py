# Import necessary libraries
from openai import OpenAI
import os
from tkinter import Tk, Label, ttk, Text, Toplevel, Scrollbar
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)


# Function to generate cover letter based on user input
def generate_cover_letter(resume_text_widget, job_description_text_widget):
    try:
        # Retrieve resume and job description from text widgets
        resume = resume_text_widget.get("1.0", "end-1c")
        job_description = job_description_text_widget.get("1.0", "end-1c")

        # Generate response using OpenAI API
        response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "system", "content": f"Given this resume: \n\n {resume} \n\n and this job description: \n\n {job_description}\n\n Write a suitable cover letter in 3 paragraphs"}
        ])

        # Update GUI elements based on successful response
        result_label.config(text="Result Generated")
        style.configure("Rounded.TFrame", background="green", relief="groove")

        # Display generated cover letter in a new window
        show_response_in_window(response.choices[0].message.content, "Generated Cover Letter")

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
        model="gpt-3.5-turbo-1106",
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "system", "content": f"Given this resume: \n\n {resume} \n\n and this job description: \n\n {job_description}\n\nRewrite my resume to fit this job descripiton"}
        ])

        # Update GUI elements based on successful response
        result_label.config(text="Result Generated")
        style.configure("Rounded.TFrame", background="green", relief="groove")

        # Display generated cover letter in a new window
        show_response_in_window(response.choices[0].message.content, "Generated Tailored Resume")

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
        model="gpt-4",
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "system", "content": f"Given this job description: \n\n {job_description}\n\nGive me at least 30 interview type questions for this job"}
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



# Function to display the generated cover letter in a new window
def show_response_in_window(response_text, word):
    response_window = Toplevel(root)
    response_window.title(word)
    response_window.geometry("600x400")

    response_label = Text(response_window, wrap="word", width=60, height=20)
    response_label.insert("1.0", response_text)
    response_label.pack(pady=10)

    # Add a scrollbar to the Text widget
    scrollbar = Scrollbar(response_window, command=response_label.yview)
    scrollbar.pack(side="right", fill="y")
    response_label.config(yscrollcommand=scrollbar.set)

    # Button to copy content
    copy_button = ttk.Button(response_window, text="Copy", command=lambda: root.clipboard_clear() or root.clipboard_append(response_text))
    copy_button.pack(pady=10)



# Function to display guide
def guide():
    # Update GUI elements 
        result_label.config(text="Paste sample resume and targeted job description in respective input fields.\n1.Select Generate Cover Letter to generate sample cover letter.\n\n2.Select Tailor Resume to generate a tailored resume for you.\n\n3.Select Generate Interview-Type Questions to generate at least 30 interview type questions.")
        style.configure("Rounded.TFrame", background="yellow", relief="groove")
    

    
# Create main Tkinter window
root = Tk()
root.title("Hunters Guide")
root.configure(bg="#1d1e1f")

# Set up the GUI layout
guide_panel = Label(root, text="\t\t   WELCOME TO HUNTERS GUIDE\t\t\t",  bg="#1d1e1f", font=('FixedSys', 18, 'bold'))
guide_panel.pack()

guide_panel = Label(root, text="\t\t          Version 1.0.1\t\t\t",  bg="#1d1e1f",fg="red", font=('FixedSys', 10, 'bold'))
guide_panel.pack()

space = Label(root, text="\n",  bg="#1d1e1f", font=('Helvetica', 15, 'bold'))
space.pack(pady=10)

label_name = Label(root, text="Paste your resume below",  bg="#1d1e1f")
label_name.pack()

resume_entry = Text(root, wrap="word", width=40, height=10)
resume_entry.pack()

space = Label(root, text="\n\n",  bg="#1d1e1f", font=('Helvetica', 15, 'bold'))
space.pack(pady=10)

label_name = Label(root, text="Enter job description below", bg="#1d1e1f")
label_name.pack()

job_description_entry = Text(root, wrap="word", width=40, height=10)
job_description_entry.pack()

space = Label(root, text="\n",  bg="#1d1e1f", font=('Helvetica', 15, 'bold'))
space.pack(pady=10)

result_label_frame_1 = ttk.Frame(root, style="Rounded.TFrame")
result_label_frame_2 = ttk.Frame(result_label_frame_1, style="Rounded.TFrame")
result_label = Label(result_label_frame_2, text="\t\t\t\t\n", bg="#131313", fg="white", wraplength=400, font=('FixedSys', 12))
result_label_frame_1.pack(pady=10)
result_label_frame_2.pack(pady=5, padx=5)
result_label.pack()

generate_button = ttk.Button(root, text="Generate Cover Letter", command=lambda: generate_cover_letter(resume_entry, job_description_entry), style="TButton")
generate_button.pack()

generate_button = ttk.Button(root, text="Tailor Resume", command=lambda: tailor_resume(resume_entry, job_description_entry), style="TButton")
generate_button.pack()

generate_button = ttk.Button(root, text="Generate Interview-Type Questions", command=lambda: interview_questions(job_description_entry), style="TButton")
generate_button.pack()

space = Label(root, text="\n\n",  bg="#1d1e1f", font=('Helvetica', 15, 'bold'))
space.pack(pady=10)

generate_button = ttk.Button(root, text="Guide", command=lambda: guide(), style="TButton")
generate_button.pack()

exit_button = ttk.Button(root, text="Exit", command=root.destroy, style="TButton")
exit_button.pack(anchor="s")

space = Label(root, text="\n\n\n\n\n",  bg="#1d1e1f", font=('Helvetica', 15, 'bold'))
space.pack(pady=10)

# Configure GUI styles
style = ttk.Style()
style.configure("Rounded.TEntry", borderwidth=0, bordercolor="blue", relief="flat", background="blue", padding=(5, 5), width=200)
style.configure("Rounded.TFrame", background="blue", relief="groove")
style.configure("TButton", font=('FixedSys', 13), foreground='white')

# Start the Tkinter event loop
root.mainloop()
