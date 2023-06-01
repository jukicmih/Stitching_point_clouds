from scipy.spatial.distance import cdist
from scipy.optimize import linear_sum_assignment


def calculate_earth_mover_distances_from_point_clouds(point_cloud_1, point_cloud_2):
    distance = cdist(point_cloud_1, point_cloud_2)
         # racuna euklidske udaljenosti izmedu tocaka iz dva point clouda i sprema ih u matricu distance t.d.
         #   distance(i, j) = ||point_cloud_1(i) - point_cloud_2(j)||_2

    assignment = linear_sum_assignment(distance)
        # povezuje tocke iz pc 1 sa tockama iz pc 2 tako da je suma udaljenosti minimalna
        # assignment je tipa [array, array], prvi array su indeksi redaka, drugi indeksi stupaca - vidi dokumentaciju

    return float(distance[assignment].sum() / min(len(point_cloud_1), len(point_cloud_2)))
        # vraca kao prosjecnu udaljenost point cloudova
