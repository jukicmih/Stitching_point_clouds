import open3d
import numpy as np


def _cull_point_cloud_in_torus_around_center(
    point_cloud: open3d.geometry.PointCloud,
    center: tuple[float, float, float],
    radius_1: float,
    radius_2: float,) -> open3d.geometry.PointCloud:
    point_cloud_as_array = np.asarray(point_cloud.points)
    final_point_cloud_array = []
    for point in point_cloud_as_array:
        point_x = point[0] - center[0]
        point_y = point[1] - center[1]
        point_z = point[2] - center[2]

        if radius_2 * radius_2 > point_x * point_x + point_z * point_z > radius_1 * radius_1:
            print( point_z * point_z)
            final_point_cloud_array.append(point)
    return open3d.geometry.PointCloud(open3d.utility.Vector3dVector(final_point_cloud_array))

