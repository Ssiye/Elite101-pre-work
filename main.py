name = input("Hello welcome, my name is chtabot.Whats yours? ") 
print("hello nice to meet you " + name + "!! ")
age = input("How old are you")
print("Wow" + age + "what a great age to be!! ")
option = input(" So," + name + " what can I do for you.\nChose from the folowing options\nOption 1\nOption 2\nEnd Conversation")
if option == "Option 1":
  print("Option 1")
elif option == "Option 2":
  print("Option 2")
elif option == "End Conversation":
  print("Good bye" + name + " it was nice talking with you!!")
else:
  print("Sorry I dint understand that🥲\nCould you try again?")
  