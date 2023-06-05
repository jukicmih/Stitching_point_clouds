from scipy.spatial import cKDTree
import numpy as np


def get_max_point_distance(source_points, target_points, source_normals) :
    kd_tree = cKDTree(source_points)
        # kreira binarno stablo ?? pomocu kojeg lako nalazimo susjede neke tocke po udaljenosti
    point_to_point_distances, next_point_indices = kd_tree.query(target_points, k=1)
        # u kd_tree su nam spremljene tocke iz sourcea i sada pozivom funkcije query na target_points i uz k=1
        # dobivamo polje ptp_distances u kojem je za svaku tocku iz targeta!!! spremljeno k (tj jedna) najmanjih
        # udaljenosti izmedu njih i tocaka iz source-a, a indeksi tih tocaka(iz sourcea) su u next_point_indices
    source_normals_np = np.asarray(source_normals)

    source_points_np = np.asarray(source_points)
    point_to_plane_distance = np.abs(
        np.sum(
            source_normals_np[np.asarray(next_point_indices)]
            * (source_points_np[np.asarray(next_point_indices)] - target_points),
            axis=-1,
        )
    )
    # sada u ptldist imamo polje ciji su elementi oblika |(p-Tq)*n_p|, za p iz source-a, q(ili Tq?) iz target-a
    # izvan funkcije pretp da sumiramo kvadrate elemenata polja ptldist da bi dobili E(T) (funkciju cilja ptl icp-a)
    return point_to_plane_distance
