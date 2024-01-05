a = "ujjwal sharma u r best"
# output = Ujjwal Sharma U R Best 
# agar sare input mai capital hai toh small ho jayege 1st word capital

x = a.title()
print(x)

x = a.capitalize() # only 1st letter capital
print(x)

x = a.upper() # all are capitals
print(x) 

x = a.lower() # all are small
print(x) 

x = a.swapcase() # jo small mai hoga vo capital mai jo captial mai hoga vo small mai
print(x) 

x = a.isupper() # true false dega
print(x) 

x = a.islower() # true false dega
print(x) 

x = a.isalpha() # true false dega all are alphabets, ujjwal -> True, ujjwal sharma -> False , space se false aayega
print(x) 

x = a.isdigit() # true false dega, check digit
print(x)

x = a.isspace() # true false dega, \n next line, \t tab 
print(x)





























