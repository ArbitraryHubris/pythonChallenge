# http://www.pythonchallenge.com/pc/def/map.html

# input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
input = "map"
output = [chr((ord(letter)-96+2)%26+96) if (ord(letter)>96 and ord(letter)<123) else letter for letter in input ]
print(''.join(output))
