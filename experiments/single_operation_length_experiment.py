import time
import uuid

from util.kms import KMS


class SingleOperationLengthExperiment:
    """
    Experiment that checks what is the average time length of a single KMS
    service operation.
    """
    CYCLES = 100

    @classmethod
    def run(cls):
        string = str(uuid.uuid4())
        serialized_string = KMS.serialize(string)

        time_start_s = time.time()
        cls.__loop_serialize(cls.CYCLES, string)
        time_end_s = time.time()
        delta = time_end_s - time_start_s
        average = delta / float(cls.CYCLES)
        print(f'KMS encrypt operation on average took {average} seconds.')

        time_start_s = time.time()
        cls.__loop_deserialize(cls.CYCLES, serialized_string)
        time_end_s = time.time()
        delta = time_end_s - time_start_s
        average = delta / float(cls.CYCLES)
        print(f'KMS decrypt operation on average took {average} seconds.')

    @classmethod
    def __loop_serialize(cls, cycles: int, item: str):
        for i in range(cycles):
            # Perform serialization operations.
            KMS.serialize(item)

    @classmethod
    def __loop_deserialize(cls, cycles: int, item: str):
        for i in range(cycles):
            # Perform deserialization operations.
            KMS.deserialize(item)


if __name__ == '__main__':
    SingleOperationLengthExperiment.run()
