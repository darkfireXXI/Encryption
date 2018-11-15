addNums = [1323167958085201897, 1819339588148037731, 2327902095847802161, 2887729552503424339, 2922296788110777449,
		   3494848181301462749, 3778627406977071029, 4519485822977169211, 5041919414598046411, 5915242218399104639,
		   7264955758847829793, 7290536627592441323, 7316903637688639081, 8997815051129627881, 9034734732789239447] # len 15
multNums = [12326779851643409, 17080571002102801, 19453110368729551, 21024073963517699, 31127804624033473,
			39469974484943129, 59719777782895381, 63693325002522731, 65391960222691703] # len 9
rotNums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61] # len 18
# print(str(bin(9034734732789239447))[2:].zfill(64))

# ENCRYPTION ------------ ENCRYPTION ------------ ENCRYPTION ------------
def encryption(filePath):
	global addNums, multNums, rotNums
	print('Encryption:')
	# print('Please write the text to be encrypted below:')
	# text = input()

	text =  open('{}encrypt.txt'.format(filePath), 'r')
	text = text.read()

	asciiText = []
	for i in text:
		asciiText.append(ord(i))
	# print(asciiText)

	biText = []
	for i in range(0, len(asciiText)):
		biText.append((str(bin(asciiText[i])[2:].zfill(64))))
	# print(biText)

	while(len(asciiText) > len(multNums)):
		addNums += addNums
		multNums += multNums
		rotNums += rotNums

	numText = []
	for i in range(0, len(asciiText)):
		if(asciiText[i]*multNums[i] >= 2**63):
			print('Fix this (1):', i, text[i], ord(text[i]), multNums[i])
		elif(addNums[i] >= 2**63):
			print('Fix this (2):', i, text[i], ord(text[i]), addNums[i])
		temp = str(bin(asciiText[i]*multNums[i]))[2:].zfill(63)
		temp0, temp1 = temp[0:63 - rotNums[i]], temp[63 - rotNums[i]:63]
		# print(temp)
		# print(temp1 + temp0)
		# print()
		numText.append(int('0' + temp1 + temp0, 2) + addNums[i])
	# print(numText)

	hexText = []
	hexMessage = ''
	for i in range(0, len(numText)):
		temp = str(hex(numText[i]))[2:].zfill(16)
		if(len(temp) > 16):
			print('help')
		hexText.append(temp)
		hexMessage += temp
	# print(hexText)
	print(hexMessage)

	message = open('{}message.txt'.format(filePath), 'w')
	message.write(hexMessage)

# DECRYPTION ------------ DECRYPTION ------------ DECRYPTION ------------

def decryption(filePath):
	global addNums, multNums, rotNums
	print('Decryption:')
	message =  open('{}message.txt'.format(filePath), 'r')
	message = message.read()
	# print(message)

	numText = []
	for i in range(0, len(message), 16):
		temp = int(message[i:i + 16], 16)
		numText.append(temp)
	# print(numText)

	while(len(numText) > len(multNums)):
		addNums += addNums
		multNums += multNums
		rotNums += rotNums

	asciiText = []
	for i in range(0, len(numText)):
		temp = numText[i] - addNums[i]
		temp = str(bin(temp))[2:].zfill(63)
		temp0, temp1 = temp[0:rotNums[i]], temp[rotNums[i]:63]
		# print(temp)
		# print(temp1 + temp0)
		# print()
		temp = int('0' + temp1 + temp0, 2)/multNums[i]
		asciiText.append(temp)
	# print(asciiText)

	text = ''
	for i in range(0, len(asciiText)):
		temp = chr(int(asciiText[i]))
		text = text + temp
	print(text)
		
# WORKING ------------ WORKING ------------ WORKING ------------

filePath = '/path/'

# encryption(filePath)
decryption(filePath)




