def good_morning(function):
    def inner_function():
        print("Good Morning Ujjwal sharma")
        function()
    return inner_function


@good_morning
def odinary():
    print("Happy Birthday!")


odinary()






