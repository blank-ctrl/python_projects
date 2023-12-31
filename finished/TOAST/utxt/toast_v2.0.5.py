try:
    import customtkinter as ctk
    import sys
    import os.path
except ModuleNotFoundError:
    print("Not all modules are installed")
    print("Modules needed: customtkinter, sys")
    print("Check if these are installed on your device")

# theme toggle
def system_theme():
    if checkbox_var.get() == 'on':
        ctk.set_appearance_mode("system")
        sw1.configure(state="disabled")
    elif checkbox_var.get() == 'off':
        sw1.configure(state="normal")
        darkmode()

def darkmode():    
    if switch_var.get() == 'on':
        ctk.set_appearance_mode("dark")
    elif switch_var.get() == 'off':
        ctk.set_appearance_mode("light")

# clear .txt file
def clearall():
    st = open("store.txt", "w")
    st.write("")
    st.close()
    lbl1.configure(text="")
    

# fetching and replacing data (≈toast_v1)
def toasting():
    ingoing = entr1.get()
    new = {}
    text = ""
    global output_text
    output_text = "\n"
    
    # getting stored data    
    stt = open("store.txt", "r")
    prior = stt.readlines()
    stt.close()

    for line in prior:
        a = ""
        b = ""
        x = True
        for thing in line:
            try: 
                int(thing)
                b += thing
                x = False
            except ValueError: 
                if x == False: break
            if thing != " " and x: a += thing
        
        new.update({a: int(b)})
    
    # adding new word to txt
    new_word = ingoing
    if new_word in new:
        new[new_word] += 1
    else: 
        item = {new_word: 1}
        new.update(item)

    for stuff in new:
        text += stuff + " " + str(new.get(stuff)) + "\n"

    lt = open("store.txt", "w")
    lt.write(text)
    lt.close
    
    # sorting dictionary of words in txt
    new_new = sorted(new.items(), key=lambda x:x[1], reverse=True)
    
    # create output
    for i in range(0,11):
        try:
            if i < 9:
                output_text += f"{i+1}.  {new_new[i][0]} ({new_new[i][1]}x)\n"
                if i == 2:
                    output_text += "Top 3 –––––\n"

            elif i == 9:
                output_text += f"{i+1}. {new_new[i][0]} ({new_new[i][1]}x)\n"
                output_text += "Top 10 –––––\n"
        except IndexError:
            pass
    
    # output
    lbl1.configure(text=output_text)    
    

# ui
if __name__ == "__main__":
    # checking if .txt exists
    if not os.path.isfile("store.txt"):
        st = open("store.txt", "w")
        st.close()

    # main variables
    app = ctk.CTk()
    app.geometry("420x395")
    app.maxsize(width=420, height=395)
    app.title("T.O.A.S.T.")
    switch_var = ctk.StringVar(value="on")
    checkbox_var = ctk.StringVar(value="off")
    
    #widgets
    frame1 = ctk.CTkFrame(app,
                          fg_color=("#d0d0f5", "#6a6a8f"))
    frame1.grid(row=1, column=1,padx=10, pady=10)

    sw1 = ctk.CTkSwitch(frame1,
                        fg_color="red",
                        button_color="#808080",
                        progress_color="#4CBB17",
                        command=darkmode,
                        variable=switch_var,
                        onvalue="on",
                        offvalue="off",
                        text="Darkmode",
                        state="normal")
    sw1.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

    ckb = ctk.CTkCheckBox(frame1,
                          text="Mirror System",
                          onvalue="on",
                          offvalue="off",
                          variable=checkbox_var,
                          command=system_theme,
                          fg_color="#4CBB17")
    ckb.grid(row=1, column=2, columnspan=3)

    entr1 = ctk.CTkEntry(master=frame1,
                         placeholder_text="Enter the first word you think of...",
                         font=('Roboto', 12),
                         text_color=("black", "white"),
                         placeholder_text_color=("#899499", "#B2BEB5"),
                         fg_color=("#E5E4E2", "#36454F"),
                         width=380)
    entr1.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

    btn1 = ctk.CTkButton(master=frame1,
                         width=100,
                         fg_color=("#E0115F", "#800000"),
                         text="Submit",
                         hover=True,
                         hover_color="#32CD32",
                         font=('Robot', 12),
                         command=toasting)
    btn1.grid(row=3, column=1, padx=0, pady=0)

    btn2 = ctk.CTkButton(master=frame1,
                         width=100,
                         fg_color=("#E0115F", "#800000"),
                         text="Exit",
                         hover=True,
                         hover_color="#32CD32",
                         font=('Robot', 12),
                         command=lambda: sys.exit())
    btn2.grid(row=3, column=2, padx=0, pady=0)

    btn3 = ctk.CTkButton(master=frame1,
                         width=100,
                         fg_color=("#E0115F", "#800000"),
                         text="ClearAll",
                         hover=True,
                         hover_color="#32CD32",
                         font=('Robot', 12),
                         command=lambda: clearall())
    btn3.grid(row=3, column=3, padx=0, pady=0)

    srcl1 = ctk.CTkScrollableFrame(frame1,
                                   width=360,
                                   height=210,
                                   fg_color=("#E5E4E2", "#36454F"),
                                   orientation="horizontal",
                                   border_width=2)
    srcl1.grid(row=4, column=1, columnspan=3, pady=10, padx=10)

    lbl1 = ctk.CTkLabel(master=srcl1,
                        width=350,
                        height=210,
                        text="",
                        font=('Roboto', 12),
                        fg_color=("#E5E4E2", "#36454F"),
                        text_color=("black", "white"),
                        anchor="nw",
                        justify="left",
                        corner_radius=0)
    lbl1.grid(row=1, column=1, padx=0, pady=0)
    

    app.mainloop()
    