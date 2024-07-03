import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')
from argparse import ArgumentParser
from poselib.skeleton.skeleton3d import SkeletonMotion
from poselib.visualization.common import plot_skeleton_motion_interactive


if __name__ == "__main__":
    args = ArgumentParser(description="NPY format Skeleton Motion Player")
    args.add_argument("npy", type=str, help="Path to the npy file containing the skeleton motion.")
    args = args.parse_args()

    if not args.npy:
        raise ValueError("Please provide the path to the npy file containing the skeleton motion.")

    motion = SkeletonMotion.from_file(args.npy)
    plot_skeleton_motion_interactive(motion)
