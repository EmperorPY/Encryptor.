# Encrypter Revamp

This is a Python project I made while learning Python and Encryption tools.

## What it does

This project is a local terminal application that lets you securely store and encrypt passwords. It uses industry-standard encryption to hash and derive 48000000 times and a master password for extreme security.

## Features

* Fully automated file and path management using the Python OS module.
* Secure encryption through hashing, the PBKDF2HMAC library for seamless conversion.
* Multi-stage user menu for seamless adding, saving, and decoding of passwords.
* Internal verification guard that checks data structure health to prevent terminal crashes.

## What I learned

* How to talk directly to the machine's operating system using the OS module to track relative script paths and directory structures.
* The core principles of modern encryption, including the use of binary file streams (`wb` and `ab`), type conversion, and key loading mechanics.
* Advanced loop tracking techniques using the `enumerate()` function to simultaneously manage index locations and data lines.
* What hashing is, the PBKDF2HMAC library, ``` base64.urlsafe_b64encode ``` method from the base 64 library and the getpass library for physical security.
* What salts are and how to use them effectively.

## How to run

Make sure you install the required cryptography package first:
```bash
pip install cryptography
```
Then download the script files and run the Python file:
```
python Encrypter.py
```

## Made with

Python, getpass, base64, cryptography.

## Future improvements

* A remove website/password feature.
* GUI?
