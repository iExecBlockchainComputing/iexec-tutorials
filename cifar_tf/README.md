##Goals

This dapp proposes to solve a recognizing images problem with **TensorFlow**,
 one of the first-in-classe open-source machine learning framework.   

The dapp is based on the advanced tutorial of the TensorFlow documentation.

For the details,
go to ``https://www.tensorflow.org/tutorials/deep_cnn``

It is designed to run into iExec backed by NVIDIA CUDA gpus to speed up the simulation.

The goal of this tutorial is to build a convolutional neural network (CNN) for recognizing images.

The model used in this CIFAR-10 tutorial is a multi-layer architecture consisting of alternating convolutions and nonlinearities. 

![alt text](images/graph_nn_1.png "Neural Network architecture")


It can evolve to multi-gpu test.

In this version, we limit the usage to a unique GPU.   


The evalution of the model after 100K iterations reaches 86%.

``
2018-02-23 15:57:01.093012: precision @ 1 = 0.862
``

Elapsed time for 100K  iterations is xxx min

###More information about the data

Check the following link for more details

``
https://www.cs.toronto.edu/~kriz/cifar.html
``

``
https://en.wikipedia.org/wiki/CIFAR-10
``


###start nvidia docker images

`sudo docker run --runtime=nvidia --rm nvidia/cuda hostname`

#start interactive 

```
sudo docker run --tty --interactive --runtime=nvidia --rm test
```

```
sudo docker run --tty -v $(pwd):/host -w /host --interactive --runtime=nvidia --rm test 
```
