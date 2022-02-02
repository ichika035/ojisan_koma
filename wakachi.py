"""
ここから分かち書き
"""

import MeCab
import sys

#tagger = MeCab.Tagger('-F\s%f[6] -U\s%m -E\\n')




import MeCab

tagger = MeCab.Tagger("-Owakati")

f = open("komachi.txt", encoding = "utf_8")
read_text = f.readlines()
f.close()

for text in read_text:
    result = tagger.parse(text)
    with open("koamchi_wakati.txt", encoding = "utf_8", mode="a") as write_file:
        write_file.writelines(result)

"""
FILE_NAME = "komachi.txt"

with open(FILE_NAME, "r", encoding="utf-8") as f:
    CONTENT = f.read()

tagger = MeCab.Tagger()
parse = tagger.parse(CONTENT)


fi = open(sys.argv[1], 'r')
fo = open(sys.argv[2], 'w')

line = fi.readline()
while line:
    result = tagger.parse(line)
    fo.write(result[1:]) # skip first \s
    line = fi.readline()

fi.close()
fo.close()
"""