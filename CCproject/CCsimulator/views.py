from django.shortcuts import render

def home(request):
	if request.method == "POST" and 'encrypt' in request.POST:
		message = request.POST.get('text')
		print(type(message))
		key = int(request.POST.get("key"))
		print(type(key))
		encrypted_message = ""
    
		for letter in message:
			if (letter.isalpha()):
				if (letter.isupper()):
					encrypted_message += chr((ord(letter) +key -65)%26 +65)
				elif (letter.islower()):
					encrypted_message += chr((ord(letter) +key -97)%26 +97)
			else:
				encrypted_message += letter		
		return render(request, "home.html", {'output': 'encrypt', 'text': message, 'key': key, 'result': encrypted_message})

	elif request.method == "POST" and 'decrypt' in request.POST:
		encrypted_message = request.POST.get('text')
		print(type(encrypted_message))
		key = int(request.POST.get("key"))
		print(type(key))
		decrypted_message = ""

		for letter in encrypted_message:
			if (letter.isalpha()):
				if (letter.isupper()):
					decrypted_message += chr((ord(letter) -key -65)%26 +65)
				elif (letter.islower()):
					decrypted_message += chr((ord(letter) -key -97)%26 +97)
			else:
				decrypted_message += letter
		return render(request, "home.html", {'output': 'decrypt', 'text': encrypted_message, 'key': key, 'result': decrypted_message})
		
	else:
		return render(request, "home.html")
