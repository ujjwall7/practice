global_variable = 10

def example_function():
    global global_variable
    global_variable = 11
    print("Inside the function:", global_variable)

example_function()

print(f"outside the function {global_variable}")








