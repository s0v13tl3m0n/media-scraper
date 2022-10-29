#!/usr/bin/env python3

import os
from wcmatch.pathlib import Path
import shutil
from datetime import datetime
from tqdm import tqdm

path = r"C:/Users"
total, used, free = shutil.disk_usage("/")
storage_sizes = ('B', 'KB', 'MB', 'GB', 'TB', 'PB')
file_formats = ("*.png", "*.jpeg", "*.jpg", "*.jfif", "*.webp",
                "*.pdn", "*.mp4", "*.mov", "*.gif", "*.mkv", "*.webm",
                "*.mwv")


def humansize(bites):
    i = 0
    while bites >= 1024 and i < len(storage_sizes)-1:
        bites /= 1024.
        i += 1
    f = ('%.2f' % bites).rstrip('0').rstrip('.')
    return '%s %s' % (f, storage_sizes[i])


def file_indexer(formats):
    index_size = 0
    file_out = []
    # for suffix in formats:
    for file in Path(path).rglob(formats):
        unix_time = file.stat().st_mtime
        # print(file.name, file.stat().st_size, unix_time, datetime.utcfromtimestamp(unix_time).strftime("%Y%m"))
        index_size += file.stat().st_size
        file_path = str(file.absolute())
        file_dict = {"filename": file.name, "filesize": file.stat().st_size,
                     "date": datetime.utcfromtimestamp(unix_time).strftime("%Y_%m"), "filepath": file_path}
        file_out.append(file_dict)
    return index_size, file_out


def tree_creation(file_dict):
    tree_path = f"{os.getcwd()}/output/"
    os.mkdir(tree_path)
    for file in tqdm(file_dict):
        if file["date"] not in os.listdir(tree_path):
            os.mkdir(f"{tree_path}/{file['date']}/")


def file_mover(file_dict):
    move_path = f"{os.getcwd()}/output/"
    for file in tqdm(file_dict):
        shutil.copy2(file["filepath"], f"{move_path}{file['date']}")


space, files = file_indexer(file_formats)
print(f"Total: {humansize(total)} \n"
      f"Used: {humansize(used)}\n"
      f"Free: {humansize(free)}\n"
      f"Needed: {humansize(space)} for {len(files)} item(s)")

tree_creation(files)
file_mover(files)
# shutil.make_archive("output", "zip", f"{os.getcwd()}/output")
