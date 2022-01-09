# Various experiments to test AWS KMS service performance

When you encrypt data, you need to protect your encryption key. 
If you encrypt your key, you need to protect its encryption key. 
Eventually, you must protect the highest level encryption key 
(known as a root key) in the hierarchy that protects your data. 
That's where AWS KMS comes in.

AWS Key Management Service (KMS) makes it easy for you to create 
and manage cryptographic keys and control their use across a wide 
range of AWS services and in your applications. 
AWS KMS is a secure and resilient service that uses hardware 
security modules that have been validated under FIPS 140-2
to protect your keys.

However, the service will make your microservices slower.
The question is - by how much? That is why I created this 
experiments repository to find out.

### Prerequisites

- You should have knowledge in AWS and AWS KMS services.
- You should understand how encryption works and why it is needed.
- You must set `KMS_KEY_ID` environment variable to point to an
existing KMS KEY.
- Install dependencies by running `pip install -r requirements.txt`.

## Experiments

A list of experiments with result data and conclusions. 

---

### Encrypted object size experiment.

The experiment checks whether the size of an object that is being encrypted
or decrypted with KMS service has any impact on the performance (e.g. length)
of operation of the KMS service.

To run an experiment:
```shell
python experiments/encrypted_object_size_experiment.py
```

#### Results:

On MacBook PRO, 2021, Intel processor, 16GB RAM, 1Gbps WiFi network.

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

#### Results:

On Lambda function, 10240 MB (~10GB) RAM.

```shell
- RUN 1
KMS encrypt/decrypt operation (100 cycles) for small string (36 length) took: 1.1505467891693115 seconds.
KMS encrypt/decrypt operation (100 cycles) for big string (3600 length) took: 1.373429775238037 seconds.

- RUN 2
KMS encrypt/decrypt operation (100 cycles) for small string (36 length) took: 1.09722900390625 seconds.
KMS encrypt/decrypt operation (100 cycles) for big string (3600 length) took: 1.312774896621704 seconds.

- RUN 3
KMS encrypt/decrypt operation (100 cycles) for small string (36 length) took: 1.130295753479004 seconds.
KMS encrypt/decrypt operation (100 cycles) for big string (3600 length) took: 1.3349699974060059 seconds.

- RUN 4
KMS encrypt/decrypt operation (100 cycles) for small string (36 length) took: 1.1800289154052734 seconds.
KMS encrypt/decrypt operation (100 cycles) for big string (3600 length) took: 1.3672645092010498 seconds.
```

#### Results:

On Lambda function, 128 MB RAM.

```shell
- RUN 1
KMS encrypt/decrypt operation (100 cycles) for small string (36 length) took: 5.7690300941467285 seconds.
KMS encrypt/decrypt operation (100 cycles) for big string (3600 length) took: 5.800090551376343 seconds.

- RUN 2
KMS encrypt/decrypt operation (100 cycles) for small string (36 length) took: 5.720337152481079 seconds.
KMS encrypt/decrypt operation (100 cycles) for big string (3600 length) took: 5.759984731674194 seconds.

- RUN 3
KMS encrypt/decrypt operation (100 cycles) for small string (36 length) took: 5.695910215377808 seconds.
KMS encrypt/decrypt operation (100 cycles) for big string (3600 length) took: 5.699832201004028 seconds.

- RUN 4
KMS encrypt/decrypt operation (100 cycles) for small string (36 length) took: 5.558764934539795 seconds.
KMS encrypt/decrypt operation (100 cycles) for big string (3600 length) took: 5.639872312545776 seconds.
```

#### Conclusion

Regardless of the environment bigger object to encrypt takes more time.
However, the difference is quite negligible between a small object
(36 characters), and a 100 times bigger object (3600 characters).

---

### Single operation length experiment.

The experiment checks what is the average duration of KMS encryption and 
KMS decryption operations.

To run an experiment:
```shell
python experiments/single_operation_length_experiment.py
```

#### Results:

On MacBook PRO, 2021, Intel processor, 16GB RAM, 1Gbps WiFi network.

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

#### Results:

On Lambda function, 10240 MB (~10GB) RAM.

```shell
- RUN 1
KMS encrypt operation on average took 0.006828951835632324 seconds.
KMS decrypt operation on average took 0.006768898963928223 seconds.

- RUN 2
KMS encrypt operation on average took 0.006952357292175293 seconds.
KMS decrypt operation on average took 0.006755657196044922 seconds.

- RUN 3
KMS encrypt operation on average took 0.0068153834342956545 seconds.
KMS decrypt operation on average took 0.00627129077911377 seconds.

- RUN 4
KMS encrypt operation on average took 0.006536862850189209 seconds.
KMS decrypt operation on average took 0.007810392379760742 seconds.
```

#### Results:

On Lambda function, 128 MB RAM.

```shell
- RUN 1
KMS encrypt operation on average took 0.028796486854553223 seconds.
KMS decrypt operation on average took 0.029197382926940917 seconds.

- RUN 2
KMS encrypt operation on average took 0.029590015411376954 seconds.
KMS decrypt operation on average took 0.029774458408355714 seconds.

- RUN 3
KMS encrypt operation on average took 0.029198884963989258 seconds.
KMS decrypt operation on average took 0.028743078708648683 seconds.

- RUN 4
KMS encrypt operation on average took 0.029194183349609375 seconds.
KMS decrypt operation on average took 0.02918060302734375 seconds.
```

#### Conclusion

Firstly, we can conclude that there is no significant difference
between KMS encryption and KMS decryption operations.

Secondly, we can conclude that operations running inside AWS cloud
(via Lambda functions) is faster than running on a local computer /
network.

Thirdly, Lambda functions with more RAM have higher CPU count and
higher network bandwidth. That is why we see significantly faster 
operation times with Lambda functions that have 10240 MB RAM, than
Lambda functions that have 128 MB RAM.
