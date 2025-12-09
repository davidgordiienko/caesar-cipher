# caesar-cipher
A simple caesar cipher I made in Python

## How to use this
Click on or download main.py and run it in an IDE of your choice. You can also run and see the code using this link: https://trinket.io/python3/a4397049c626

After successfully opening the file and running it, you'll be presented with 4 commands:
1. Encrypt
2. Decrypt
3. Custom Text
4. Exit

The regular way to run the program is to use "encrypt" first, which will save the encrypted output to a global variable. Then if you use "decrypt", it will reference that variable and decrypt it back into normal text.

However, I eventually realized it would make more sense if you were able to encrypt/decrypt individual strings of text independently of the global variable. I realized it didn't make sense to have to first encrypt something before you are able to decrypt it. So the "custom text" command brings you to a new sub-menu that lets you encrypt text without saving it to the global encrypted_text variable as well as decrypt inputted text without referencing the encrypted_text variable.

## AI Use
While a bit of AI was used to debug the code and spot logic errors, including text wrapping issues and syntax errors, all the code itself was written 100% by hand and was not generated with AI. AI was only used for debugging purposes and I did not directly use the code it gave me, but rather figured it out on my own based on what advice it gave me.

## Why I made this
I was bored and had the urge to program something so I made this quick little program to practice my Python and coding skills. I don't think a program like this would have any practical use but it was still a good practice experience nonetheless.
