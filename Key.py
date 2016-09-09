def Main():
    return "Hello, world!"

def Fun1(number, text):
    result = ""
    for i in range(0, number):
        result += str(number)
    result += "-" + text + "-"
    for i in range(0, number):
        result += str(number)
    return result