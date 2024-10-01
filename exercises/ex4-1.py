def pasta_time(time, budget):
    if time < 6:
        print("It's the middle of the night")
    if time > 22:
        print("The diner is closed by now")
    if budget < 10:
        print("You don't have enough money for anything fancy")
    if budget >= 10 and 6 <= time <= 22:
        print("Fettuccine Alfredo tonight!")
        if budget >= 13:
            print("Plus a side salad!")
    else:
        print("Looks like it's microwaved Mac & Cheese again")

if __name__ == '__main__':
    pasta_time(5,9)
    print()
    pasta_time(23, 9)
    print()
    pasta_time(6, 11)
    print()
    pasta_time(6, 13)