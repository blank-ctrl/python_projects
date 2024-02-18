import sqlite3 as sql
import sys
import tkinter as tk


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

    txt.configure(text="*"*50)

    app.update()
    max_width = frame1.winfo_width()
    max_height = frame1.winfo_height()
    app.geometry(f"{max_width+20}x{max_height+20}")
    app.wm_maxsize((max_width+20), (max_height+20))

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
    txt.configure(text=output_text)

    #close connection
    cur.close()
    db_con.close()

    app.update()
    max_width = frame1.winfo_width()
    max_height = frame1.winfo_height()
    app.geometry(f"{max_width+20}x{max_height+20}")
    app.wm_maxsize((max_width+20), (max_height+20))

# ui
class Button:
    def __init__(self, button_text, button_column, button_command):
        self = tk.Button(master=frame2,
                         width=9,
                         fg="#800000",
                         text=button_text,
                         font='Roboto',
                         command=button_command,
                         background="#6a6a8f")
        self.grid(row=1,
                  column=button_column,
                  padx=3, 
                  pady=0)

if __name__ == "__main__":
    db_con = sql.connect("data.db")
    cur = db_con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS list (word TEXT, count INTEGER)")
    cur.close()
    db_con.close()

    app = tk.Tk()
    app.geometry("435x170")
    app.wm_maxsize(435, 170)
    app.title("T.O.A.S.T.")
    entry_var = tk.StringVar(value="on")
    checkbox_var = tk.StringVar(value="off")
    
    #widgets
    frame1 = tk.Frame(app,
                      bg="#6a6a8f",
                      height=30,
                      width=40)
    frame1.grid(row=0, column=0,padx=10, pady=10)

    frame2 = tk.Frame(frame1,
                     height=10,
                     bg="#6a6a8f")
    frame2.grid(row=1, column=0, columnspan=3, pady=5, padx=10)

    frame3 = tk.Frame(frame1,
                     width=380,
                     height=180,
                     bg= "#999999")
    frame3.grid(row=2, column=0, columnspan=3, pady=10, padx=10)

    entr1 = tk.Entry(master=frame2,
                     textvariable="Input",
                     font='Roboto',
                     fg="#FFFFFF",
                     width=40)
    entr1.grid(row=0, columnspan=3, padx=10, pady=10)
      
    txt = tk.Label(master=frame3,
                   text="*"*50,
                   justify="left")
    txt.grid(row=0, column=0, sticky="nw", ipadx=10, ipady=10)
    
    btn1 = Button("Submit", 0,lambda: toasting())
    btn2 = Button("Exit", 1, lambda: sys.exit())
    btn3 = Button("Clear All", 2, lambda: clearall())

    app.mainloop()