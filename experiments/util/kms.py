import base64
import os

import boto3 as boto3


class KMS:
    KMS_BOTO_CLIENT = boto3.client('kms')
    KMS_KEY_ID = os.environ['KMS_KEY_ID']

    @staticmethod
    def serialize(value: str) -> str:
        encrypted: bytes = KMS.__encrypt(value)
        return base64.b64encode(encrypted).decode()

    @staticmethod
    def deserialize(value: str) -> str:
        base64_decoded_value = base64.b64decode(value)
        return KMS.__decrypt(base64_decoded_value)

    @staticmethod
    def __encrypt(sensitive_data: str) -> bytes:
        return KMS.KMS_BOTO_CLIENT.encrypt(
            KeyId=KMS.KMS_KEY_ID,
            Plaintext=sensitive_data.encode()
        )['CiphertextBlob']

    @staticmethod
    def __decrypt(sensitive_data: bytes) -> str:
        return KMS.KMS_BOTO_CLIENT.decrypt(
            KeyId=KMS.KMS_KEY_ID,
            CiphertextBlob=sensitive_data
        )['Plaintext'].decode()
