from cryptography.fernet import Fernet
import os
import subprocess
import time

#FORCE PYTHON TO USE THE SCRIPT'S ACTUAL FOLDER
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_PATH = os.path.join(SCRIPT_DIR, "Encrypter key.key")
VAULT_PATH = os.path.join(SCRIPT_DIR, "safe_data.dat")  # Renamed file

print("\nWelcome to the encryptor.\nThis script allows you to save and encrypt passwords in a different hidden file.The encryption key is saved in another hidden file.\nBOTH ARE HIDDEN AS THEY END IN UNRECOGNISED ENDING. FILTER YOUR FILE SEARCH BEFORE LOOKING.\nTo decrypt passwords input the key and your passwords will show.")



# 1. Handle the Key File
if os.path.exists(KEY_PATH):
    with open(KEY_PATH, "rb") as file:
        key = file.read()
        time.sleep(5)
        print("Key loaded successfully!")
else:
    key = Fernet.generate_key()
    with open(KEY_PATH, "wb") as file:
        file.write(key)
    print("New key generated and saved!")

cipher = Fernet(key)

# 2. Encryption Loop
while True:
    print("\n---------------\nENCRYPTION MENU\n---------------\nType quit to enter the next menu")
    website = input("Enter the website name:\n").strip()
    if website.lower() == "quit":
        break
        
    password = input("Enter a password for the website:\n").strip()
    if password.lower() == "quit":
        break
        
    # Combine website and password
    data_to_encrypt = f"{website}: {password}"
    encrypted_message = cipher.encrypt(data_to_encrypt.encode())
    
    # Save to the new dat file
    with open(VAULT_PATH, "ab") as file:
        file.write(encrypted_message + b"\n")
    print(f"🔒 Encrypted and saved credentials for {website}!")

# 3. Decryption / Viewing Loop
while True:
    print("\n---------------\nDECRYPTION MENU\n---------------\n")
    action = input("Scroll up to see passwords.\nType decode to see all passwords, or exit: ").strip().lower()
    
    if action == "exit":
        break
    elif action == "decode":
        #check to ensure the file exists before attempting to read it
        if not os.path.exists(VAULT_PATH) or os.path.getsize(VAULT_PATH) == 0:
            print("❌ No passwords saved yet! Please encrypt a password in Menu #1 first.")
            continue
            
        print("\n🔓 --- YOUR DECRYPTED VAULT ---")
        print("Enter Encryption Key: ")
        key_input = input().strip()
        
        # Verify the key matches
        if key_input != key.decode():
            print("❌ Invalid key.")
            break
            
        with open(VAULT_PATH, "rb") as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        decrypted_bytes = cipher.decrypt(line)
                        print(decrypted_bytes.decode())
                    except Exception:
                        print(f"⚠️ Line {line_num}: Could not decrypt. (Key mismatch)")
    else:
        print("Invalid option.")

print("\nThank You for using the encrypter.")
