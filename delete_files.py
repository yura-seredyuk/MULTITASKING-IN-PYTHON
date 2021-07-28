from pathlib import Path
import os


directory = '../../test_files'
pathlist = [name for name in Path(directory).glob('*.txt')]


pathlist = [name for name in Path(directory).glob('*.txt')]
c = 0
for path in pathlist:
    c += 1
    os.remove(path)
    print(path)
print(c)