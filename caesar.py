# An encoder/decoder for our spies to secretly send messages.
encryption_option = input("Would you like to Encode or Decode? ") 

# should_encode will be true if the user 
should_encode = "encode" in encryption_option.lower()
# should_decode will be true if the user
should_decode = "decode" in encryption_option.lower()

# Ask the user for their message and cipher number.
cyper_number = int(input("What is your cypher number? "))
message = input("What is your message? ")
translated_message = ""
if should_encode:
    # Your code here!
    for i in range(len(message)):
      encode = message[i]

      # Keeps punctuation the same
      if (ord(encode) >= 32 and ord(encode) <= 47) or (ord(encode) >= 58 and ord(encode) <= 64) or (ord(encode) >= 91 and ord(encode) <= 96) or (ord(encode) >= 123 and ord(encode) <= 126):
          translated_message += chr(ord(encode))
      # Encodes only uppercase characters
      if encode.isupper():
        # Formula that ensures that the characters stay within the 65-90 ASCII range
          translated_message += chr(((((ord(encode) + cyper_number) - 65) % 26) + 65))
      # Encodes only lowercase characters
      if encode.islower():
        # Formula that ensures that the characters stay within the 97-122 ASCII range
          translated_message += chr(((((ord(encode) + cyper_number) - 97) % 26) + 97))
    pass
elif should_decode:
    # Your code here for extra credit
    # Focus on getting the code above to work first.
    for i in range(len(message)):
      decode = message[i]
      if ord(decode) == 32:
          translated_message += chr(32)
      # Decodes only uppercase characters
      if decode.isupper():
        # Formula that ensures that the characters stay within the 65-90 ASCII range
          translated_message += chr(((((ord(decode) - cyper_number) - 65) % 26) + 65))
      # Encodes only lowercase characters
      if decode.islower():
        # Formula that ensures that the characters stay within the 97-122 ASCII range
          translated_message += chr(((((ord(decode) - cyper_number) - 97) % 26) + 97))
    pass
else:
    # Print a nice notice that we only support encrypt/decrypt
    # Your code here!
    print("Error! This program only supports encrypt/decrypt. Please try again.")
    pass

print(translated_message)