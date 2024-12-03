def zmnozi(text):
    i = 0
    zmnozek = 0
    while i < len(text):
        # print(i)
        # print(text[i:i+3])
        if text[i:i+3] == "mul":
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
    # print(zmnozek)
    return zmnozek

f = open("input.txt", "r")
text = ""
skupniZmnozek = 0
for line in f:
    skupniZmnozek+= zmnozi(line)
print(skupniZmnozek)

