# Exercise 4: Registration page ☑️
# Using widgets create a GUI as shown in below image

# Exercise 4: Registration page ☑️
# Using widgets create a GUI as shown in below image

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("12/nov/2023")
root.configure(bg="white")

def submit():
    stdname = studentNameEntry.get()
    stdmobnum = mobileNumEntry.get()
    stdemail = emailEntry.get()
    stdhome = homeAddrEntry.get()
    stdgender = selected_option.get()
    stdcourse = radio_var.get()

    # if not stdname or not stdmobnum or not stdemail or not stdhome or not stdgender or not stdcourse:
    if not all((stdname, stdmobnum, stdemail, stdhome, stdgender, stdcourse)):
        submit_button["text"] = "Incomplete"
        root.after(3000, lambda: submit_button.config(text="Submit"))
    else:
        submit_button["text"] = "Submitted"
        root.after(3000, lambda: submit_button.config(text="Submit"))

def clear():
    studentNameEntry.delete(0, "end")
    mobileNumEntry.delete(0, "end")
    emailEntry.delete(0, "end")
    homeAddrEntry.delete(0, "end")
    selected_option.set("")
    radio_var.set("")
    checkbox_var_1.set(False)
    checkbox_var_2.set(False)
    checkbox_var_3.set(False)


############### LOGO IMAGE ####################
script_directory = os.path.dirname(os.path.realpath(__file__))
img = Image.open(os.path.join(script_directory, "BSULOGO.png"))
tk_img = ImageTk.PhotoImage(img)

# Creating a label which contains the image
logolabel = tk.Label(root, image=tk_img)
logolabel.pack(side="top")

#################### Registration Page #########################

container = tk.Frame(root)
container.pack()
button_container = tk.Frame(container)

# Heading texts
text1 = tk.Label(container, text="Student Management System", font=("Helvetica", 16), fg="#22363D")
text1.grid(row=0, columnspan=3)

text2 = tk.Label(container, text="New Student Registration", font=("Helvetica", 14), fg="#22263D")
text2.grid(row=1, columnspan=3)

# Student name
studentNameLabel = tk.Label(container, text="Student Name")
studentNameLabel.grid(row=2, column=0)

studentNameEntry = tk.Entry(container)
studentNameEntry.grid(row=2, column=1)

# Mobile Number
mobileNumLabel = tk.Label(container, text="Mobile Number")
mobileNumLabel.grid(row=3, column=0)

mobileNumEntry = tk.Entry(container)
mobileNumEntry.grid(row=3, column=1)

# Email Adress
emailLabel = tk.Label(container, text="Email ID")
emailLabel.grid(row=4, column=0)

emailEntry = tk.Entry(container)
emailEntry.grid(row=4, column=1)

# Home Adress
homeAddressLabel = tk.Label(container, text="Home Address")  # Corrected variable name
homeAddressLabel.grid(row=5, column=0)

homeAddrEntry = tk.Entry(container)
homeAddrEntry.grid(row=5, column=1)

# Using ttk.Combobox for gender selection
genderLabel = tk.Label(container, text="Gender")
genderLabel.grid(row=6, column=0)

gender_options = ['Male', 'Female']
selected_option = tk.StringVar()
studentGenderDropdown = ttk.Combobox(container, textvariable=selected_option, values=gender_options, state="readonly")
studentGenderDropdown.grid(row=6, column=1)


# Courses Enrolled
courseLabel = tk.Label(container, text="Courses Enrolled")
courseLabel.grid(row=7, column=0)
radio_var = tk.StringVar(value=0)
# Radio buttons
radio_1 = tk.Radiobutton(container, text="BSc CC", variable=radio_var, value=1)
radio_1.grid(row=7, column=1)
radio_2 = tk.Radiobutton(container, text="BSc CY", variable=radio_var, value=2)
radio_2.grid(row=8, column=1)
radio_3 = tk.Radiobutton(container, text="BSc PSY", variable=radio_var, value=3)
radio_3.grid(row=9, column=1)
radio_4 = tk.Radiobutton(container, text="BA & BM", variable=radio_var, value=4)
radio_4.grid(row=10, column=1)


# Languages
langLabel = tk.Label(container, text="Languages Known")
langLabel.grid(row=11, column=0)

checkbox_var_1 = tk.BooleanVar()
checkbox_var_2 = tk.BooleanVar()
checkbox_var_3 = tk.BooleanVar()
# Checkboxes
checkbox_eng = tk.Checkbutton(container, text="English", variable=checkbox_var_1)
checkbox_eng.grid(row=11, column=1)

checkbox_tagalog = tk.Checkbutton(container, text="Tagalog", variable=checkbox_var_3)
checkbox_tagalog.grid(row=11, column=2)

checkbox_urdu_hindi = tk.Checkbutton(container, text="Hindi/Urdu", variable=checkbox_var_2)
checkbox_urdu_hindi.grid(row=12, column=1)

rateEngCommSkillsLabel = tk.Label(container, text="Rate Your English Communication Skills: ")
rateEngCommSkillsLabel.grid(row=13, columnspan=5)

slider = tk.IntVar()
rateEngCommSkillsScale = tk.Scale(container, from_=0, to=10, orient='horizontal', variable=slider, length=200)

# Configure the Scale widget with a blue background
ttk.Style().configure("TScale", troughcolor="lightblue")
ttk.Scale(container, from_=0, to=10, orient='horizontal', variable=slider, style="TScale").grid(row=14, columnspan=5)

submit_button = tk.Button(container, text="Submit", command=submit, bg="#22263D", fg="white", padx=20, pady=5)
submit_button.grid(row=15, column=0, columnspan=2, padx=(5, 10), pady=(5, 10))

clear_button = tk.Button(container, text="Clear", command=clear, bg="#22263D", fg="white", padx=20, pady=5)
clear_button.grid(row=15, column=1, columnspan=2, padx=(10, 10), pady=(10, 10))

root.geometry(f"{img.width}x600")

# displaying the window
root.mainloop()