import sys

def encryption(message, offset):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	encrypted_text = ''

	for char in message.lower():
		if char == ' ' :
			encrypted_text += char
		else:
			index = alphabet.find(char)
			new_index = (index + offset) % len(alphabet)
			encrypted_text += alphabet[new_index]
	print('plain text:', message)
	print('encrypted text:', encrypted_text)

def decryption(message, offset):

	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	decrypted_text = '' 

	for char in message.lower():
		if char == ' ':
			decrypted_text += char
		else:
			index = alphabet.find(char)
			new_index = (index - offset) % len(alphabet)
			decrypted_text += alphabet[new_index]

	print('enrypted text:', message)
	print('plain text:', decrypted_text)




def caesar():
	if len(sys.argv) != 4:
		exit()
	else:
		if int(sys.argv[3]) < 26:
			if sys.argv[1] == '-e':
				encryption(sys.argv[2], int(sys.argv[3]))
			elif sys.argv[1] == '-d':
				decryption(sys.argv[2], int(sys.argv[3]))
		else:
			esxit()

if __name__ == '__main__':
	caesar()