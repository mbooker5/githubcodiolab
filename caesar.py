import sys

cypher_number = int(sys.argv[1])
uppercase_message = ""
for line in sys.stdin:
    uppercase_message += line.upper()

# Ask the user for their message and cipher number.
translated_message = ""
    # Your code here!
for i in range(len(uppercase_message)):
  encode = uppercase_message[i]

  # Keeps punctuation the same
  if (ord(encode) >= 32 and ord(encode) <= 47) or (ord(encode) >= 58 and ord(encode) <= 64) or (ord(encode) >= 91 and ord(encode) <= 96) or (ord(encode) >= 123 and ord(encode) <= 126):
      translated_message += chr(ord(encode))
  # Encodes only uppercase characters
  if encode.isupper():
    # Formula that ensures that the characters stay within the 65-90 ASCII range
      translated_message += chr(((((ord(encode) + cypher_number) - 65) % 26) + 65))
  # Encodes only lowercase characters
  if encode.islower():
    # Formula that ensures that the characters stay within the 97-122 ASCII range
      translated_message += chr(((((ord(encode) + cypher_number) - 97) % 26) + 97))
pass


print(translated_message)