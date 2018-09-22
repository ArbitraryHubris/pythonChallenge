# http://www.pythonchallenge.com/pc/def/map.html

input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# since a is ord value of 97, subtract 96 so we can use modulus 26 to roll over from z to a
# then add the 96 back in and copy the resulting chr to the array
# letters not in the a-z set are copied as is with the else clause
output = [chr((ord(letter)-96+2)%26+96) if (ord(letter)>96 and ord(letter)<123) else letter for letter in input]

# create a string with '' and then join the array to that string
print(''.join(output))
