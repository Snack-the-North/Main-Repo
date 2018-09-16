# *****************************************************
#                                                    *
# Copyright 2018 Amazon.com, Inc. or its affiliates. *
# All Rights Reserved.                               *
#                                                    *
# *****************************************************
""" A sample lambda for face detection"""
import json
import os

import awscam
import cv2
import numpy as np


c
def main():
    while True:
        # Get a frame from the video stream
        ret, frame = awscam.getLastFrame()
        if not ret:
            raise Exception('Failed to get frame from the stream')

        cv2.imshow('Raw Input', frame)

if __name__ == '__main__':
    main()
