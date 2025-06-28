import json
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Network:
    nodes: List[str]
    links: List[Tuple[str, str]]

    @classmethod
    def from_json(cls, path: str) -> 'Network':
        """Load network data from a JSON file."""
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        links = [tuple(pair) for pair in data.get('links', [])]
        return cls(nodes=data.get('nodes', []), links=links)

    def network_score(self) -> float:
        """Return a simple link density score between 0 and 1.

        Duplicate or reversed links are ignored so the score never exceeds
        1.0.
        """
        n = len(self.nodes)
        if n < 2:
            return 0.0
        max_links = n * (n - 1) // 2

        unique_links = {
            frozenset(pair)
            for pair in self.links
            if len(pair) == 2 and pair[0] != pair[1]
        }
        actual_links = len(unique_links)

        return actual_links / max_links
