def decrypt():
    
    print("Welcome to Caesar Cipher Decryption.\n")
    encrypted_message = input("Enter the message you would like to decrypt: ").strip()
    print()
    key = int(input("Enter key to decrypt: "))
    
    decrypted_message = ""

    for letter in encrypted_message:
    	if (letter.isalpha()):
    		if (letter.isupper()):
    			decrypted_message += chr((ord(letter) -key -65)%26 +65)
    		elif (letter.islower()):
    			decrypted_message += chr((ord(letter) -key -97)%26 +97)
    	else:
    		decrypted_message += letter

    print(decrypted_message)

decrypt()
