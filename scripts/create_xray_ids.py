#!/usr/bin/env python3

import argparse
import json
import uuid

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Deploy manager. Processes configs and certs")
    parser.add_argument('-n', "--number", type=int, default=1, help="number of new ids")
    parser.add_argument('-t', "--tag", type=str, default=None, help="tag in config")
    args = parser.parse_args()
    return args


def generate_guides(n, base_tag):
    if not base_tag:
        base_tag = "random_user_{}".format(str(uuid.uuid4())[:4])

    guides = []
    for idx in range(n):
        tag = base_tag if n == 1 else f"{base_tag}_{idx}"
        guide = {
            "tag": tag,
            "id": str(uuid.uuid4()),
            "alterId": 64
        }
        guides.append(guide)

    return json.dumps(guides, indent=4)


def main():
    args = parse_args()
    json_output = generate_guides(args.number, args.tag)
    print(json_output)

if __name__ == "__main__":
    main()
