import scipy.io
import io
import open3d

def read_pcd(file_path, filename):

    with io.open(file_path + "/" + filename, "rb") as f:
        try:
            mat_contents = scipy.io.loadmat(f)
        except (ValueError, OSError):
            _logger.error("Point cloud " + str(filename) + " is corrupted.")
        if "worldCoordinates" in mat_contents:
            point_cloud = mat_contents["worldCoordinates"]
        else:
            point_cloud = mat_contents["lidarPts"]

    new_pcd = open3d.geometry.PointCloud()
    new_pcd.points = open3d.utility.Vector3dVector(point_cloud)

    return new_pcd
