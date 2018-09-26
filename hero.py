#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PIL import Image
import os

def mkdirPath ():
    localPath = os.path.join(os.path.abspath('.'), 'hero')
    if not os.path.exists(localPath):
        os.mkdir(localPath)
    return localPath

def split ():
    imgDir = mkdirPath()
    index = 0
    im = Image.open('/Users/shiwj/Documents/myhero.jpg')
    print('width: %s height: %s' % (im.width, im.height))
    for i in range(0, 2200, 200):
        for j in range(0, 1600, 200):
            index += 1
            iw = i + 200
            ih = j + 200
            imageItem = im.crop([j, i, ih, iw])
            name = forName(index)
            print('正在裁剪 %s, 坐标位置: %d %d %d %d' %(name, j, i, ih, iw))
            imageItem.save(os.path.join(imgDir, name), 'JPEG')

def forName (index):
    nameList = {
        1: "廉颇",
        2: "小乔",
        3: "赵云",
        4: "墨子",
        5: "妲己",
        6: "嬴政",
        7: "孙尚香",
        8: "鲁班七号",
        9: "庄周",
        10: "刘禅",
        11: "高渐离",
        12: "阿轲",
        13: "钟无艳",
        14: "孙膑",
        15: "扁鹊",
        16: "白起",
        17: "芈月",
        18: "吕布",
        19: "周瑜",
        20: "元歌",
        21: "夏侯惇",
        22: "甄姬",
        23: "曹操",
        24: "典韦",
        25: "宫本武藏",
        26: "李白",
        27: "马可波罗",
        28: "狄仁杰",
        29: "达摩",
        30: "项羽",
        31: "武则天",
        32: "司马懿",
        33: "老夫子",
        34: "关羽",
        35: "貂蝉",
        36: "安琪拉",
        37: "程咬金",
        38: "露娜",
        39: "姜子牙",
        40: "刘邦",
        41: "韩信",
        42: "王昭君",
        43: "兰陵王",
        44: "花木兰",
        45: "张良",
        46: "不知火舞",
        47: "娜可露露",
        48: "橘右京",
        49: "亚瑟",
        50: "孙悟空",
        51: "牛魔",
        52: "后羿",
        53: "刘备",
        54: "张飞",
        55: "李元芳",
        56: "虞姬",
        57: "钟馗",
        58: "杨玉环",
        59: "成吉思汗",
        60: "杨戬",
        61: "女娲",
        62: "哪吒",
        63: "干将莫邪",
        64: "雅典娜",
        65: "蔡文姬",
        66: "太乙真人",
        67: "东皇太一",
        68: "鬼谷子",
        69: "诸葛亮",
        70: "大乔",
        71: "黄忠",
        72: "铠",
        73: "苏烈",
        74: "百里玄策",
        75: "百里守约",
        76: "公孙离",
        77: "明世隐",
        78: "裴擒虎",
        79: "狂铁",
        80: "米莱狄",
        81: "伽罗",
        82: "盾山",
        83: "孙策",
        84: "弈星",
        85: "梦奇",
        86: "1",
        87: "2",
        88: "3",
    }
    return nameList[index]

if __name__ == '__main__':
    split()