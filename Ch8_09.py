# (Binary to hex) Write a function that parses a binary number into a hex number.
# The function header is:
# def binaryToHex(binaryValue):
# Write a test program that prompts the user to enter a binary number and displays
# the corresponding hexadecimal value.

binaryHexDictionary = {
'0000' : '0',
'0001' : '1',
'0010' : '2',
'0011' : '3',
'0100' : '4',
'0101' : '5',
'0110' : '6',
'0111' : '7',
'1000' : '8',
'1001' : '9',
'1010' : 'A',
'1011' : 'B',
'1100' : 'C',
'1101' : 'D',
'1110' : 'E',
'1111' : 'F'
}

def binaryToHex(binaryValue):
    strBinaryValue = str(binaryValue)
    noOfZeroes = 4 + len(strBinaryValue) % 4
    addZeroes = noOfZeroes * '0'
    if noOfZeroes != 0:
        strBinaryValue = addZeroes + strBinaryValue
    hex = ''
    # setOfFourBinary = strBinaryValue[len(strBinaryValue) - 4: len(strBinaryValue)]
    # hex = binaryHexDictionary[setOfFourBinary] + hex
    for i in range(0, len(strBinaryValue) - 4, 4):
        setOfFourBinary = strBinaryValue[len(strBinaryValue) - 4 - i: len(strBinaryValue) - i]
        hex = binaryHexDictionary[setOfFourBinary] + hex

    return hex

def test():
    binaryNumber = eval(input("Enter the binary number:"))
    print("Hex equivalent is:", binaryToHex(binaryNumber))


test()