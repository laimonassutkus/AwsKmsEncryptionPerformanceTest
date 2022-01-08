# Various experiments to test AWS KMS service performance

---

### Encrypted object size experiment.

The experiment checks whether the size of an object that is being encrypted
or decrypted with KMS service has any impact on the performance (e.g. length)
of operation of the KMS service.

To run an experiment:
```shell
python experiments/encrypted_object_size_experiment.py
```

Results:

```shell
- RUN 1
KMS encrypt/decrypt operation (100 cycles) for small string (36 length) took: 7.655616044998169 seconds.
KMS encrypt/decrypt operation (100 cycles) for big string (3600 length) took: 8.54363489151001 seconds.

- RUN2
KMS encrypt/decrypt operation (100 cycles) for small string (36 length) took: 7.862951993942261 seconds.
KMS encrypt/decrypt operation (100 cycles) for big string (3600 length) took: 10.226698160171509 seconds.

- RUN 3
KMS encrypt/decrypt operation (100 cycles) for small string (36 length) took: 7.87743878364563 seconds.
KMS encrypt/decrypt operation (100 cycles) for big string (3600 length) took: 8.440075159072876 seconds.

- RUN 4
KMS encrypt/decrypt operation (100 cycles) for small string (36 length) took: 7.4631102085113525 seconds.
KMS encrypt/decrypt operation (100 cycles) for big string (3600 length) took: 8.200579166412354 seconds.
```

---

### Single operation length experiment.

TODO.

To run an experiment:
```shell
python experiments/single_operation_length_experiment.py
```

Results:

```shell
- RUN 1
KMS encrypt operation on average took 0.03863358974456787 seconds.
KMS decrypt operation on average took 0.04181498050689697 seconds.

- RUN 2
KMS encrypt operation on average took 0.038693521022796634 seconds.
KMS decrypt operation on average took 0.03963184833526611 seconds.

- RUN 3
KMS encrypt operation on average took 0.03916390895843506 seconds.
KMS decrypt operation on average took 0.037720980644226076 seconds.

- RUN 4
KMS encrypt operation on average took 0.04037215948104858 seconds.
KMS decrypt operation on average took 0.03773927927017212 seconds.
```
