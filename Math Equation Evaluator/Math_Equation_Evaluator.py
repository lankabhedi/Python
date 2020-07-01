import re

print("""
************************************************
*--Python Project:  Basic Calculator-----------*
*---------Made By: Samnit Mehandiratta---------*
************************************************

Enter 'q' to quit, 'r' to reset and 'h' for help.
Hint: Type your equation after the prompt '>' and press Enter.
""")

switch = True
answer = ""


def calculator():
    global answer
    global switch
    equation = ""

    if str(answer) == "":
        equation = input("> ")
    else:
        equation = input("> " + str(answer))

    if equation == 'q':
        print("See you later human-like creature!")
        switch = False
    elif equation == 'r':
        answer = ""
    elif equation == "":
        pass
    elif equation == 'h':
        print("""
        The calculator supports addition(+), subtraction(-), multiplication(*), exponent(**),
        division(/) and modulus(//) using the operators as described in the brackets.
        """)
    # elif re.sub('[1234567890+*/" "]', '', equation) == "" or re.sub('[1234567890]', '', equation) == "-":
    # print("Please enter a number after the operator.")
    else:
        if "/0" in equation:
            print("Infinity")
            answer = ""
        else:
            equation = "@" + equation
            if (len(((re.sub('[A-Za-z;:)(&^%$#!|\'<>.,?="]', '', equation)).rstrip())) > 1) or (
                    ((re.sub('[A-Za-z;:)(&^%$#!|\'<>.,?="]', '', equation)).rstrip())[-1] in ["+", "-", "/", "*"]):
                equation = ((re.sub('[A-Za-z;:)(&^%$#@!|\'<>.,?="]', '', equation)).rstrip()).rstrip("*")
                equation = ((re.sub('[A-Za-z;:)(&^%$#@!|\'<>.,?="]', '', equation)).rstrip()).rstrip("+")
                equation = ((re.sub('[A-Za-z;:)(&^%$#@!|\'<>.,?="]', '', equation)).rstrip()).rstrip('/')
                equation = ((re.sub('[A-Za-z;:)(&^%$#@!|\'<>.,?="]', '', equation)).rstrip()).rstrip("-")
                equation2 = str(answer) + equation
                answer = eval(equation2)+0

            else:
                equation = re.sub('[A-Za-z;:)(&^%$#@!|\'<=>.,?"]', '', equation)
                equation = equation.replace(" ", "")
                equation2 = str(answer) + equation
                answer = eval(equation2)+0
                # print("Solution = " + answer)


while switch:
    calculator()
