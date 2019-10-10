import json
from difflib import get_close_matches

data= json.load(open("data.json"))

def translate(x):
    x = x.lower()
    if x in data:
        return data[x]
    elif len(get_close_matches(x, data.keys())) > 0:
        yn = input("did you mean %s instead? press Y if yes or N if no: " % get_close_matches(x, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(x, data.keys())[0]]
        elif yn == "N":
            return "The word does not exist."
        else:
            return "we did not understand your input."
    else:
        return "the word does not exist."

word = input("enter word: ")

ans = translate(word)

if type(ans) == list:
    for item in ans:
        print(item)
else:
    print(ans)
