import datetime



def datetime_decorator(func):

        def decorated():

                print(datetime.datetime.now())

                func()

                print(datetime.datetime.now())

        return decorated()



@datetime_decorator

def main_function_1():

        print("MAIN FUNCTION 1 START")



@datetime_decorator

def main_function_2():

        print("MAIN FUNCTION 2 START")



@datetime_decorator

def main_function_3():

        print("MAIN FUNCTION 3 START")
