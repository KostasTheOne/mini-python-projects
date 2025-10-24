from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
FONT = ("Arial",10,"normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    rand_letters = [choice(letters) for char in range(randint(8,10))]
    rand_numbers = [choice(numbers) for number in range(randint(2,4))]
    rand_symbols = [choice(symbols) for symbol in range(randint(2,4))]
    password_list = rand_letters + rand_numbers + rand_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if website=="" or password=="" or email=="":
        messagebox.showinfo(title="Missing values", message="There are missing values.")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email}\nPassword:{password}\nIs it ok to save?")
        if is_okay:
            with open("data.txt","a") as file:
                file.write(f"{website} | {email} | {password} \n")
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            web_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)


canvas = Canvas(width = 200, height = 200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Website Label
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

#Website Entry
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()


#Email/Username
email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)



#Password
password_label = Label(text= "Password:", font= FONT)
password_label.grid(column=0, row=3)
password_entry = Entry(width=19)
password_entry.grid(column=1, row=3)



#Generate Password Button
pass_gen_button = Button(text="Generate Password",font= FONT,width=14, command=generate_password)
pass_gen_button.grid(column=2, row=3)

#Add Button
add_button = Button(text="Add",width=36, font=FONT, command=save_password)
add_button.grid(column=1, row=4,columnspan=2)





window.mainloop()
