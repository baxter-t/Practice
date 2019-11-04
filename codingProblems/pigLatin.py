def check_letters(w):

    return len([x for x in w if x.isalpha()]) == 0


def pig_it(s):

    words = s.split(" ")

    return " ".join([x[1:] + x[0] + "ay" for x in words if check_letters(x)])
print(pig_it("Pig latin is cool"))
