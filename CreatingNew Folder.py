import os.path
import sys

if __name__ == "__main__":
    x = sys.argv[0]
    p = sys.argv[1]
    p = p.replace('\\\\', '\\')
    files = os.listdir(p)
    files_name = []
    folders_name = []
    for f in files:
        f_name = os.path.splitext(f)[0]
        ext = os.path.splitext(f)[1]
        if ext != '':
            files_name.append(f.lower())
        else:
            folders_name.append(f)
    d = {}
    for fold in folders_name:
        d[fold] = []
        for fil in files_name:
            if fold.lower() in fil:
                d[fold].append(fil)
                os.rename(os.path.join(p,fil), os.path.join(p, fold, fil))
                # d.update({fold: fil})
    print(d)
    # print(folders_name)
    # print(files_name)
