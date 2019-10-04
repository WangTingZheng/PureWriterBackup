import zipfile

z = zipfile.ZipFile('../res/zip/test.pwb', 'r')
z.extractall(path=r"../res/temp")
z.close()