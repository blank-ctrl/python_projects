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


if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("500x645")
    switch_var = ctk.StringVar(value="on")

    frame1 = ctk.CTkFrame(app,
                          height=600,
                          width=450,
                          fg_color=("#d0d0f5", "#6a6a8f"))
    frame1.grid(row=0, column=0,padx=10, pady=10, ipadx=10, ipady=10)

    sw1 = ctk.CTkSwitch(frame1, 
                        fg_color="red",
                        button_color="#808080",
                        progress_color="#00ff7f",
                        command=darkmode,
                        variable=switch_var,
                        onvalue="on",
                        offvalue="off",
                        text="Enable Darkmode")
    sw1.grid(row=0, column=0, padx=10, pady=10)
    

    app.mainloop()
    