import open3d


def point_2_plane(source, target, trans_init, threshold, max_it):

    reg_p2l = open3d.pipelines.registration.registration_icp(
        source, target, threshold, trans_init,
        open3d.pipelines.registration.TransformationEstimationPointToPlane(),
        open3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=max_it))

    return reg_p2l