name = input("Hello welcome, my name is chatbot.101, Whats yours? ") 
print("hello nice to meet you " + name + ", thats such a nice name!!")
age = input("How old are you")
print("Wow " + age + " what a great age to be!! ")

program_loop = True

print("So," + name + " what can I do for you.")
def choices():
  print("\n1.Option 1\n2.Option 2\n3.End Conversation\n")

def choice():
  in_use = True
  option = input("Chose from the folowing options by typeing in a number 1-3: ")
  if option == "1":
    print("Option 1")
    return in_use
  elif option == "2":
    print("Option 2")
    return in_use
  elif option == "3":
    print("Good bye " + name + ", it was nice talking with you!!")
    in_use = False 
  else: 
    print("Sorry I didn't understand that 🥲\nCould you try again?\n")
    return in_use
while program_loop: 
  choices()
  program_loop = choice()