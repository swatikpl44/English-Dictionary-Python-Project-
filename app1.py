#                                        INTERACTIVE ENGLISH DICTIONARY

# JSON is a standard library
# Load the json file into a variable(of 'dict' type) using open method
# I have used 'diiflib' module and its 'get_close_matches' function to find the similar possibilities of a word

import json
import difflib
from difflib import get_close_matches

info= json.load(open("data.json"))

def meaning(w):
    w=w.lower()
    if w in info:
        return info[w]
    elif len(get_close_matches(w,info.keys())) > 0 :
        t= input("Did you mean %s instead? Enter y if yes, or n if no: " % get_close_matches(w,info.keys())[0])
        if t=='y':
            return info[get_close_matches(w,info.keys())[0]]
        elif t=='n':
            return "The word doesn't exist.Please double check it!!"
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist.Please double check it!!"

user_input= input("Enter word: ")
output= meaning(user_input)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)


#                                                  CODE ENDS HERE