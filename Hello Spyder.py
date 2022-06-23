from time import sleep

def cls():
    print("\033[2J\033[;H", end='')
    sleep(0.1)

cls()

name1 = input("First Name? ")
name2 = input("Last Name? ")
full_name = f"{name1.title()} {name2.upper()}"
message = f"Hello, {full_name}!"
print("")
print("\t",message,"\n\t How are you man?")
message1 = "I am doing very well"
print("\n\t",name1.title(),"says:", message1)
print(name1, name2)