try:
    import customtkinter as ctk
except ModuleNotFoundError:
    print("Not all modules are installed")
    print("Modules needed: customtkinter")
    print("Check if these are installed on your device")

def darkmode():    
    if switch_var.get() == 'on':
        ctk.set_appearance_mode("dark")
    elif switch_var.get() == 'off':
        ctk.set_appearance_mode("light")

if __name__ == '__main__':
    app = ctk.CTk()
    app.geometry("1680x645")

    switch_var = ctk.StringVar(value="on")

    frame1 = ctk.CTkFrame(app, 
                          fg_color=("white", "black"),
                          height=645,
                          width=40)
    frame1.pack(padx=0, pady=0)

    switch1 = ctk.CTkSwitch(frame1,
                            text="enable darkmode",
                            command=darkmode,
                            variable=switch_var,
                            onvalue="on",
                            offvalue="off")
    switch1.pack(padx=0, pady=0)

    app.mainloop()
    