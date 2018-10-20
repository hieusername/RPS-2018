romanNumerals = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
}

num1 = input("What is your input? ")

def double_digit():
    num2 = (num1[0])

    if int(num2) > 0:
        if int(num2) < 4:
            output1 = romanNumerals.get(10)*int(num2)
            #print(output1)
        elif int(num2) == 4:
            output1 = romanNumerals.get(40)
            #print(output1)
        elif int(num2) > 4 and int(num2) < 9:
            output1 = romanNumerals.get(50)+(romanNumerals.get(10)*(int(num2)-5))
            #print(output1)
        elif int(num2) == 9:
            output1 = romanNumerals.get(90)
            #print(output1)

    num4 = (num1[1])

    if int(num4) < 4:
        output2 = romanNumerals.get(1)*int(num4)
        #print(output2)
    elif int(num4) == 4:
        output2 = romanNumerals.get(4)
        #print(output2)
    elif int(num4) > 4 and int(num4) < 9:
        output2 = romanNumerals.get(5)+(romanNumerals.get(1)*(int(num4)-5))
        #print(output2)
    elif int(num4) == 9:
        output2 = romanNumerals.get(9)
        #print(output2)

    print(str(output1)+str(output2))
def single_digit():
    num4 = (num1[0])

    if int(num4) < 4 and int(num4) > 0:
        output2 = romanNumerals.get(1) * int(num4)
        print(output2)
    elif int(num4) == 4:
        output2 = romanNumerals.get(4)
        print(output2)
    elif int(num4) > 4 and int(num4) < 9:
        output2 = romanNumerals.get(5) + (romanNumerals.get(1) * (int(num4) - 5))
        print(output2)
    elif int(num4) == 9:
        output2 = romanNumerals.get(9)
        print(output2)
    else:
        print("Zero!")

if int(num1) >= 10:
    double_digit()
else:
    single_digit()


