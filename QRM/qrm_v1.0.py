import customtkinter as ctk
import tkinter.filedialog as tkf
import sys
import qrcode
from PIL import Image

### process
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
  
## main
def qr_make():
    directory = tkf.asksaveasfilename()

    if directory:
        qr = qrcode.QRCode(box_size=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

        state = menu1.get()
        if state == "TEXT":
            qr.add_data(entr1.get())
        elif state == "HTTP":
            qr.add_data(f"http://{entr1.get()}")
        elif state == "HTTPS":
            qr.add_data(f"https://{entr1.get()}")

        qr.make(fit=True)
        img = qr.make_image()

        img_bg = Image.new(mode="RGB", size=(img.size[0], img.size[1]))
        img_bg.paste(img)
        img_bg.save(f"{directory}.png")


### ui
# elements
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
                  pady=15)

if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("420x160")
    app.maxsize(width=420, height=160)
    app.title("QRM")
    switch_var = ctk.StringVar(value="on")
    checkbox_var = ctk.StringVar(value="off")
    menu_var = ctk.StringVar(value="TEXT")
    
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
    sw1.grid(row=1, column=1, columnspan=2, padx=10, pady=15)

    ckb = ctk.CTkCheckBox(frame1,
                          text="Mirror System",
                          onvalue="on",
                          offvalue="off",
                          variable=checkbox_var,
                          command=system_theme,
                          fg_color="#4CBB17")
    ckb.grid(row=1, column=2, columnspan=3, pady=15)

    entr1 = ctk.CTkEntry(master=frame1,
                         placeholder_text="Enter your text ...",
                         font=('Roboto', 12),
                         text_color=("black", "white"),
                         placeholder_text_color=("#899499", "#B2BEB5"),
                         fg_color=("#E5E4E2", "#36454F"),
                         width=380)
    entr1.grid(row=2, column=1, columnspan=3, padx=10, pady=0)

    menu1 = ctk.CTkOptionMenu(master=frame1,
                             width=100,
                             values=["TEXT", "HTTP", "HTTPS"],
                             variable=menu_var)
    menu1.grid(row=3, column=3, pady=15)
    
    btn1 = Button("Create QR", 1,lambda: qr_make())
    btn2 = Button("Exit", 2, lambda: sys.exit())


    app.mainloop()