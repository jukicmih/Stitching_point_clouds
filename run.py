import os
import numpy as np
from Utils.pcd_cutter import _cull_point_cloud_in_torus_around_center
from Algorithms._calculate_earth_mover_distances_from_point_clouds import _calculate_earth_mover_distances_from_point_clouds
from Visualisation.visualize import visualize
from Utils.read_pcd import read_pcd
from Algorithms.get_max_point_distance import get_max_point_distance
import open3d.geometry

username = "MihaelaJ"
#file_path = "C:/Users/" + username + "/Desktop/zadatak/lidar_sample"
file_path = "C:/Users/" + username + "/Desktop/quality_check/CCHA0B2202029903_SE-SNA170_20220714_230543_VERY_GOOD/Lidar/"

mat_files = [f for f in os.listdir(file_path) if f.endswith(".mat")]

step = 20   # uzimamo svaki dvadeseti file
for i in range(0, len(mat_files) - step, step):
    one_array = np.empty((0, 3))
    point_cloud1 = read_pcd(file_path, mat_files[i])
    visualize(point_cloud1)
    point_cloud2 = read_pcd(file_path, mat_files[i + step])
    visualize(point_cloud2)
    one_array = np.vstack((one_array, point_cloud1.points))
    one_array = np.vstack((one_array, point_cloud2.points))
    new_pcd = open3d.geometry.PointCloud()
    new_pcd.points = open3d.utility.Vector3dVector(one_array)
    visualize(new_pcd)
    point_cloud1.estimate_normals()
    p2l_dist = get_max_point_distance(point_cloud1.points, point_cloud2.points, point_cloud1.normals)
    suma = 0
    suma = np.sum( p2l_dist * p2l_dist )
    print("point to plane : ", suma)


# one_array = np.empty((0, 3))
#   pcd = read_pcd("C:/Users/MihaelaJ/Desktop", "CCHA0B2202029903_SE-SNA170_20220714_194416_10_10_1341863041177833_agg.mat")

# j = 0
# for filename in mat_files:
#     j += 1
#     if(j == 1):
#         point_cloud = read_pcd(file_path, filename)
#         #pcd = open3d.io.read_point_cloud(file_path + filename)
#     if(j == 2):
#         point_cloud2 = read_pcd(file_path, filename)
#         #pcd2 = open3d.io.read_point_cloud(file_path + filename)
#         break
#     # one_array = np.vstack((one_array, point_cloud))

#
# normals = point_cloud.estimate_normals()
# print(point_cloud.has_normals())
# visualize(point_cloud)

# p2l_dist = get_max_point_distance(point_cloud.points, point_cloud2.points, point_cloud.normals)
#
# suma = 0
# suma = np.sum( p2l_dist * p2l_dist )
# print(suma)
#
# centar = point_cloud.get_center()
# print(centar)


# cut_pcd = _cull_point_cloud_in_torus_around_center(point_cloud, centar, 15, 20)
# cut_pcd.points = open3d.utility.Vector3dVector(np.array(cut_pcd.points)+np.array([0, 50, 0]))
# open3d.visualization.draw_geometries([point_cloud, cut_pcd])
# visualize(cut_pcd)

# downsample_rate = 50
# downsampled_source = point_cloud.points[0::downsample_rate]
# downsampled_source2 = point_cloud2.points[0::downsample_rate]
#
# new_pcd = open3d.geometry.PointCloud()
# new_pcd.points = open3d.utility.Vector3dVector(downsampled_source)
# new_pcd2 = open3d.geometry.PointCloud()
# new_pcd2.points = open3d.utility.Vector3dVector(downsampled_source2)

#udaljenost = _calculate_earth_mover_distances_from_point_clouds(np.asarray(new_pcd.points), np.asarray(new_pcd2.points))
#print(udaljenost)