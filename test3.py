li=[]
with open("soundex_python.txt") as file:   
    data = file.read()

punc = '''-!()[]{};:'"\,<>./?@#$%^&*_~+=-'''
for element in data:  
    if element in punc:  
        data= data.replace(element, " ")
li=data.split()

def get_soundex(name):
    name=name.upper()
    soundex=""
    soundex+=name[0]
    dictionary = {"BFPV": "1", "CGJKQSXZ":"2", "DT":"3", "L":"4", "MN":"5", "R":"6", "AEIOUHWY":"."}

    for char in name[1:]:
        for key in dictionary.keys():
            if char in key:
                code = dictionary[key]
                if code != soundex[-1]:
                    soundex += code
    soundex = soundex.replace(".", "")
    soundex = soundex[:4].ljust(4, "0")
    return soundex
abc={}
lis=[]
if __name__ == '__main__':
    for name in li:
        abc[get_soundex(name)]=name
        lis.append(get_soundex(name))
        
check=[]
for i in lis:
    if lis.count(i) >1 and i not in check:
        check.append(i)
        print(f"{abc[i]} {i}")




