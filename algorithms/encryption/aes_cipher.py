from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

"""Encriptación con AES
    Modo de operación EAX: Encrypt, Authenticate, Translate.
    Es un modo de operación de tipo Authenticated Encryption, (AEAD), que
    permite al receptor la verificación de la integridad de tanto el mensaje
    encriptado como el desencriptado. 
    EAX utiliza un número aleatorio de única vez (nonce), que debe ser de 
    16 bytes de longitud para AES.
    También usa una etiqueta MAC (Message Authentication Code), utilizada para
    confirmar que el mensaje viene del emisor declarado. Este MAX protege tanto
    la integridad como la autenticidad de un mensaje"""

# ENCRYPTION


def encryptAES(key, data):
    # tantos bytes como caracteres
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return nonce, ciphertext, tag


# DECRYPTION
def decryptAES(key, nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        print("Message is authentic")

    except ValueError:
        print("Key is incorrect or message is corrupted")
    return plaintext


if __name__ == "__main__":
    key = get_random_bytes(16)
    data = input("Escribe un mensaje a encriptar con AES: (128 chars MAX)\n")
    if len(data) > 128:
        data = data[:128]

    data = data.encode("ascii")
    # Encriptar
    print("\nEncriptando...\n")
    nonce, ciphertext, tag = encryptAES(key, data)

    ct_print = b64encode(ciphertext).decode("ascii")
    print("Ciphertext =>", ct_print)

    # Desencriptar
    print("\nDesencriptando...\n")
    m = decryptAES(key, nonce, ciphertext, tag)

    pt_print = m.decode("ascii")
    print("Plaintext =>", pt_print)

# https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html?highlight=eax%20mode#eax-mode
