'''
    原文档提取汉字并转拼音，统计各字母出现频率和频数
'''
import pypinyin
import re,string

def readtxt():   #读取原文档并提取汉字，转拼音字符串，返回字符串和汉字字数
    with open("gcdxy.txt", "r") as f:  # 打开文件
        data = f.read()  # 读取文件
        f.close()

    res1 = ''.join(re.findall('[\u4e00-\u9fa5]', data))
    hanzisum=len(res1)

    result1 = pypinyin.pinyin(data, style=pypinyin.NORMAL)
    #print(result1)
    result=''
    for i in result1:
        result=result+i[0]

    result=''.join(re.findall(r'[A-Za-z]', result))  #re.sub(r"[%s]+" %punc, "",result)
    #print(result)
    return result,hanzisum

def freqpy():  #计算原文档的各拼音字母出现的频率和频数
    result,hanzisum=readtxt()
    dict={}
    for i in result:
        if i not in dict.keys() :
            dict[i]=1
        else:
            dict[i]+=1

    sum=0
    freq={}
    for key in dict:
        sum+=dict[key]

    for k in dict:
        freq[k]=dict[k]/sum
        freq[k]=freq[k]*100

    return freq,dict

if __name__ == '__main__':
    freq,count=freqpy()
    print("各字母频率%：",end=' ')
    print(freq)
    print("各字母频数：", end=' ')
    print(count)


