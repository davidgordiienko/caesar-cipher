running = True
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
encrypted_text = ""
decrypted_text = ""

custom_encrypted_text = ""
custom_decrypted_text = ""

def encrypt(text):
  print("Hello world")

while running:
  print("Available commands: \n Encrypt \n Decrypt \n Custom Text \n Exit")
  command = input("Enter a command:")
  if command.lower() == "encrypt":
    encrypted_text = ""
    input_text = input("Enter text to encrypt (only characters A-Z allowed):")
    for char in input_text:
      if char not in letters:
        print(char + "is not a letter from A-Z")
        break
      else:
        char_index = letters.index(char)
        encrypted_char = letters[(char_index + 5) % 53]
        encrypted_text += encrypted_char
    print(encrypted_text)
  elif command.lower() == "decrypt":
    if encrypted_text == "":
      print("Nothing to decrypt (did you encrypt anything yet?")
    else:
      for char in encrypted_text:
        encrypted_char_index = letters.index(char)
        decrypted_char = letters[(encrypted_char_index - 5) % 53]
        decrypted_text += decrypted_char
      print(decrypted_text)
      decrypted_text = ""
  elif command.lower() == "custom text":
    print("Custom Text Commands: \n Encrypt \n Decrypt \n Back")
    command = input("Enter a command:")
    if command.lower() == "encrypt":
      print("Encrypt")
      custom_input_text = input("Enter text to encrypt (only characters A-Z allowed):")
      for char in custom_input_text:
        if char not in letters:
          print(char + "is not a letter from A-Z")
          break
        else:
          char_index = letters.index(char)
          encrypted_char = letters[(char_index + 5) % 53]
          custom_encrypted_text += encrypted_char
      print(custom_encrypted_text)
      custom_encrypted_text = ""
    elif command.lower() == "decrypt":
      custom_encrypted_text = input("Enter text to decrypt (only characters A-Z allowed):")
      for char in custom_encrypted_text:
        encrypted_char_index = letters.index(char)
        decrypted_char = letters[(encrypted_char_index - 5) % 53]
        custom_decrypted_text += decrypted_char
      print(custom_decrypted_text)
      custom_decrypted_text = ""
  elif command.lower() == "exit":
    print("Goodbye!")
    running = False
