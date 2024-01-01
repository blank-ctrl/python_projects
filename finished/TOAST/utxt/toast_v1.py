# needs an existing txt file called "store.txt" in the same directory as it is run in
# v1 will not create this file for you

def getin(inpt):
    if inpt.isalpha(): 
        correctio = input(f'Is "{inpt.lower()}" correct? (Y/N)\n')
        if correctio.lower() == "y":
            counted = input("Do you want it to be added to the list? (Y/N)\n")
            if counted.lower() == "y": truth = True
            else: truth = False 
            return [inpt.lower(), truth]
        else: return getin(input("Write the first word that comes to mind:\n"))
    else: 
        print("\n Only words are allowed! \n")
        getin()

# T.O.A.S.T. stands for "Think Of Any Senseless Thing" (wip name -_-)

def toast_v1():
    new = {}
    text = ""
    output_text = "\n"
    max_len = 0

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
    
    new_new = sorted(new.items(), key=lambda x:x[1], reverse=True)

    for i in new_new:
        if len(i[0]) > max_len: 
            max_len = len(i[0])

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

    print(output_text)
    
    #works nicely

toast_v1()

