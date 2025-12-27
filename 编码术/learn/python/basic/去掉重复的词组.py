import sys

# 去除重复的单词
words=set(sys.argv[1:])
# print("去除重复的单词:", words)
# print("单词个数:", len(words))
print("有{}个不同的单词: 分别是{}".format(len(words), words))
