import argparse
from .model import Community


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute community belonging score")
    parser.add_argument("data", help="Path to community JSON file")
    args = parser.parse_args()
    community = Community.from_json(args.data)
    print("Members:", ", ".join(community.members))
    print(f"Belonging score: {community.belonging_score():.2f}")


if __name__ == "__main__":
    main()
