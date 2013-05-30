


def three_lines():
    new_line()
    new_line()
    new_line()

three_lines()

def new_line():
    print
    
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

clear_screen()
