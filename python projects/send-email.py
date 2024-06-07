import customtkinter as ctk
import time

window = ctk.CTk()
window.title = ("Clock Application")
window.geometry("400x200")


frame = ctk.CTkFrame(master=window)
frame.pack(pady=20, padx=20, fill='both', expand=True)

hour = ctk.CTkFrame(master=frame)
hour

hour.pack(pady=5, padx=5)

minute = ctk.CTkFrame(master=frame)
minute.pack(pady=5, padx=5)


















window.mainloop()