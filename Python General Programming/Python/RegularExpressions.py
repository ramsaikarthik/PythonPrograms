import re

txt = "The rain in rain in spain"
txt_list = ["The rain in spain","Hindu","Muslim","Christain"]
x=[]
x.append(re.search("rain.in",txt))
x.append(re.search("rain|in",txt))
x.append(re.search("The.*",txt)) # . is for any character and * is for zero or more occurances
x.append(re.findall("[a-n]",txt))
print(x)