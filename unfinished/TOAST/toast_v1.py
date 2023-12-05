from sort_dict import *

def getin(inpt):
    correctio = input(f'Is "{inpt.lower()}" correct? (Y/N)\n')
    if correctio.lower() == "y":
        counted = input("Do you want it to be added to the list? (Y/N)\n")
        if counted.lower() == "y": truth = True
        else: truth = False 
        return [inpt.lower(), truth]
    else: return getin(input("Write the first word that comes to mind:\n"))

# T.O.A.S.T. stands for "Think Of Any Shit Thing" (yeah it is a work in progress name)

def toast_v1():
    new = {}
    text = ""
    output_text = ""

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

    new_word = getin(input("Write the first word that comes to mind:\n"))
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
    
    sorted_new = sort_dict(new)
    output_text = sorted_new

    print(output_text)

    # add sorting (look at stuff in new) + better ui
    # rest works fine


toast_v1()

