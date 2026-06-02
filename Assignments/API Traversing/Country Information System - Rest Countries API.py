import requests

url=requests.get("https://restcountries.com/v3.1/name/india")
response = url.json()

#1. Using a loop, print the total number of keys in the country record
for country in response:
    print("Country:", country["name"]["common"])
    print("Total number of keys:", len(country))

# 2. Using a loop, print all available key names
print("all available key names:")
for country in response:
    print("Country:", country["name"]["common"])

    for key in country.keys():
        print(key)

# 3. Using a loop, print only string-type fields (region, subregion, status)
print("only string-type fields (region, subregion, status):")
fields = ["region", "subregion", "status"]

for country in response:
    for field in fields:
        if isinstance(country[field], str):
            print(f"{field}: {country[field]}")

# 4. Using a loop, print population, area, timezones
fields = ["population", "area", "timezones"]

for country in response:
    print("Country:", country["name"]["common"])

    for field in fields:
        print(f"{field}: {country[field]}")

# 5. Using a loop, print all official and common country names
for country in response:
    print("Common Name:", country["name"]["common"])
    print("Official Name:", country["name"]["official"])

# 6. Using a loop, print currency codes and currency names
for country in response:
    print("Country:", country["name"]["common"])

    for code, details in country["currencies"].items():
        print("Currency Code:", code)
        print("Currency Name:", details["name"])

# 7. Using a loop, print all spoken languages
print("all spoken languages:")
for country in response:
    print("Country:", country["name"]["common"])

    for code, language in country["languages"].items():
        print(language)

# 8. Using a loop, print all border country codes
print("all border country codes:")
for country in response:
    print("Country:", country["name"]["common"])

    if "borders" in country:
        for border in country["borders"]:
            print(border)

#9. Using a loop, print flag image URLs
print("flag image URLs:")
for country in response:
    print("Country:", country["name"]["common"])

    for key, value in country["flags"].items():
        if key in ["png", "svg"]:
            print(f"{key}: {value}")

#10. Using a loop, print top-level keys only
print("top-level keys only:")
for country in response:
    print("Country:", country["name"]["common"])

    for key in country.keys():
        print(key)

#11. Using a loop, print first N key-value pairs (example: first 8)
print("First 8 Key-Value pairs:")
N = 8

for country in response:
    count=0

    for key,value in country.items():
        print(f"{key}: {value}")
        count+=1

        if count == N:
            break

#12. Using a loop, print long text fields (> 25 characters)
print("long text fields (> 25 characters):")
for country in response:
    for key, value in country.items():
        if isinstance(value, str) and len(value) > 25:
            print(f"{key}: {value}")

# 13. Using a loop, print searchable text fields (country name, capital, region, languages)
print("searchable text fields (country name, capital, region, languages):")
for country in response:
    print("Country Name:", country["name"]["common"])
    print("Capital:",country["capital"][0])
    print("Region:", country["region"])

    for language in country["languages"].values():
        print(language)

# 14. Using a loop, print numeric values greater than 1 million
print("Numeric values greater than 1 million:")
for country in response:
    for key, value in country.items():

        if isinstance(value, (int,float)) and value > 1000000:
            print(f"{key}: {value}")

#15. Using a loop, print index number with each language name
print("index number with each language name:")
for country in response:
    print("Country:", country["name"]["common"])

    for index,language in enumerate(country["languages"].values(),1):
        print(f"{index}. {language}")