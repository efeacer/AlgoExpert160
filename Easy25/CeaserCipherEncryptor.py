def caesarCipherEncryptor(string, key):
	"""
	Encrypte each char: O(n)
	"""
	enc = ""
	len_alphabet = ord('z') - ord('a') + 1
	for c in string:
		temp = ord(c) - ord('a')
		temp += key
		temp %= len_alphabet
		temp += ord('a')
		enc += chr(temp)
	return enc