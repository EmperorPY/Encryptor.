from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64
import os
from getpass import getpass #Very cool library

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480_000_00,
    )
    print("hashing...")
    return base64.urlsafe_b64encode(kdf.derive(password.encode())) # Lets me use the right format fernet expects and pbkdf2hmac takes the master password and salt to encrypt.

#FORCE PYTHON TO USE THE SCRIPT'S ACTUAL FOLDER
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_PATH = os.path.join(SCRIPT_DIR, "safe_data.dat")
SALT_PATH = os.path.join(SCRIPT_DIR, "Salt.sal")

print("\nWelcome to the Password Vault.\nEnter a website and password to encrypt and save it.\nEnter your master password anytime to decrypt and view saved entries.\nNOTE: THE SCRIPT DOESNT FREEZE CHARACTERS ARE JUST HIDDEN FOR SECURITY PURPOSES.")

if os.path.exists(SALT_PATH):
    with open(SALT_PATH, "rb") as file:
        salt = file.read()
        print("Salt loaded successfully!")
else:
    salt = os.urandom(16)
    with open(SALT_PATH, "wb") as file:
        file.write(salt)
    print("New salt generated and saved!")

master_password = getpass("Enter your master password: ")
key = derive_key(master_password, salt) # Makes a key based on the hashed password and salt.

cipher = Fernet(key)

# 2. Encryption Loop
while True:
    print("\n---------------\nENCRYPTION MENU\n---------------\nType quit to enter the next menu")
    website = input("Enter the website name:\n").strip()
    if website.lower() == "quit":
        break
        
    password = getpass("Enter a password for the website:\n").strip()# Hides input (getpass)
    if password.lower() == "quit":
        break
        
    # Combine website and password
    data_to_encrypt = f"{website}: {password}"
    encrypted_message = cipher.encrypt(data_to_encrypt.encode())# Encrypts with the key and turns it to bytes.
    
    # Save to the new dat file
    with open(VAULT_PATH, "ab") as file:
        file.write(encrypted_message + b"\n")# Write the encrypted message to the file as bytes. (unreadable)
    print(f"🔒 Encrypted and saved credentials for {website}!")

print("\n---------------\nDECRYPTION MENU\n---------------\nScroll up to see passwords once you type decode.")

# 3. Decryption / Viewing Loop
while True:
    action = input("Type decode to see all passwords, or type exit to leave.\n").strip().lower()
    
    if action == "exit":
        break
    elif action == "decode":
        #check to ensure the file exists before attempting to read it
        if not os.path.exists(VAULT_PATH) or os.path.getsize(VAULT_PATH) == 0: # If the password file doesnt exist or the file size = 0 (nothing inside it) raise an error.
            print("❌ No passwords saved yet! Please encrypt a password in Menu #1 first.")
            continue
            
        print("\n\n\n\n🔓 --- YOUR DECRYPTED VAULT ---")
            
        with open(VAULT_PATH, "rb") as file:
            for line_num, line in enumerate(file, 1): # Creates a dictionary every line has an index that starts at 1 instead of 0
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        decrypted_bytes = cipher.decrypt(line)# Decrypts the password
                        print(decrypted_bytes.decode())# Makes the passwords converts to normal text and then prints it
                    except Exception:
                        print(f"⚠️ Line {line_num}: Could not decrypt. (Key mismatch)") # Error Message
    else:
        print("Invalid option.") # Error Message

print("\nThank You for using the encrypter.") # Exit message
