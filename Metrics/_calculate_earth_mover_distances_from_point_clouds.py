from scipy.spatial.distance import cdist
from scipy.optimize import linear_sum_assignment


def _calculate_earth_mover_distances_from_point_clouds(point_cloud_1, point_cloud_2):
    distance = cdist(point_cloud_1, point_cloud_2)
    # calculates a distance matrix where
    # distance(i,j) = metric_dist(point_cloud_1(i),  point_cloud_2(j))

    assignment = linear_sum_assignment(distance)
    #  returns an array of row indices and one of corresponding column indices giving the optimal assignment, i.e.
    #  for every element in point_cloud_1 with index i, function finds the element in point_cloud_2 with index j
    #  s.t. distance(i,j) is least possible, but function is injective

    return float(distance[assignment].sum() / min(len(point_cloud_1), len(point_cloud_2)))
