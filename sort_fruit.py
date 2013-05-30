def sort_fruit(openfile, writefile):
    unsorted_fruits = []
    infile = open(openfile, 'r')
    outfile = open(writefile, 'w')

    while True:
        text = infile.readline()

        if text == "":
            break
        else:
            unsorted_fruits.append(text)

    unsorted_fruits.sort()

    for fruit in unsorted_fruits:
        outfile.write(fruit)

    infile.close()
    outfile.close()

    return

    
