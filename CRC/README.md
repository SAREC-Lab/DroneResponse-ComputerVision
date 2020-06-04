# Getting Started with CRC 

While computer vision models can be trained on a CPU, training on a GPU will allow the training to run quicker and more efficiently. This is where **CRC** comes in! Since everyone may not have access to a GPU directly, we will be using **CRC** for all of our vision model training purposes. 

## Common Tasks 

### Connect to front-end node 

```sh 
# from your local machine, connect to a CRC front-end node 
ssh -CY <YOUR-NETID>@crcfe02.crc.nd.edu
```

Make sure to use your Notre Dame NetID 

### Installing Dependencies 

Your file system is mounted on the machine to where you will submit your jobs (i.e.,training a vision model), so you can prepare your environment on the front-end node ('crcfe02.crc.nd.ed`) and then later submit the job to be completed. 

Since these are vision tasks, I suggest creating and preparing a conda environment that you can use later to run your program. You will only need to run it once (unless you add more dependencies to the project). 

