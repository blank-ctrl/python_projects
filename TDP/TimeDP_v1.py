try:
    import customtkinter as ctk
    import sys
except ModuleNotFoundError:
    print("Not all modules are installed")
    print("Modules needed: customtkinter, sys")
    print("Check if these are installed on your device")

# toggle themes
def darkmode():    
    pass



# main
def main():
    pass


# add timespan
def add_timespan():
    pass


# add element
def add_element():
    pass

# remove last instance
def remove_last(var):
    pass

# advanced
def advanced():
    widget = Widget([200, 200], "Widget")


### ui
# elements
class Button:
    def __init__(self, parent, button_text, button_column, button_command):
        self = ctk.CTkButton(master=parent,
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
        
class Switch:
    def __init__(self) -> None:
        pass
        
class CheckBox:
    def __init__(self) -> None:
        pass

class Entry:
    def __init__(self) -> None:
        pass

class Label:
    def __init__(self) -> None:
        pass

class Frame:
    def __init__(self, main, position):
        self = ctk.CTkFrame(master=main[0],
                            fg_color=main[1],
                            width=(main[2]-(position[2]*2)),
                            height=(main[3]-(position[3]*2)))
        self.grid(row=position[0],
                  column=position[1],
                  padx=position[2],
                  pady=position[3],
                  columnspan=position[4])

class ScrollableFrame:
    def __init__(self) -> None:
        pass

# main     
class Widget:
    def __init__(self, size, title) -> None:
        self = ctk.CTk()
        self.geometry(f"{size[0]}x{size[1]}")
        self.maxsize(width=size[0], height=size[1])
        self.title(title)

        self.mainloop()
        
if __name__ == "__main__":

    main = ctk.CTk()
    main.geometry("420x395")
    main.maxsize(width=420, height=395)
    main.title("TDP")
    
    #elements of main
    Frame_main = Frame([main, ("#d0d0f5", "#6a6a8f"), 420, 395], [1, 1, 10, 10, 1])
    Button_main = Button(Frame_main, "button", 1, lambda: advanced())

    

    main.mainloop()