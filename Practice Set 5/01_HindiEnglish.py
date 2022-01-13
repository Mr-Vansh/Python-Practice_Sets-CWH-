hindiEnglish = {
    "kyu" : "why",
    "kya" : "what",
    "kab" : "when",
    "kaun" : "who",
    "kaise" : "how"
}

print("Options are : \n", hindiEnglish.keys())
a = input("Enter an hindi word for its english translation : ")

#   .get() will return ( NONE ) rather than throwing ( ERROR ) if provided key is not present in the LIST
print("English translation of the word is :", hindiEnglish.get(a))