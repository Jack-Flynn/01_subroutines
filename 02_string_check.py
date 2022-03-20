def int_check(question):
    while True:
        try:
            response = int(input(question))
            if response <= 5:
                print("You are too young to to de doing this by yourself")
            elif 5 < response <= 15:
                print("Eh i guess you're old enough")
            elif 15 < response <= 30:
                print("Yeah your age is fine")
            elif 30 < response <= 60:
                print("Getting a bit old there are you?")
            elif 60 < response <= 110:
                print("Wow you really are a bit old")
            else:
                print("Uhh are you dead yet?")
            break

        except ValueError:
            print("Not a valid age")
    return response


int_check("How old are you?")
