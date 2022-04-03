def times_table(a):
    for x in range(1, 13):
        answer = x * a
        print("{} times {} is {}".format(x, num, answer))
    

try:
    num = int(input("What do you want to multiply by?"))
except ValueError:
    num = int(input("Please enter a whole number"))
times_table(num)
