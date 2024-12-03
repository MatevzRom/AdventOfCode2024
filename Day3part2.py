def zmnozi(text, naredi):
    i = 0
    zmnozek = 0
    while i < len(text):
        if text[i:i+4] == "do()":
            naredi = True
        if text[i:i+7] == "don't()":
            naredi = False
        if text[i:i+3] == "mul" and naredi:
            i=i+3
            if text[i]=="(":
                number1 = ""
                number2 = ""
                j = 1
                first = True
                while True:
                    if text[i+j].isdigit() and first:
                        number1 += text[i+j]
                    elif text[i+j]==',':
                        first = False
                    elif text[i+j].isdigit() and not first:
                        number2 += text[i+j]
                    elif text[i+j]==')' and number1 != "" and number2 != "":
                        zmnozek += int(number1)*int(number2)
                        break
                    else:
                        break
                    j+=1
        i += 1
    return zmnozek, naredi

f = open("input.txt", "r")
text = ""
skupniZmnozek = 0
naredi = True
for line in f:
    zmnozek,naredi = zmnozi(line, naredi)
    skupniZmnozek+= zmnozek
print(skupniZmnozek)

