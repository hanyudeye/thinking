 todo: 看书，或pdf，或一个网页 ,系统学习

1. 每个学习周期，看一页书 (25分钟) ,这是合理的学习任务，能按时完成

2. 戴耳机隔离噪音


## 2026-05-02

- [x] 周期1 输入输出
- [x] 周期2 学会使用gptel 进行终端问问题 (这样就可以减少打开网页)，但终端不智能呀，还是要想办法
- [x] 周期4 查看有关 shell 的网页
- [x] emacs 中有什么快捷键可以直接选中一行 , can use ~v j~ do it
- [x] thinking: 为自己的困难找借口是 没有成长吗？ 困难的种类 是的，任何困难都是人解决的，解决的程度看自己的态度
- [x] put translation window to 0.2 
- [x] 周期3 编程往后面再看一页，下一页(page 6)讲的是一些函数的概念说明，不是很复杂，但看着很枯燥还是什么
- [x] 修改tmux底部右侧状态栏的显示 set -g status-right "%H:%M"
- [x] page7 提出了stream 流的 abstract conception 抽象 概念，和函数接近，提供一些东西，会产生另一种东西，这个东西就是不同类型的流，语言开发者创造这种抽象可能是为了给 语言使用者 更方便的使用吧
- [x] page8-9 注释的作用是 作为编码的文档，辅助说明或概括说明编码的用途
- [x] page 10-16 控制结构，分支/重复，分支使功能更灵活，有一种智能感
- [x] page 17-29 类，模块化，工程化，规范
- [x] page 30-68 变量 vars ，可以变化的数据，这种数据一般作为中转吧，maybe,so you can use it to do some operation,like mathematical computation。高级语言的发明者，为了实现自然语言编程，已经做了很多的工作，例如做出图形程序，更容易让计算机知道你的用途，而那些各种应用库的创造者，创造了很多有用的库，所以现在编程已经非常简单了，只要引入库，直接使用，就像搭积木，或购买零件一样
- [x] page 69-95 使用库 iostream , vector ,..
- [x] page 96-120 数组和指针 , 指针是机器相关的对象，表示对象所在的内容地址，因为自然语言中不会用到，但写论文的时候，有一个引用符号，或者网页链接/桌面快捷方式，所以指针一般用于引用，跟变量意思差不多，但因为指针也是一个数字，以前可能会用于计算，但现在都不推荐使用了，因为要很小心
- [x] 表达式：数学计算的表达式，语言科学家把它复用于 数学计算
- [x] page 196: 函数，也是为了规范，把一个<计算机执行功能> 集中到一个块中，组合成库后就可以很方便地复用
- []

## 2026-05-19

- 玻璃纤维，主要用于隔热，危害没有石棉大，别太恐惧，注意空气质量
- [x] todo: 下载sdcv 词典，因为当前朗道词典词汇不够
- 完整表达某个观点，就是要说出完整的故事
- wsl 中的网络和windows 的网络是怎么样的，为什么断网后就无法互联

## 2026-05-20
- 给我一个python脚本，我能根据日期推算每天的涨潮时间，比如我输入一个日期，你给我涨潮时间



Here's a Python script that calculates the high tide time for a given date:

```Python
import datetime as dt
from pytz import timezone, UTC

# Define the location and its offset from UTC
location = "New York"  # adjust to your desired location
offset = -5 * 60 * 60  # in seconds (adjust according to your time zone)

# Create a timezone object for the given location
tz = timezone(location)
UTC_tz = UTC()

def high_tide(date_str):
    date_obj = dt.datetime.strptime(date_str, "%Y-%m-%d")
    date_obj_utc = UTC_tz.localize(date_obj).astimezone(tz)
    
    # Calculate the high tide time based on the location
    if location == "New York":
        high_tide_offset = 2.5 * 60 * 60  # in seconds (adjust according to your high tide offset)
        return date_obj_utc + dt.timedelta(seconds=high_tide_offset)
    else:
        raise ValueError(f"High tide calculation not implemented for {location}.")

date_str = input("Enter a date (YYYY-MM-DD): ")
print(high_tide(date_str))
```

To use this script, simply replace `"New York"` with your desired location (which must be supported by the `pytz` library), and run the script. When prompted, enter a date in the format `YYYY-MM-DD`. The script will output the high tide time for that date.

Note: This script uses the `pytz` library to handle timezone conversions. You may need to install this library using pip (`pip install pytz`) if you haven't already. Additionally, the high tide offset is specific to New York; adjust this value according to your location's actual high tide time.



pytz.exceptions.UnknownTimeZoneError: 'New York'


You're likely trying to use the 'US/East' timezone instead of 'New York', which is not a recognized timezone. Try replacing it with `pytz.timezone('US/East')`.


- [x] 使用 emacs看 spacemacs 文档 2026-05-20T02:42:52+08:00
- 我感觉空想根本就没有灵感，还不如出去走走，所以看书比空想重要，要增加阅读量




