def encrypt():
    
    print("Welcome to Caesar Cipher Encryption.\n")
    message = input("Type a message you would like to encrypt: ")
    print()
    key = int(input("Enter your key: "))

    encrypted_message = ""
    
    for letter in message:
    	if (letter.isalpha()):
    		if (letter.isupper()):
    			encrypted_message += chr((ord(letter) +key -65)%26 +65)
    		elif (letter.islower()):
    			encrypted_message += chr((ord(letter) +key -97)%26 +97)
    	else:
    		encrypted_message += letter
    			
    print(encrypted_message)

encrypt()
