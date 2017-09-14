import random

def monopolyworp():
    dubbel = 0

    while True:
        gooi1 = random.randint(1,6)
        gooi2 = random.randint(1,6)

        if gooi1 == gooi2:
            dubbel += 1

            if dubbel < 3:
                print("{} + {} = {} (dubbel)".format(gooi1,gooi2,gooi1+gooi2))
            else:
                print("{} + {} = (direct naar gevangenis)".format(gooi1,gooi2))
                break
        else:
            print("{} + {} = {}".format(gooi1,gooi2,gooi1+gooi2))
            break

monopolyworp()
