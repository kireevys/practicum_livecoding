import json
import pprint
from pathlib import Path

from parsing.models import Product


def file_to_model(file: Path) -> list[Product]:
    with open(file) as f:
        data = json.load(f)

    return [Product(**item) for item in data]


if __name__ == "__main__":
    pprint.pprint(file_to_model(Path("example.json")))
