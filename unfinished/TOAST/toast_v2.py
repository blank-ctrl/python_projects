try:
    import customtkinter
    from datetime import datetime
except ModuleNotFoundError:
    print("Not all modules are installed")
    print("Modules needed: customtkinter, datetime")
    print("Check if these are installed on your device")

def darkmode():
    now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    
    print(switch_var.get())
    if switch_var.get() == 'on':
        customtkinter.set_appearance_mode("dark")
        print(f"{now} \nDarkmode state: on\n")
    elif switch_var.get() == 'off':
        customtkinter.set_appearance_mode("light")
        print(f"{now} \nDarkmode state: off\n")

if __name__ == '__main__':

    app = customtkinter.CTk()
    app.geometry("400x150")
    switch_var = customtkinter.StringVar(value="on")
    switch = customtkinter.CTkSwitch(app, text="enable darkmode", command=darkmode,
                                    variable=switch_var, onvalue="on", offvalue="off")
    switch.pack(padx=0, pady=0)

    app.mainloop()
    