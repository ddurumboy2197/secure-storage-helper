import android
from android import Android, SharedPreferences

class SecureStorage:
    def __init__(self, context):
        self.context = context
        self.shared_preferences = SharedPreferences(context, "secure_storage")

    def set_secure_value(self, key, value):
        encrypted_value = self.encrypt(value)
        self.shared_preferences.edit().putString(key, encrypted_value).apply()

    def get_secure_value(self, key):
        encrypted_value = self.shared_preferences.getString(key, "")
        return self.decrypt(encrypted_value)

    def encrypt(self, value):
        # Android 10 dan oldin ishlatiladi
        if android.sdk_int < 29:
            from cryptography.fernet import Fernet
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)
            encrypted_value = cipher_suite.encrypt(value.encode())
            return encrypted_value.decode()
        else:
            # Android 10 dan keyin ishlatiladi
            from javax.crypto import Cipher
            from javax.crypto.spec import IvParameterSpec, SecretKeySpec
            from java.security import KeyFactory
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAKeyFactorySpi
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509EncodedKeySpec
            from java.security.spec import RSAPublicKeySpec
            from java.security.spec import RSAPrivateKeySpec
            from java.security.spec import PKCS8EncodedKeySpec
            from java.security.spec import X509
