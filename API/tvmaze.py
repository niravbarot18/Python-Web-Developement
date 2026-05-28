import requests

userin = input("Enter Show Name:")

url = requests.get(f"https://api.tvmaze.com/search/shows?q={userin}")
mydata = url.json()

print(mydata)

# type
print("Type:", type(mydata))

# keys
print("Keys:",mydata[0].keys())

# access single data first show name

print(mydata[0]["show"]["name"])

# last name

print(mydata[-1]["show"] ["name"])

for i in mydata:
    print(i["show"]["name"])

# range

for i in range(len(mydata)):
    print(mydata[i]["show"]["name"])

# searching

# English Language
# ENGLISH , english , English

# english == english

for i in mydata :
    if "english" in i["show"]["language"].lower():
        print(i["show"]["name"])

for i in mydata:
    if i["show"] ["language"].upper() == "ENGLISH":
        print(i["show"]["name"])

# type -- > Animation

for i in mydata:
    if "animation" in i["show"]["type"].lower():
        print(i["show"]["name"])

# startswith
# string -- > start ?

# s name

for i in mydata:
    if i["show"]["name"].lower().startswith("s"):
        print(i["show"]["name"])

# endswith

for i in mydata:
    if i["show"]["name"].lower().endswith("an"):
        print(i["show"]["name"])

# count

# status -- > end

count = 0
for i in mydata:
    if "ended" in i["show"]["status"].lower():
        count += 1
print(count)

# LIST ENDED -- > LIST NAME

lst = []
for i in mydata:
    if "ended" in i["show"]["status"].lower():
        lst.append(i["show"]["name"])
    print(lst)

# hindi -- > Language
hindi_lang = []
for i in mydata:
    if "hindi" in i["show"]["language"].lower():
        hindi_lang.append(i["show"]["name"])
print(hindi_lang)
print(len(hindi_lang))

# genre -- > Action
for i in mydata:
    for j in i["show"]["genres"]:
        if "action" in j.lower():
            print(i["show"]["name"])

