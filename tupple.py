# adding items to a tuple
city=("Delhi","Nairobi","Mombasa","Kisumu")
newcity = list(city)
newcity[1]="Addis Ababa"
city= tuple(newcity)
print(city)

# Add 
citi=("Delhi","Nairobi","Mombasa","Kisumu")
newcities = citi + ("Addis ababa",)
print(newcities)


#Remove
city=("Delhi","Nairobi","Mombasa","Kisumu")
newcity = list(city)
newcity.remove("Mombasa")
city= tuple(newcity)
print(city)
