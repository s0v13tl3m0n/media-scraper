#!/usr/bin/env python3
import os
from pathlib import Path
import shutil
from datetime import datetime, timedelta

path = r"C:/Users"
index_size = 0
file_dict = {}
total, used, free = shutil.disk_usage("/")
storage_sizes = ('B', 'KB', 'MB', 'GB', 'TB', 'PB')


def humansize(bytes):
    i = 0
    while bytes >= 1024 and i < len(storage_sizes)-1:
        bytes /= 1024.
        i += 1
    f = ('%.2f' % bytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, storage_sizes[i])


def file_indexer(formats):

    for file in Path(path).rglob("*.png"):
        unix_time = file.stat().st_ctime
        print(file.name, file.stat().st_size, unix_time, datetime.utcfromtimestamp(unix_time).strftime("%Y%m"))

# directory_list = list()
# for root, dirs, files in os.walk(path, topdown=False):
#     for name in dirs:
#         directory_list.append(os.path.join(root, name))

# print(directory_list)

print(f"Total: {humansize(total)}")
print(f"Used: {humansize(used)}")
print(f"Free: {humansize(free)}")
print(humansize(index_size), "/", free)
