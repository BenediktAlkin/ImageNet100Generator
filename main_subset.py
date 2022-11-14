import argparse

from imagenet_subset_generator import generate_subset, VERSIONS


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in1k_path", required=True, help="path to the directory where imagenet is stored")
    parser.add_argument("--out_path", required=True, help="path to the directory where imagenet is stored")
    parser.add_argument("--version", choices=VERSIONS, help="use predefined classes from a popular version")
    parser.add_argument("--train", action="store_true", help="generate the train dataset")
    parser.add_argument("--val", action="store_true", help="generate the val dataset")
    return parser.parse_args()


if __name__ == "__main__":
    generate_subset(**parse_args().__dict__)
