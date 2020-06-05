#!/usr/bin/env bash
#$ -M <your_net_id>@nd.edu  # Email to be notified (also put $ in front of this line)
#$ -m abe                   # Send mail when job begins, ends and aborts
#$ -q gpu	                # Specify job queue
#$ -l gpu_card=1            # Specify number of GPU cards to use - WE WILL USE ONE, BECAUSE WE ARE POLITE! :D 
#$ -N my_job                # Specify a job name

echo " >> Running on $(uname -n)"

# enable cluster anaconda
module load conda

# prepare shell for conda
conda init `ps -o comm= -p $$`
source ~/.bashrc

# activate conda environment
conda activate DroneResponse

# run your custom script
python test.py
