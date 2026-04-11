import os
import shutil

def copy_origin_contents_to_destination(origin, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    if not os.path.exists(destination):
        os.mkdir(destination)

    origin_contents = os.listdir(origin)
    item_paths = []
    for item in origin_contents:
        item_path = os.path.join(origin, item)
        if os.path.isfile(item_path):
            item_paths.append(item_path)
            shutil.copy(item_path, destination)
        else:
            directory_copy_path = os.path.join(destination, item)
            nested_item_paths = copy_origin_contents_to_destination(item_path, directory_copy_path)
            item_paths.extend(nested_item_paths)
    return item_paths