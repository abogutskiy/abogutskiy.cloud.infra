#!/usr/bin/env python3

import argparse
import json
import grp
import os
import pwd
import shutil
import tarfile

from typing import Callable, Dict, List, Union, Optional

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Deploy manager. Processes configs and certs")
    parser.add_argument("--config", required=True, type=str, help="Path to deploy config")
    parser.add_argument("--configs-dir", type=str, default=None,
                        help="Path to configs dir. [default = dirname(config)]")
    args = parser.parse_args()

    if args.configs_dir is None:
        args.configs_dir = os.path.dirname(os.path.abspath(args.config))
    with open(args.config, 'r') as f:
        args.config = json.loads(f.read())

    return args

def traverse_and_apply(path: str, func: Callable[[str], None],
                       with_dirs: bool = False):
    for root, dirs, files in os.walk(path):
        for name in files:
            func(os.path.join(root, name))
        for name in dirs:
            path = os.path.join(root, name)
            func(path)
            traverse_and_apply(path, func, with_dirs)

def set_owner(destination: str, owner: str, with_folder: bool = False) -> None:
    user, group = owner.split(":")
    uid = pwd.getpwnam(user).pw_uid
    gid = grp.getgrnam(group).gr_gid

    if with_folder:
        os.chown(destination, uid, gid)

    traverse_and_apply(destination, lambda p: os.chown(p, uid, guid), True)

def set_permissions(destination: str, permissions: int, with_folder: bool = False) -> None:
    if with_folder:
        os.chmod(destination, permissions)

    traverse_and_apply(destination, lambda p: os.chmod(p, permissions), True)

def copy(source: str, destination: str) -> None:
    if not os.path.exists(source):
        raise Exception("source path doesn't exist {}".format(source))

    if os.path.isfile(source):
        shutil.copy(source, destination)
    elif os.path.isdir(source):
        shutil.copytree(source, destination)
    else:
        raise Exception("unsupported suorce type")

def unpack(source: str, destination: str) -> None:
    if not os.path.exists(source):
        raise Exception("source path doesn't exist {}".format(source))

    with tarfile.open(source, "r:gz") as tar:
        tar.extractall(path=destination)

def main():
    args = parse_args()
    for item in args.config:
        if item.get("example", False):
            continue

        if "source" not in item or "destination" not in item or "action" not in item:
            raise Exception("source, destination and action fields are required in deploy " \
                    "config's item: {}".format(repr(item)))
        item["source"] = os.path.join(args.configs_dir, item["source"])

        if os.path.exists(item["destination"]) and item.get("cleanup", False):
            shutil.rmtree(item["destination"])
        os.makedirs(item["destination"], exist_ok=True)

        action = item["action"]
        if action == "copy":
            copy(item["source"], item["destination"])
        elif action == "unpack":
            unpack(item["source"], item["destination"])
        else:
            raise Exception("unknown action field in deploy config's item: {}".format(action))

        if "owner" in item:
            set_owner(item["destination"], item["owner"],
                      item.get("set_folder_attrs", False))

        if "permissions" in item:
            set_permissions(item["destination"], int(item["permissions"], 8),
                            item.get("set_folder_attrs", False))

if __name__ == "__main__":
    main()
