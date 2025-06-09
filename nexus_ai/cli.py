import argparse
from .model import Network


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute network score")
    parser.add_argument("data", help="Path to network JSON file")
    args = parser.parse_args()
    network = Network.from_json(args.data)
    print("Nodes:", ", ".join(network.nodes))
    print(f"Network score: {network.network_score():.2f}")


if __name__ == "__main__":
    main()
