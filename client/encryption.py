from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

# create the RSA private key (and public key together with it)
def create_keys():
    private_key = rsa.generate_private_key(
            public_exponent = 65537,
            key_size = 2048,
            backend = default_backend(),
    )
    return private_key

# get the public key corresponding to the private key
def get_public_key(private_key):
    return private_key.public_key()

def get_public_key_pem(public_key):
    pem = public_key.public_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem

# save the private key on disk
def save_key(private_key, filename):
    pem = private_key.private_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm = serialization.NoEncryption()
    )
    with open(filename, "wb") as pem_out:
        pem_out.write(pem)

# load the private key from disk
def load_key(filename):
    with open(filename, "rb") as pem_in:
        private_key = serialization.load_pem_private_key(
            pem_in.read(),
            password=None,
        )
        return private_key

# encrypt a message with a public key
def encrypt(message, public_key):
    ciphertext = pubk.encrypt(
        message,
        padding.OAEP(
            mgf = padding.MGF1(algorithm = hashes.SHA256()),
            algorithm = hashes.SHA256(),
            label = None,
        )
    )
    return ciphertext

# decrypt a ciphertext with a private key
def decrypt(ciphertext, private_key):
    plaintext = nk.decrypt(
        ciphertext,
        padding.OAEP(
            mgf = padding.MGF1(algorithm = hashes.SHA256()),
            algorithm = hashes.SHA256(),
            label = None,
        )
    )
    return plaintext


#pk = create_keys()
#pubk = pk.public_key()
#message = b"this is a very secret message"
#ciphertext = encrypt(message, pubk)
#
#out = "private_key.pem"
#save_key(pk, out)
#
#nk = load_key(out)
#plaintext = decrypt(ciphertext, nk)
#assert(message == plaintext)
#
#public_key = get_public_key_pem(pk.public_key())
