# Written By: Benjamin Goldberg
#
# This code will decode the H.264 byte stream into a viewable video format
# For now, using the direct byte stream from hardware_encode.py



import subprocess
import hardware_encode as he

byte_stream = he.out
