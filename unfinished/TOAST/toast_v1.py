# T.O.A.S.T. stands for "Think Of Any Shit Thing" (yeah it is a work in progress name)

def toast_v1():
    new = []
    text = ""

    st = open("store.txt", "r")
    prior = st.readlines()
    st.close()

    for line in prior:
        print(line)
        string = True
        b = ""
        w = ""
        for thing in line:
            print(thing)
            if thing.isnumeric() and string: 
                w = w + thing
                string = False
            elif thing.isnumeric():
                w = w + thing  
            else: b = b + thing

        new.append([b, w]) # need to add dict instead of list + checker for key and value

    for stuff in new:
        stop = False
        for data in stuff:
            if stop: text = text + data
            else:
                text = text + f"\n {data} "
                stop = True # doesnt works as intended

    print(text)

toast_v1()
