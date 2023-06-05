def visualize(point_cloud):

    import open3d

    mesh_frame = open3d.geometry.TriangleMesh.create_coordinate_frame(size=10,
                                                                      origin=point_cloud.get_center())
    open3d.visualization.draw_geometries([point_cloud, mesh_frame])


