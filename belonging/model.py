import json
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Community:
    members: List[str]
    connections: List[Tuple[str, str]]

    @classmethod
    def from_json(cls, path: str) -> 'Community':
        """Load community data from a JSON file."""
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        connections = [tuple(pair) for pair in data.get('connections', [])]
        return cls(members=data.get('members', []), connections=connections)

    def belonging_score(self) -> float:
        """Return a simple connection density score between 0 and 1.

        Duplicate or reversed connections are ignored so the score never
        exceeds 1.0.
        """
        n = len(self.members)
        if n < 2:
            return 0.0
        max_connections = n * (n - 1) // 2

        unique_connections = {
            frozenset(pair)
            for pair in self.connections
            if len(pair) == 2 and pair[0] != pair[1]
        }
        actual_connections = len(unique_connections)

        return actual_connections / max_connections
