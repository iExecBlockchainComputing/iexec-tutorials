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
2019-11-18 16:35:49.328320: I tensorflow/stream_executor/platform/default/dso_loader.cc:42] Successfully opened dynamic library libcublas.so.10.0
2019-11-18 16:35:50.431366: I tensorflow/stream_executor/platform/default/dso_loader.cc:42] Successfully opened dynamic library libcudnn.so.7
2019-11-18 16:35:54.892618: precision @ 1 = 0.862
TF version: 1.14.0
2051 sec
Formatted:
0:34:11

``

###More information about the data

Check the following link for more details

``
https://www.cs.toronto.edu/~kriz/cifar.html
``

``
https://en.wikipedia.org/wiki/CIFAR-10
``

Build your app:

``
docker build -t YOUR_NAME/cifar_tensorflow .
``

If you have access to gpu nvidia on your machine

``
docker build -t YOUR_NAME/cifar_tensorflow N
``

N is the number of batches (i.e nb of iterations), increase N will increase the model and increase the time to solution.

then register your app on iexec and publish apporder by following the step by step section
at `https://docs.iex.ec/appprovider.html#set-up-you-app`


