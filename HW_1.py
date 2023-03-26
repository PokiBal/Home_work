###  1  ###

# def print_details(name, last_name, age, phone):
#     {
#         print("\nMy identification details:\n",name, last_name,"\nAge:", age,"\nPhone number:", phone)
#     }
# print_details("Inbal","Rozenfeld",36, "054-3374944")




###  2  ###

# def check_string(str):
#     all_condition = False
#     try:
#         if str[7]== 'a' and str[8] =='b' and str[9] =='c':
#             all_condition = True
#             return print("True")
#         elif all_condition == False:
#             return print ("False")
#     except IndexError as msg:
#         print(msg)
    
# check_string("inbalis my name")
# check_string("asdfgrhabc")
# check_string("")

### 3  ###

# def oneStringSwapted(str1, str2):
#         part1_string = str2[:2] + str1[2:] + " " 
#         part2_string = str1[:2] + str2 [2:]
#         finalStr = part1_string + part2_string
#         return finalStr
# print(oneStringSwapted("abc","xyzhjhj"))
# print(oneStringSwapted("",""))

###  4  ###

# def append_ing_to_string(str):
#         x = len(str)
#         new_str=""
#         try:
#             assert x >=3, "Minimum 3 characters!"
#             if str[x-3:] == "ing":
#                 new_str = str+"ly"
#                 return new_str
#             else:
#                 new_str = str+"ing"
#                 return new_str
#         except AssertionError as msg:
#             print(msg)
#         return 

# print(append_ing_to_string("llling"))
# print(append_ing_to_string("lll"))


###  5  ###

# def new_string(str):
#         x = len(str)
#         y =int(x/2)
#         new_str=""
#         firstchar=str[0]
#         lastchar=str[x-1]
#         middlechar=str[y]       
#         try:
#             assert x >=3, "Minimum 3 characters!"
#             new_str += middlechar + str[1:y] + lastchar + str[y+1:x-1] + firstchar
#             return new_str
#         except AssertionError as msg:
#             print(msg)
            
#         return new_str

# print(new_string("afffbeeec")) 
# print(new_string("axxxbyyc"))
# print(new_string("as"))


###  6  ###

# def insertToMiddleString(original_str, strToAdd):
#     new_str=""
#     space = ' '
#     x=original_str.rfind(space)
#     new_str = original_str[0:x+1] + strToAdd + original_str[x:]
#     print(new_str)

# print(insertToMiddleString("Python 3.0", "Tutorial"))

