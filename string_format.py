

def places(number):

    x = 0

    for i in number:
        x +=1
        if i == ".":
            x += 2
            break

    return number[:x]

