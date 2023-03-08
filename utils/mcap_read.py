import json
import base64
import struct
import numpy as np

import mcap
from mcap.reader import make_reader

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def get_lidar_data(file, topic):
    with open(file, "rb") as f:
        reader = make_reader(f)
        for schema, channel, message in reader.iter_messages(topic):
            timestamp = message.log_time
            enc = json.loads(message.data)              # get a PointCloud message stored into a json file and convert it in a python dictionary
            dec = base64.b64decode(enc['data'])         # decode Points string using base64 decoding
            uint8_array = np.frombuffer(dec, dtype=np.uint8)
            res = struct.iter_unpack('<ffff', uint8_array)
            yield (timestamp, list(res))


def get_gnss_data(file, topic):
    with open(file, "rb") as f:
        reader = make_reader(f)
        for schema, channel, message in reader.iter_messages(topic):
            timestamp = message.log_time
            enc = json.loads(message.data)
            yield (timestamp, enc)