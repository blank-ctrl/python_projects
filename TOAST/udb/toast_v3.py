try:
    import customtkinter as ctk
    import sqlite3 as sql
    import sys
except ModuleNotFoundError:
    print("Not all modules are installed")
    print("Modules needed: customtkinter, sys, sqlite3")
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


# db operations
def clearall():
    # open connection
    db_con = sql.connect("data.db")
    cur = db_con.cursor()

    # deleting all data from db
    cur.execute("DELETE FROM list")
    db_con.commit()
    
    # close connection
    cur.close()
    db_con.close()

# main process (toasting)
def toasting():
    # set output to " and get input
    output_text = ""
    ingoing = entr1.get()

    # open connection
    db_con = sql.connect("data.db")
    cur = db_con.cursor()
    
    # try to fetch current count of word
    current_val = cur.execute("SELECT count FROM list WHERE word=(:word)", (ingoing,)).fetchone()
    if current_val == None:                                       # add word and set its copunt to 1 if word not in table
        cur.execute("INSERT INTO list VALUES (:word, :initial)", (ingoing, 1))
        db_con.commit()
    else:                                                         # increment count of word if word in table
        cur.execute("UPDATE list SET count=(:num) WHERE word=(:word)", (current_val[0]+1, ingoing))
        db_con.commit()

    # fetching all data from db and sorting it
    db_data = cur.execute("SELECT * FROM list").fetchall()
    db_data.sort(key=lambda x: x[1], reverse=True)

    # create output
    for i in range(11):
        try:
            if i < 9:
                output_text += f"{i+1}.  {db_data[i][0]} ({db_data[i][1]}x)\n"
                if i == 2:
                    output_text += "Top 3 –––––\n"

            elif i == 9:
                output_text += f"{i+1}. {db_data[i][0]} ({db_data[i][1]}x)\n"
                output_text += "Top 10 –––––\n"
        except IndexError:
            pass

    # output
    lbl1.configure(text=output_text)
    
    #close connection
    cur.close()
    db_con.close()


# ui
class Button:
    def __init__(self, button_text, button_column, button_command):
        self = ctk.CTkButton(master=frame1,
                             width=100,
                             fg_color=("#E0115F", "#800000"),
                             text=button_text,
                             hover=True,
                             hover_color="#32CD32",
                             font=('Robot', 12),
                             command=button_command)
        self.grid(row=3,
                  column=button_column,
                  padx=0, 
                  pady=0)

if __name__ == "__main__":
    db_con = sql.connect("data.db")
    cur = db_con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS list (word TEXT, count INTEGER)")
    cur.clsoe()
    db_con.close()

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
    
    btn1 = Button("Submit", 1,lambda: toasting())
    btn2 = Button("Exit", 2, lambda: sys.exit())
    btn3 = Button("Clear All", 3, lambda: clearall())


    app.mainloop()