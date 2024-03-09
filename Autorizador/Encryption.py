from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
from Crypto.Cipher import AES

def encrypt(plaintext, key, iv):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext

def decrypt(ciphertext_b64, key, iv):
    print("Decrypt")
    print("B64  ",ciphertext_b64)
    # Decodificar la cadena Base64 en un arreglo de bytes
    ciphertext = base64.b64decode(ciphertext_b64)
    print("BYTES  ",ciphertext)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    # Eliminar el padding    
    plaintext = plaintext.rstrip(b'\0')          
    #backend = default_backend()
    #cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    #decryptor = cipher.decryptor()
    #decryptedText = decryptor.update(ciphertext) + decryptor.finalize()
    #decrypted_text = decryptedText.decode('utf-8')
    
    return plaintext

    
