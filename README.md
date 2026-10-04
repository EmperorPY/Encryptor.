# **Encrypter**

This is a Python project I made while learning Python and cryptography.

**What it does**

This project is a local terminal application that lets you securely store and encrypt passwords. It uses industry-standard encryption to scramble your credentials into a hidden data file and manages a secret encryption key file behind the scenes.

**Features**

* Fully automated file and path management using the Python OS module.
* Secure two-way symmetrical encryption powered by the Cryptography library (Fernet).
* Multi-stage user menu for seamless adding, saving, and decoding of passwords.
* Internal verification guard that checks data structure health to prevent terminal crashes.

**What I learned**

* How to talk directly to the machine's operating system using the OS module to track relative script paths and directory structures.
* The core principles of modern encryption, including the use of binary file streams (`wb` and `ab`), type conversion, and key loading mechanics.
* Advanced loop tracking techniques using the `enumerate()` function to simultaneously manage index locations and data lines.

**How to run**

Make sure you install the required cryptography package first:
```bash
pip install cryptography
```
Then download the script files and run the Python file:
```bash
python Encrypter.py
```
Make sure you filter your search bar to ```Show Hidden``` if the file does not show up near your download or stored folder.

**Made with**

Python.

**Future improvements**

* Implement a `.gitignore` system to protect secret key configurations from being pushed online.
* A remove website/password feature.
* Build a master login phase using a predicided password you must remeber so the script relies on a memorable phrase aswell as a heavy raw file token.
