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

