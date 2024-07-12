mydict = {
         "fast": "In a quick respect",
         "prince": "A coder",
         "marks":[25,20,16],
         "otherdict": {'prince'}
          }

print(list(mydict.keys()))
print(mydict.values())
print(mydict.items())
print(mydict.get("prince2"))
print(mydict.get("prince"))
print(mydict["prince"])