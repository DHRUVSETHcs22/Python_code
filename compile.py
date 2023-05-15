import re
st="python is the best language"
comp=re.compile("best")
print(comp.search(st))
print(comp.match(st))
print(comp.sub("most",st))
print(comp.split(st))
print(comp.findall(st))
