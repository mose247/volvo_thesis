import os
from utils.mcap_read import *


# TOPICS 
LIDAR_FRONT = "/env/input/lidar-front"
LIDAR_REAR = "/env/input/lidar-rear"
GNSS_POSE = "/env/input/gnss-pose"


def main():

    # Get the path where to reach the raw data
    absolute_path = os.path.dirname("thesis") 
    relative_path = "data/environment_data_2023-02-21T13-50-49-GMT_1.mcap"
    full_path = os.path.join(absolute_path, relative_path)

    # Create generator objects to retrieve the points at the different timestamps
    front = get_lidar_data(full_path, LIDAR_FRONT)
    rear = get_lidar_data(full_path, LIDAR_REAR)
    #gnss = get_gnss_data(full_path, GNSS_POSE)


    (timestamp, data) = next(front)
        
    points = np.array(data)
    xyz = points[:,:3]
        
    print(f"Timestamp: {timestamp} ns")
    print(f"Points: \n {points}")



if __name__ == '__main__':
    main()