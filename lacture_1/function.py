# function is a block of code which only runs when it is caled
# function is build to execute some sort of task 
# A function can return data as a result

# def Hello():
#     print("Hello function is called")
# Hello()

# Arguments is the information that can be passed in the function and you can pass as many arguments as you want 

# def myfun(name):
#     print("Hello",name)
# myfun("Tanish")

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus") # function will receive the tuple of arguments

# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes") # it will receive as a dict 


def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
