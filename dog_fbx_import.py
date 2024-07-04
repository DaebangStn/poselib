import torch
from argparse import ArgumentParser

from poselib.skeleton.skeleton3d import SkeletonMotion, SkeletonState
from poselib.visualization.common import plot_skeleton_motion_interactive


if __name__ == "__main__":
    args = ArgumentParser(description="FBX to Skeleton Motion NPY Converter")
    args.add_argument("fbx", type=str, help="Path to the input fbx file")
    args.add_argument("npz", type=str, help="Path to the output npz file")
    args.add_argument("--scale", type=float, help="Scalar value for mjcf model", default=0.012)
    args.add_argument("--root", type=str, help="Root joint name.", default="Hips")
    args.add_argument("--vis", action='store_true', help="Visualize the skeleton motion.")
    args = args.parse_args()

    print(f'Converting {args.fbx} to {args.npz}...')
    motion = SkeletonMotion.from_fbx(fbx_file_path=args.fbx, root_joint=args.root, fps=60)

    # Suppose at least one point is on the ground (jump is not allowed)
    min_h, _ = torch.min(motion.global_translation[..., 2:3], dim=1)
    # allow jump
    # min_h = torch.min(motion.global_translation[..., 2:3])

    root_trans = motion.root_translation
    root_trans[:, 2:3] -= min_h
    root_trans *= args.scale
    root_trans[:, 2] += 0.05  # prevent penetration

    sk_state = SkeletonState.from_rotation_and_root_translation(motion.skeleton_tree, motion.local_rotation, root_trans)
    motion_corrected = SkeletonMotion.from_skeleton_state(sk_state, fps=motion.fps)

    motion_corrected.to_file(args.npz)
    if args.vis:
        plot_skeleton_motion_interactive(motion_corrected)

    print('Done.')
