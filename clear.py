



def three_line():
    new_line()
    new_line()
    new_line()

def new_line():
    print
    
def nine_line():
    three_line()
    three_line()
    three_line()

def clear_screen():
    nine_line()
    nine_line()
    three_line()
    three_line()
    new_line()

clear_screen()
