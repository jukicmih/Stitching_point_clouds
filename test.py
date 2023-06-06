# point to point - odrežemo oba pointclouda oko centra mixanog pointclouda
# dakle fja prima rezani point cloud1 i drugi isto rezani oko centra mixanog pointclouda

#isto i za point to plane
#za emd

import open3d
import os
import numpy as np
import matplotlib.pyplot as plt


from Algorithms._calculate_earth_mover_distances_from_point_clouds import \
    _calculate_earth_mover_distances_from_point_clouds
from Utils.read_pcd import read_pcd
from Algorithms.get_max_point_distance import get_max_point_distance
from Algorithms.point_2_point import point_2_point
# from open3d.geometry import estimate_normals
from Visualisation.visualize import visualize
from Utils.pcd_cutter import _cull_point_cloud_in_torus_around_center


username = "MirnaL"
file_path = "C:/Users/" + username + "/Desktop/quality_check/CCHA0B2202029903_SE-SNA170_20220714_185346_BAD/Lidar/"
mat_files = [f for f in os.listdir(file_path) if f.endswith(".mat")]
print(mat_files)

rmse_res = []
p2l_res = []
emd_res = []
downsample_rate = 50
step = 100
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

    pc1_cut = _cull_point_cloud_in_torus_around_center(point_cloud1, new_pcd.get_center(), 2, 10)
    pc2_cut = _cull_point_cloud_in_torus_around_center(point_cloud2, new_pcd.get_center(), 2, 10)
    del point_cloud1, point_cloud2

    del one_array
    visualize(pc1_cut)
    visualize(pc2_cut)


    pc1_cut.estimate_normals()
    p2l_dist = get_max_point_distance(pc1_cut.points, pc2_cut.points, pc1_cut.normals)
    suma = np.sum(p2l_dist*p2l_dist)
    p2l_res.append(suma)
    print("Point to plane:", suma)
    downsampled_source1 = pc1_cut.points[0::downsample_rate] #gledamo svaku stotu tocku
    downsampled_source2 = pc2_cut.points[0::downsample_rate]

    new_pcd1 = open3d.geometry.PointCloud()
    new_pcd1.points = open3d.utility.Vector3dVector(downsampled_source1)
    new_pcd2 = open3d.geometry.PointCloud()
    new_pcd2.points = open3d.utility.Vector3dVector(downsampled_source2)

    suma1 = _calculate_earth_mover_distances_from_point_clouds(np.asarray(new_pcd1.points), np.asarray(new_pcd2.points))
    emd_res.append(suma1)
    print("earth mover's distance:", suma1)

    trans_init = np.eye(4)# ne kuzim zasto mora biti 4
    reg_p2p = point_2_point(new_pcd1, new_pcd2, trans_init, 0.02, 200)
    rmse_res.append(reg_p2p.inlier_rmse)
    print("point to point:", reg_p2p.inlier_rmse)
    del new_pcd1, new_pcd2


plt.figure()
plt.title("point to plane, E")
plt.plot(p2l_res, 'g')
plt.show()

plt.figure()
plt.title("earth mover's distance")
plt.plot(emd_res, 'r')
plt.show()

plt.figure()
plt.title("point to point, RMSE")
plt.plot(rmse_res, 'b')
plt.show()



# normals = point_cloud1.estimate_normals()
# print(point_cloud1.has_normals())
# visualize(point_cloud1)
#
# p2l_dist = get_max_point_distance(point_cloud1.points, point_cloud2.points, point_cloud1.normals)
# print(p2l_dist)
# print(len(p2l_dist))
# suma = 0
# # for i in range(len(p2l_dist)):
# #     suma += p2l_dist(i)^2
#
# suma = np.sum(p2l_dist*p2l_dist)
# print("Point to plane:")
# print(suma)
#
# temp_array1 = np.asarray(point_cloud1.points)
# temp_array2 = np.asarray(point_cloud2.points)
#
# print(temp_array1.shape)
# print(temp_array2.shape)

#downsampleiranje
# downsample_rate = 100
# downsampled_source1 = point_cloud1.points[0::downsample_rate] #gledamo svaku desetu tocku
# downsampled_source2 = point_cloud2.points[0::downsample_rate]
#
# new_pcd1 = open3d.geometry.PointCloud()
# new_pcd1.points = open3d.utility.Vector3dVector(downsampled_source1)
# new_pcd2 = open3d.geometry.PointCloud()
# new_pcd2.points = open3d.utility.Vector3dVector(downsampled_source2)

# suma1 = _calculate_earth_mover_distances_from_point_clouds(np.asarray(new_pcd1.points), np.asarray(new_pcd2.points))
# print(suma1)

# center = point_cloud1.get_center()
# print(center)
# print(center.shape)
# center_R = np.reshape(center, (1, 3))
#
# print(center_R)
# print(center_R.shape)
#
# isti_array = np.empty((100, 3))
# for i in range(100):
#     isti_array[i, :] = center_R
#
# print(isti_array)
# # new_pcd = open3d.geometry.PointCloud()
# # new_pcd.points = open3d.utility.Vector3dVector(isti_array)
# new_pcd = open3d.geometry.PointCloud(open3d.utility.Vector3dVector(isti_array))
# visualize(new_pcd)
#
# pcd = open3d.geometry.PointCloud()
# pcd.points = open3d.utility.Vector3dVector(np.array(new_pcd.points) + np.array([0, 5, 0]))
#
# open3d.visualization.draw_geometries([new_pcd, pcd])
#
# # mesh = open3d.geometry.create_mesh_coordinate_frame(origin = one_array)
# #visualize(one_array)
# #trans_init = I
