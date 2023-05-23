import scipy.io
import io
import os
import numpy as np
import open3d
from Visualisation.visualize import visualize
from Utils.read_pcd import read_pcd

username = "MihaelaJ"
file_path = "C:/Users/" + username + "/Desktop/zadatak/lidar_sample"
file_names = os.listdir(file_path)

one_array = np.empty((0, 3))

for filename in file_names:
    point_cloud = read_pcd(file_path, filename)
    one_array = np.vstack((one_array, point_cloud))

visualize(one_array)

