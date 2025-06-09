# 播放中文歌曲
import pygame

#初始化调音器
pygame.mixer.init()

#加载音乐文件
pygame.mixer.music.load("1.mp3")
#播放音乐文件
pygame.mixer.music.play()
# 等待播放完成
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
