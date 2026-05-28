#resume dictionary

resume = {
    "Name":"Nirav",
    "Role":"Jr Intern",
    "Age": 20
}
print(resume)

#Covid Dictionary
covid = {"Ahmedabad": 1000, "Surat": 500,  "Rajkot":300}
print(covid)

#Type
print(type(covid))

#keys
print(covid.keys())

#values
print(covid.values())

#key-value pairs
print(covid.items())

#length
print(len(covid))

#accessing data
#rajkot case
print(covid["Rajkot"])

#surat case
print(covid["Surat"])


#mydata dictionary
mydata={"Ahmedabad":1000, "Surat":[500,550,600], "Rajkot":[300,400]}
print(mydata)
print(mydata["Surat"][1])
#550
print(mydata["Surat"][2])
#600


mydata2={"Ahmedabad":[{"Date":"21 May 2020","Case":1000},
                      {"Date":"25 May 2020","Case":1500},
                      {"Date":"27 May 2020","Case":1800},],
         "Surat":[400,500],
         "Rajkot":300}
print(mydata2)

print(mydata2["Ahmedabad"][2]["Case"])
#1800
print(mydata2["Ahmedabad"][1]["Date"])
#25 May 2020

