try:
    import customtkinter as ctk
    import sys
except ModuleNotFoundError:
    print("Not all modules are installed")
    print("Modules needed: customtkinter")
    print("Check if these are installed on your device")

# darkmode 
def darkmode():    
    if switch_var.get() == 'on':
        ctk.set_appearance_mode("dark")
    elif switch_var.get() == 'off':
        ctk.set_appearance_mode("light")

# fetching and replacing data (≈toast_v1)
def toasting():
    ingoing = entr1.get().strip()
    new = {}
    text = ""
    max_len = 0
    global output_text
    output_text = "\n"
    
    # getting stored data
    st = open("store.txt", "r")
    prior = st.readlines()
    st.close()

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
    if new_word[1]:
        if new_word[0] in new: new[new_word[0]] += 1
        else: 
            item = {new_word[0]: 1}
            new.update(item)

    for stuff in new:
        text += stuff + " " + str(new.get(stuff)) + "\n"

    lt = open("store.txt", "w")
    lt.write(text)
    lt.close
    
    # sorting dictionary of words in txt
    new_new = sorted(new.items(), key=lambda x:x[1], reverse=True)
    
    # defining lenght of longest word
    for i in new_new:
        if len(i[0]) > max_len: 
            max_len = len(i[0])
    
    # preparing output text
    for i in new_new:
        if new_new.index(i) < 9:
            emptyness = max_len-len(i[0])
            output_text += f"{new_new.index(i)+1}.  {i[0]}"
            while emptyness:
                output_text += " "
                emptyness -= 1
            output_text += f" ({i[1]}x)\n"

            if new_new.index(i) == 2:
                output_text += "Top 3 –––––\n"

        elif new_new.index(i) == 9:
            emptyness = max_len-len(i[0])
            output_text += f"{new_new.index(i)+1}. {i[0]}"
            while emptyness:
                output_text += " "
                emptyness -= 1
            output_text += f" ({i[1]}x)\n"
            output_text += "Top 10 –––––\n"
    
    # output
    lbl1.configure(text=output_text)
    

# ui
if __name__ == "__main__":
    app = ctk.CTk()
    switch_var = ctk.StringVar(value="on")
    
    #widgets
    frame1 = ctk.CTkFrame(app,
                          fg_color=("#d0d0f5", "#6a6a8f"))
    frame1.grid(row=1, columnspan=1,padx=10, pady=10)

    sw1 = ctk.CTkSwitch(frame1, 
                        fg_color="red",
                        button_color="#808080",
                        progress_color="#00ff7f",
                        command=darkmode,
                        variable=switch_var,
                        onvalue="on",
                        offvalue="off",
                        text="Enable Darkmode")
    sw1.grid(row=1, columnspan=2, padx=10, pady=10)

    entr1 = ctk.CTkEntry(master=frame1,
                         placeholder_text="Enter the first word you think of...",
                         font=('Roboto', 12),
                         text_color=("white", "black"),
                         placeholder_text_color="#B2BEB5",
                         fg_color=("#36454F", "#E5E4E2"),
                         width=300)
    entr1.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

    btn1 = ctk.CTkButton(master=frame1,
                         width=100,
                         fg_color=("#E0115F", "#800000"),
                         text="Submit",
                         hover=True,
                         hover_color="#32CD32",
                         font=('Robot', 12),
                         command=toasting)
    btn1.grid(row=3, column=1, padx=10, pady=10)

    btn2 = ctk.CTkButton(master=frame1,
                         width=100,
                         fg_color=("#E0115F", "#800000"),
                         text="Exit",
                         hover=True,
                         hover_color="#32CD32",
                         font=('Robot', 12),
                         command=lambda: sys.exit())
    btn2.grid(row=3, column=2, padx=10, pady=10)

    lbl1 = ctk.CTkLabel(master=frame1,
                        width=300,
                        height=250,
                        text="",
                        font=('Roboto', 12),
                        fg_color=("#36454F", "#E5E4E2"),
                        text_color=("white", "black"),
                        anchor="nw",
                        justify="left")
    lbl1.grid(row=4, column=1, columnspan=2, pady=10, padx=10)
    

    app.mainloop()
    