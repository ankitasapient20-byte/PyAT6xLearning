#built-in fxn
result= max(3.2)
print(result)

#No return type
def greet()
    print("Hello")

    greet()
#No return type and with args
def greet_by_name(name):
    print("Hello",name)

    greet_by_name("Ankita")

#No return type but default param
def say_hello_default_arg(name="Ankita"):
        print("Hello",name.upper())

        say_hello_default_arg() or
        say_hello_default_arg("Upadhyay")

    def multiple_args(name1="A", name2="B"):
        print("MUL--> ", name1, name2

         multiple_args()
        multiple_args(name1="Ankita", name2=Avantika)
        multiple_args(name1="Ankita")
        multiple_args(name2="Ankita", name1=Avantika)
