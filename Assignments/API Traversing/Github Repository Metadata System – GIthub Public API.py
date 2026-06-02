import requests

url = requests.get("https://api.github.com/repos/python/cpython")
response=url.json()

#1. Using a loop,Print total number of keys in repo record
# print("Total number of keys:", len(response))
# Using a loop:

count=0

for key in response:
    count+=1

print("Total Number of keys:",count)

# 2. Using a loop,Print all available key names
print("All available key names:")
for key in response.keys():
    print(key)

# 3. Using a loop,Print string fields (name, full_name, language)
print("String Fields contains: (name, full_name, language):")
fields = ["name", "full_name", "language"]

for field in fields:
    if isinstance(response[field], str):
        print(f"{field}: {response[field]}")

# 4. Using a loop,Print numeric fields (stars, forks, watchers)
print("Numeric fields (stars, forks, watchers):")
fields = ["stargazers_count","forks_count","watchers_count"]

for field in fields:
    if isinstance(response[field], int):
        print(f"{field}:{response[field]}")

# 5.Using a loop, Print owner details
print("Owner Details:")
for key,value in response["owner"].items():
    print(f"{key}: {value}")

# 6. Using a loop,Print repository URLs
print("URLs:")
for key,value in response.items():
    if "url" in key and isinstance(value,str):
        print(f"{key}: {value}")

# 7. Using a loop,Print boolean fields
print("Boolean Fields:")
for key,value in response.items():
    if isinstance(value,bool):
        print(f"{key}: {value}")

# 8. Using a loop,Print top-level keys only
print("Top Level keys:")
for key in response:
    print(key)

#9. Using a loop,Print first N key-value pairs
print("Top N=7 Level Keys:")
N=7
count=0

for key,value in response.items():
    print(f"{key}:{value}")
    count+=1

    if count==N:
        break

# 10.Using a loop, Print long text fields (> 40 characters)
print("Long Text Fields:")
for key,value in response.items():
    if isinstance(value,str) and len(value)>40:
        print(f"{key}:{value}")

# 11. Using a loop,Print searchable fields
print("Searchable Fields:")
fields = ["name","full_name","language"]

for field in fields:
    print(f"{field}:{response[field]}")

# 12.Using a loop, Print datatype of each key
print("DataType of each key:")
for key in response:
    print(f"{key}:{type(response[key])}")

# 13. Using a loop,Print index with each URL field
# count=1
# for key, value in response.items():
#     if "url" in key:
#         print(f"{count}. {key}:{value}")
#         count+=1

#using enumerate:
print("Index with each URL field:")
url_fields=[]

for key,value in response.items():
    if "url" in key:
        url_fields.append((key,value))

for index, (key,value) in enumerate(url_fields,1):
    print(f"{index}. {key}: {value}")

# 14.Using a loop, Print fields having dictionary values
print("Fields Having Dictionary Values:")
for key in response:
    if isinstance(response[key], dict):
        print(key)
        #print(f"{key}: {response[key]}")     #For Key-value Pairs

# 15. Using a loop,Print formatted repository report
print("==============Repository Report==============")

report = {
    "Repository Name": response["name"],
    "Full Name": response["full_name"],
    "URL": response["url"],
    "Owner": response["owner"]["login"],
    "Language": response["language"],
    "Description": response["description"],
    "Stars":response["stargazers_count"],
    "Forks":response["forks_count"],
    "Watchers":response["watchers_count"],
    "Network Count": response["network_count"],
    "Subscribers Count": response["subscribers_count"]
}

for key,value in report.items():
    print(f"{key}:{value}")