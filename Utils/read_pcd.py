import scipy.io
import io
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

    return point_cloud