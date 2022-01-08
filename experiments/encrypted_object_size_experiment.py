import time
import uuid

from util.kms import KMS


class EncryptedObjectSizeExperiment:
    """
    Experiment that checks whether the object to encrypt/decrypt with KMS key has
    any effect on the performance of the KMS service.
    """
    CYCLES = 100

    @classmethod
    def run(cls):
        small_string = str(uuid.uuid4())
        big_string = str(uuid.uuid4()) * 100

        time_start_s = time.time()
        cls.__loop(cls.CYCLES, small_string)
        time_end_s = time.time()
        delta = time_end_s - time_start_s
        print(
            f'KMS encrypt/decrypt operation ({cls.CYCLES} cycles) for small string '
            f'({len(small_string)} length) took: {delta} seconds.'
        )

        time_start_s = time.time()
        cls.__loop(cls.CYCLES, big_string)
        time_end_s = time.time()
        delta = time_end_s - time_start_s
        print(
            f'KMS encrypt/decrypt operation ({cls.CYCLES} cycles) for big string '
            f'({len(big_string)} length) took: {delta} seconds.'
        )

    @classmethod
    def __loop(cls, cycles: int, item: str):
        for i in range(cycles):
            # Perform serialization/deserialization operations.
            KMS.deserialize(KMS.serialize(item))


if __name__ == '__main__':
    EncryptedObjectSizeExperiment.run()
