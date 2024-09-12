#!/usr/bin/env python3

import argparse
import json
import uuid

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Deploy manager. Processes configs and certs")
    parser.add_argument('-t', "--tag", type=str, default=None, help="tag in config")


    group = parser.add_mutually_exclusive_group()
    group.add_argument('-n', "--number", type=int, help="number of new ids [for tags only]")
    group.add_argument('-r', "--range", type=str, help="range of new ids "
                                                                    "in \"from,to\" format [for tags only]")

    args = parser.parse_args()
    args.from_idx = 0
    args.to_idx = 0
    if args.number:
        args.to_idx = args.number
    elif args.range:
        args.from_idx, args.to_idx = [int(e) for e in args.range.strip().split(',')]
        if args.from_idx >= args.to_idx:
            sys.stderr.write("Invalid range. Expected from,to format where from < to, received {}"\
                                .format(repr(args.range)))
            exit(1)

    return args


def generate_guides(base_tag, from_idx=0, to_idx=1):
    if not base_tag:
        base_tag = "random_user_{}".format(str(uuid.uuid4())[:4])

    guides = []
    for idx in range(from_idx, to_idx):
        tag = base_tag if to_idx - to_idx == 1 else f"{base_tag}_{idx}"
        guide = {
            "tag": tag,
            "id": str(uuid.uuid4()),
            "alterId": 64
        }
        guides.append(guide)

    return json.dumps(guides, indent=4)


def main():
    args = parse_args()
    json_output = generate_guides(args.tag, args.from_idx, args.to_idx)
    print(json_output)

if __name__ == "__main__":
    main()
