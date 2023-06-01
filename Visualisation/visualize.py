import open3d


def visualize(new_pcd):

    # new_pcd = open3d.geometry.PointCloud()
    # new_pcd.points = open3d.utility.Vector3dVector(points)
    open3d.visualization.draw_geometries([new_pcd])
