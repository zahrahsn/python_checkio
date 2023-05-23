import os
import re
import os.path
import sys
from re import Pattern

pattern = r's(\d+).?e(\d+)|season(\d+).?episode(\d+)|(\d+)x(\d+)'


def tuple_to_string(tuple_string, ext) -> str:
    return f'S{tuple_string[0]}.E{tuple_string[1]}{ext}'


if __name__ == "__main__":
    x = sys.argv[0]
    p = sys.argv[1]
    # print(p)
    p = p.replace('\\\\', '\\')
    files = os.listdir(p)
    for f in files:
        match_result = re.findall(pattern, f.lower())
        if match_result is not None:
            ext = os.path.splitext(f)[1]
            resultofdef = tuple_to_string(match_result[0], ext)
            pre = os.path.join(p, f)
            new = os.path.join(p, resultofdef)
            os.rename(pre, new)
            print(f"File {pre} => {new}")
    # print(series)
