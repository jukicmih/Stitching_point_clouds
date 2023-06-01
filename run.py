import scipy.io
import io
import os
import numpy as np
import open3d

from Utils.pcd_cutter import _cull_point_cloud_in_torus_around_center
from Metrics.calculate_earth_mover_distances_from_point_clouds import calculate_earth_mover_distances_from_point_clouds
from Visualisation.visualize import visualize
from Utils.read_pcd import read_pcd
from Metrics.get_max_point_distance import get_max_point_distance
import open3d.geometry

username = "MihaelaJ"
#file_path = "C:/Users/" + username + "/Desktop/zadatak/lidar_sample"
file_path = "C:/Users/" + username + "/Desktop/quality_check/CCHA0B2202029903_SE-SNA170_20220714_230543_VERY_GOOD/Lidar/"

file_names = os.listdir(file_path)

mat_files = []
i = 0
for file in file_names:
    if file.endswith(".mat"):
        i += 1
        if i % 10 == 0:
            mat_files.insert(int(i/10), file)

#print(mat_files)

#one_array = np.empty((0, 3))
#pcd = read_pcd("C:/Users/MihaelaJ/Desktop", "CCHA0B2202029903_SE-SNA170_20220714_194416_10_10_1341863041177833_agg.mat")

# for filename in file_names:
j = 0
for filename in mat_files:
    j += 1
    if(j == 1):
        point_cloud = read_pcd(file_path, filename)
        #pcd = open3d.io.read_point_cloud(file_path + filename)
    if(j == 2):
        point_cloud2 = read_pcd(file_path, filename)
        #pcd2 = open3d.io.read_point_cloud(file_path + filename)
        break
    # one_array = np.vstack((one_array, point_cloud))

# print(one_array)

normals = point_cloud.estimate_normals()
print(point_cloud.has_normals())
visualize(point_cloud)

p2l_dist = get_max_point_distance(point_cloud.points, point_cloud2.points, point_cloud.normals)

suma = 0
suma = np.sum( p2l_dist * p2l_dist )
print(suma)

centar = point_cloud.get_center()
#udaljenost = calculate_earth_mover_distances_from_point_clouds(np.asarray(point_cloud.points), np.asarray(point_cloud2.points))

# cut_pcd = _cull_point_cloud_in_torus_around_center(point_cloud, centar, 18,20)
# cut_pcd.points = open3d.utility.Vector3dVector(np.array(cut_pcd.points)+np.array([0, 50, 0]))
#open3d.visualization.draw_geometries([point_cloud, cut_pcd])
# visualize(cut_pcd)
downsample_rate = 10
downsampled_source = point_cloud.points[0::downsample_rate]
downsampled_source = point_cloud2.points[0::downsample_rate]