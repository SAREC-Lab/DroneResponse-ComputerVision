# Getting Started with CRC 

*Shoutout to my friend Lucas, the CS Magician, for the great instructions and rad tips to model off of! :)* 

While computer vision models can be trained on a CPU, training on a GPU will allow the training to run quicker and more efficiently. This is where **CRC** comes in! Since everyone may not have access to a GPU directly, we will be using **CRC** for all of our vision model training purposes. 

## Operating Systems 

### MAC Homies 

If you want to use a GUI then then you will probably need to downloa da a program like [Fastx](https://docs.crc.nd.edu/general_pages/f/fastx.html#fastx) first! After this is complete, you can simply proceed with the next steps. 

### Windows Homies 

I recommend getting an SSH client like **MobaXterm** to SSH into CRC resources. Follow these [instructions](https://docs.crc.nd.edu/general_pages/m/mobaxterm.html) to get started. Or you could opt to completely replace the operating system if you please or use the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10). 

> Your life would be a lot easier with Linux, but I support you and your quest for challenge if you want to stick it out with Windows! 

## File Transfers 

You will probably need to transfer files from your local machines to the CRC filesystem space and vice versa. While there are different file transfer clients, anything requiring the use of a GUI is **SO SLOW** and not fun at all to use, especially when you are trying to upload data. 

I recommend mounting the CRC drive locally to your machine to make life easier and have included linux based instructions below. If it proves to be too difficult to mount the CRC drive locally, no worries, we will make it work! If it is not mounted properly, it may end up causing you more headaches anyways. 

### Mounting CRC Drive Locally 

Do the following in your local machine, not in CRC: 

```sh
# create variables
NETID=<your_notre_dame_net_id>
MOUNTPOINT=/mnt/crc
initial="$(echo $NETID | head -c 1)"

# create dir
mkdir -p $MOUNTPOINT

# mount file system
sshfs -o allow_other -C $NETID@crcfe02.crc.nd.edu:/ $MOUNTPOINT

# navigate to user home
cd $MOUNTPOINT/afs/crc.nd.edu/user/$initial/$NETID/
```

If mounted locally you can do things like version control easily: 

```sh
# from your local machine, mount the CRC drive and run:
cd $MOUNTPOINT/afs/crc.nd.edu/user/$initial/$NETID/Private/
git clone git@github.com:username/project.git my_project

# then you can open the repository with your
# text editor / IDE of choice (e.g. VS Code):
code my_project

```
The code changes will be updated to the CRC machines in real time. 

[Follow these instructions if you would like to mount the CRC driver locally for a different OS](https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh)

### File Transfer Clients 

If you prefer to use a client, which is the less efficient but safe option, then feel free to follow the suggestions under **File Transfers** [here](https://docs.crc.nd.edu/new_user/quick_start.html).


## Cluster Computing Format

In case some of the terminology sounds weird I have included the diagram from the [Quick Start Guide](https://docs.crc.nd.edu/new_user/quick_start.html) below: 
```
                                                 Cluster
                                         +---+---+---+---+---+---+
               +---->+-------+           |   |   |   |   |   |   |
               |     | Front |           |   |   |   |   |   |   |
               |     |  End  |           |   |   |   |   |   |   |
               |     +---+---+           |   |   |   |   |   |   |
Internet       |         |               +---+---+-------+---+---+
Connection     |         |                           ^
               |         |                           |
               |         +---------------------------+
           ____|______
           \+--+------+
           \|Personal |
           \|Computer |
           \+---------+
```

## Common Tasks 

### Connect to front-end node 

```sh 
# from your local machine, connect to a CRC front-end node 
ssh -CY <YOUR-NETID>@crcfe02.crc.nd.edu
```

Make sure to use your Notre Dame NetID 

### Installing Dependencies 

Your file system is mounted on the machine to where you will submit your jobs (i.e.,training a vision model), so you can prepare your environment on the front-end node (`crcfe02.crc.nd.ed`) and then later submit the job to the **cluster** to be completed. 

Since these are vision tasks, I suggest creating and preparing a conda environment that you can use later to run your program. I have included a script that can do this for you `create_env.sh`. You will only need to run it once (unless you add more dependencies to the project). 

```sh 
# if you do not have access to the files, 
# from a front-end node, git clone the repo 
git clone https://github.com/SAREC-Lab/DroneResponse-ComputerVision.git

# run the create_env.sh script 
./create_env.sh
```
If you get a `Permission denied` error then do `chmod 755 create_env.sh` and then run the script

### Interactive Shell 

From a front-end node you can spawn an interactive shell inside the cluster, so you can quickly experiment code with the GPUs.

This is **NOT** for training your models, only for prototyping! Anything that is "heavy duty" should be a job that is submitted to the queue which is explained below. If the task will take longer than an hour, then it should probably be submitted to the queue. 

```sh
# login to the GPU cluster
qrsh -q gpu -l gpu_card=0

# If your file system is mounted; you can
# navigate through the files, find and run your program:

conda activate DroneResponse
python test.py
```
If the file system is not mounted, then you will need to take the appropriate steps using a client to get the files into your CRC space to access and run. 

If all goes well, your output should look something like this: 

```sh 
 >> Python version:	 3.6.10 |Anaconda, Inc.| (default, May  8 2020, 02:54:21) 
[GCC 7.3.0]
 >> Tensorflow version:	 2.1.0
 >> PyTorch version:	 1.5.0
 >> OpenCV version:	 3.4.2

 >> CUDA available?	True
	GPU 0: GeForce GTX TITAN X
	GPU 1: GeForce GTX TITAN X
	GPU 2: GeForce GTX TITAN X
	GPU 3: GeForce GTX TITAN X
Sleeping 20s...
FINISHED!! HURRAY :D!
```

### Submitting Jobs

You can use `job_submit.sh` as a base script to create your own. Let's use it as an example.

Make sure to edit the file and replace `<your_net_id>` with your NetID. 

```sh
qsub job_submit.sh
```

### Checking Job Status

```sh
qstat -u <your_nd_net_id>
```

### Terminating Jobs

You can get your job ID with `qstat -u <your_nd_net_id>` and then run:

```sh
qdel <job_id>
```
### Execution Results

When you submit your job, you will see a file named like `my_job.o985324` with the outputs of your execution. If this file is empty, wait until your execution is finished.

The outputs of `qsub job_submit.sh` should look like this:

```sh
 >> Running on qa-rtx6k-044.crc.nd.edu
/opt/sge/crc/spool/qa-rtx6k-044/job_scripts/985324: line 16: module: command not found
/opt/sge/crc/spool/qa-rtx6k-044/job_scripts/985324: line 19: conda: command not found
 >> Python version:	 3.6.10 |Anaconda, Inc.| (default, May  8 2020, 02:54:21) 
[GCC 7.3.0]
 >> Tensorflow version:	 2.1.0
 >> PyTorch version:	 1.5.0
 >> OpenCV version:	 3.4.2

 >> CUDA available?	True
	GPU 0: Quadro RTX 6000
Sleeping 20s...
FINISHED!! HURRAY :D!
```

## Other Tasks

### Check disk storage

```sh
quota
# Quota for /afs/crc.nd.edu/user/n/netid
# Volume Name                   Quota      Used %Used   Partition
# u.netid                     1500 GB     15 GB    1%         30%
```
**If you were able to do all this, then props to you! :D You will be in good shape for training the computer vision models on CRC!** 

![Alt Text](https://4.bp.blogspot.com/-FL-5tsODN_4/WN_NN6QHJbI/AAAAAAAOVJs/xBcy7pPquVkgL-Q5qf-klPTpGGh87gmWwCLcB/s1600/AW401359_05.gif)
