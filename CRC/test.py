#!/usr/bin/env python
import sys
import cv2
import time
import torch
import tensorflow as tf

print(" >> Python version:\t", sys.version)
print(" >> Tensorflow version:\t", tf.__version__)
print(" >> PyTorch version:\t", torch.__version__)
print(" >> OpenCV version:\t", cv2.__version__)
print()
print(" >> CUDA available?\t{}".format(torch.cuda.is_available()))
for d in range(torch.cuda.device_count()):
    print("\tGPU {}: {}".format(d, torch.cuda.get_device_name(d)))

#print(tf.test.gpu_device_name())

sleeptime = 10
print("Sleeping {}s...".format(sleeptime))
time.sleep(sleeptime)

print("FINISHED!! HURRAY :D")
