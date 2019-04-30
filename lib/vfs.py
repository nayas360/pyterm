# Virtual File System manager
import os
from zipfile import ZipFile

root = 'root/'
fname = 'FileSystem.fs'
LEVEL = 8  # compression level 0 or 8 only
CMP64 = True  # 64 bit compression


def init():
    if fname not in os.listdir():
        try:
            os.mkdir(root)
        except:
            pass
    else:
        zf = ZipFile(fname, 'r', LEVEL, CMP64)
        zf.extractall(root)
        zf.close()
        # os.remove(fname)


def cleanup():
    def addToZip(zf, path, zippath):
        if os.path.isfile(path):
            zf.write(path, zippath, LEVEL)
            # print(path)
        elif os.path.isdir(path):
            for nm in sorted(os.listdir(path)):
                # print(path)
                addToZip(zf, os.path.join(path, nm), os.path.join(zippath, nm))
            zf.write(path, zippath, LEVEL)
            # print(path)

    zf = ZipFile(fname, 'w', LEVEL, CMP64)
    addToZip(zf, root, os.path.basename(root))
    zf.close()
    # delete everything recursively
    # print()
    clean(root, root)


def clean(path, node):
    if os.path.isfile(path):
        os.remove(path)
        # print(path)
    elif os.path.isdir(path):
        for nodes in sorted(os.listdir(path)):
            # print(path)
            clean(os.path.join(path, nodes), os.path.join(node, nodes))
        os.rmdir(path)
        # print(path)
