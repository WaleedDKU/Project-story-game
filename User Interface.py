import tkinter as tk

# Create a window
window = tk.Tk()
window.title("Account")


# Define functions for registration and sign-in
def register():
    # Create a new pop-up window for registration
    register_window = tk.Toplevel(window)
    register_window.title("Register")

    # Define a function to handle the registration form submission
    def submit_registration():
        # Open the "Accounts" file to check for existing usernames
        with open("Accounts.txt", "r") as f:
            existing_usernames = [line.strip().split(",")[0] for line in f.readlines()]

        # Get the entered username and password from the user
        username = register_username_entry.get().lower()
        password = register_password_entry.get()

        # Check if the username is blank or empty with spacebar
        if username == "" or " " in username:
            register_error_label.config(text="Invalid username.")
        # Check if the username is already taken
        elif username in existing_usernames:
            register_error_label.config(text="Username already taken.")
        # Check if the password is at least 10 characters long
        elif len(password) < 10:
            register_error_label.config(text="Password must be at least 10 characters.")
        # If all checks pass, save the username and password to the "Accounts" file
        else:
            with open("Accounts.txt", "a") as f:
                f.write(f"{username},{password}\n")
            register_success_label.config(text="Registration successful.")

    # Create labels and entry fields for the registration form
    register_username_label = tk.Label(register_window, text="Username")
    register_username_label.grid(row=0, column=0)
    register_username_entry = tk.Entry(register_window)
    register_username_entry.grid(row=0, column=1)

    register_password_label = tk.Label(register_window, text="Password")
    register_password_label.grid(row=1, column=0)
    register_password_entry = tk.Entry(register_window, show="*")
    register_password_entry.grid(row=1, column=1)

    # Create a button to submit the registration form
    register_button = tk.Button(register_window, text="Register", command=submit_registration)
    register_button.grid(row=2, columnspan=2)

    # Create a label for error messages
    register_error_label = tk.Label(register_window, fg="red")
    register_error_label.grid(row=3, columnspan=2)

    # Create a label for success messages
    register_success_label = tk.Label(register_window, fg="green")
    register_success_label.grid(row=4, columnspan=2)


def login():
    # Open the "Accounts" file to check for existing usernames and passwords
    with open("Accounts.txt", "r") as f:
        accounts = [line.strip().split(",") for line in f.readlines()]

    # Get the entered username and password from the user
    username = username_entry.get().lower()
    password = password_entry.get()

    # Check if the username and password match an existing account
    if [username, password] in accounts:
        success_label.config(text="Login successful.")
        success_label.grid(row=3, columnspan=2)  # Add success_label to the window
    else:
        error_label.config(text="Invalid username or password.")


# Create labels and entry fields for the username and password
username_label = tk.Label(window, text="Username")
username_label.grid(row=0, column=0)
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1)

password_label = tk.Label(window, text="Password")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1)

# Create buttons for registration and sign-in
register_button = tk.Button(window, text="Register", command=register)
register_button.grid(row=2, column=0)

login_button = tk.Button(window, text="Sign In", command=login)
login_button.grid(row=2, column=1)

# Create labels for error and success messages
error_label = tk.Label(window, fg="red")
error_label.grid(row=3, columnspan=2)

success_label = tk.Label(window, fg="green")
success_label.grid(row=4, columnspan=2)

# Start the main event loop
window.mainloop()
