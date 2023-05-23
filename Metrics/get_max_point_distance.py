from scipy.spatial import cKDTree
import numpy as np

def get_max_point_distance(source_points, target_points, source_normals):
    kd_tree = cKDTree(source_points)
    point_to_point_distances, next_point_indices = kd_tree.query(target_points, k=1)
    source_normals_np = np.asarray(source_normals)
    source_points_np = np.asarray(source_points)
    point_to_plane_distance = np.abs(
        np.sum(
            source_normals_np[np.asarray(next_point_indices)]
            * (source_points_np[np.asarray(next_point_indices)] - target_points),
            axis=-1,
        )
    )
    return point_to_plane_distance
