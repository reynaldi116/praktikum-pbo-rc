import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.login_frame = tk.Frame(master)
        self.login_frame.pack(padx=10, pady=10)

        self.login_frame.configure(bg="#add8e6")

        self.users = {
            "rey": "1111",
        }

        self.label_username = tk.Label(self.login_frame, text="Username:")
        self.label_username.grid(row=0, column=0)
        self.entry_username = tk.Entry(self.login_frame)
        self.entry_username.grid(row=0, column=1)

        self.label_password = tk.Label(self.login_frame, text="Password:")
        self.label_password.grid(row=1, column=0)
        self.entry_password = tk.Entry(self.login_frame, show="*")
        self.entry_password.grid(row=1, column=1)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login, bg="#d2b48c") 
        self.login_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.register_button = tk.Button(master, text="Register", command=self.show_register_window, bg="#d2b48c")
        self.register_button.pack(pady=5)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in self.users and self.users[username] == password:
            messagebox.showinfo("Login Berhasil", "Selamat Datang, " + username + "!")
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah")

    def show_register_window(self):
        register_window = tk.Toplevel(self.master)
        register_window.title("Registrasi")

        register_frame = tk.Frame(register_window)
        register_frame.pack(padx=10, pady=10)

        register_frame.configure(bg="#add8e6")

        label_username = tk.Label(register_frame, text="Username:")
        label_username.grid(row=0, column=0)
        entry_username = tk.Entry(register_frame)
        entry_username.grid(row=0, column=1)

        label_password = tk.Label(register_frame, text="Password:")
        label_password.grid(row=1, column=0)
        entry_password = tk.Entry(register_frame, show="*")
        entry_password.grid(row=1, column=1)

        register_button = tk.Button(register_frame, text="Register", command=lambda: self.register(entry_username.get(), entry_password.get()), bg="#d2b48c") 
        register_button.grid(row=2, column=0, columnspan=2, pady=5)

    def register(self, username, password):
        if username in self.users:
            messagebox.showerror("Registrasi Gagal", "Username sudah terpakai")
        else:
            self.users[username] = password
            messagebox.showinfo("Registrasi Berhasil", "Akun berhasil dibuat")

            self.master.focus_set()
            self.master.grab_set()
            self.master.grab_release()

def main():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
