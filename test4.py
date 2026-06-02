word=str(input("enter a word or sentence:"))
print(len(word))
letters=len(word.replace(" ",""))
print(letters)    #length without spaces
print(word.lower())
print(word.upper())
print(word.title())
print(word.find("a"))
print(word.strip()) 
print(word.count(" "))   
print(word.capitalize())
print(word.split())
colors=["black","green","red"]
symbol="@"
print(symbol.join(colors))

