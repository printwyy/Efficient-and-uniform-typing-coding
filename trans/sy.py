'''
    量化效率
    由于影响打字效率的因素有很多，如：平均码长、指法是否规范、是否熟悉键盘、按键速度、重码率（同字母组合需筛选的同音字）、电脑处理速度、键盘反馈速度等
    其中大部分因素是由于人、电脑工具和输入法的不同，仅根据原文档是暂时无法量化确定的
    理论上可以把打字效率理解为（按键速度（键/秒）除以 有效平均码长（键/字））为每秒的打字输入效率

    而在这里按键速度人与人之间是不同的，无法完全确定，而可以确定的是有效平均码长
    可以根据效率理论公式得出码长越短效率越高
    平均码长可以通过提取文档中字母个数和汉字个数计算出来的理论有效平均码长
    假定理想状态为无联想功能的全拼输入，每个字需要完全的全拼字母组合输入
    在这里，影响效率的评价因素为有效平均码长，即：全文输入所有的拼音字母/全文字数 单位：键/字 （平均输入一个字需要按多少个键）

'''


import pinyin as py


def eff(wordnum,charsum):

    #print(wordnum)
    '''
    charsum=0
    for key in charnum:
        charsum += charnum[key]
    '''
    codelen=charsum/wordnum

    #print(codelen)   #效率  有效平均码长
    return codelen

if __name__ == '__main__':

    pinyin,wordnum=py.readtxt()
    freq,charnum=py.freqpy()
    num=sum(charnum.values())
    print("效率（输入原文的平均码长）：", end=' ')
    print(eff(wordnum,num))
