
'''

通过分析高频声母和单韵母以及各组合韵母的出现频数
用就近和最少使用频数优先原则，使用高频单韵母周围的低频声母代替原组合韵母，设计了三种方案

'''

import pinyin as py
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import string
import sy
import quantification as q

def repla(rep,str):   #按照方案替换对应的字符串
    for i in rep.keys():
        str=str.replace(i,rep[i])

    return str


def descr(data):  #重新描述替换后的新输入方案的各项指标

    dictcount={}
    for i in data:
        if i not in dictcount.keys() :
            dictcount[i]=data.count(i)

    #print(dict)
    ssum=0
    freq={}
    for key in dictcount:
        ssum+=dictcount[key]

    for k in dictcount:
        freq[k]=dictcount[k]/ssum
        freq[k]=freq[k]*100

    f=pd.DataFrame.from_dict(freq, orient='index', columns=['26 key % frequency'])
    #print(f)

    ax=sns.heatmap(f,cmap="YlGnBu",annot=True,yticklabels=True,fmt='.4g')
    ax.set(title= "26 key Heatmap %")  #绘制使用新输入方案的热力图
    #plt.savefig('b.jpg')

    plt.show()

    #print(sum)
    jhx=q.quan(freq,dictcount)

    key=list(dictcount.keys())
    count=list(dictcount.values())
    plt.bar(key,count)

    plt.xlabel('key')
    plt.ylabel('count')   #画新输入编码方案的各字母使用频数
    plt.savefig('count2.jpg')
    plt.show()
    return jhx,ssum

str1,num=py.readtxt()
#方案1
rep1={"ai":'q',"ao":'w',"an":'x',"ang":"av","ei":'f',"er":'r',"en":'t',"ie":'d',"eng":"ev",
     "un":'l',"ui":'k',"iu":'m',"ing":"iv","ou":'p',"ong":"ov","ve":"vv","ch":"cc","zh":"zz","sh":"ss"}
#方案2
rep2={"ai":'q',"ao":'w',"an":'x',"ang":"av","ei":'f',"er":'d',"en":'t',"ie":'r',"eng":"ev",
     "un":'l',"ui":'k',"iu":'m',"ing":"iv","in":'j',"ou":'p',"ong":"ov","ve":"vv","ch":"cc","zh":"zz","sh":"ss"}
#方案3
rep3={"ai":'q',"ao":'w',"an":'x',"ang":"av","ei":'f',"er":'d',"en":'t',"ie":'r',"eng":"ev",
     "un":'b',"ui":'k',"iu":'m',"ing":"iv","in":'l',"ou":'p',"ong":"ov","ve":"vv","ch":"cc","zh":"zz","sh":"ss"}

#with open("gcdxyre2.txt", "w") as f:
 #   f.write(str1)
  #  f.close()

#with open("gcdxyre.txt", "r") as f:  # 打开文件
 #   data = f.read()  # 读取文件
with open("gcdxy.txt", "r") as f:  # 打开文件
    data = f.read()  # 读取文件
    f.close()

res1 = ''.join(re.findall('[\u4e00-\u9fa5]', data))
hanzisum = len(res1)

jh=[0,0,0,0]
sum=[0,0,0,0]
effi=[0,0,0,0]

data1=repla(rep1,str1)

data2=repla(rep2,str1)

data3=repla(rep3,str1)

jh[1],sum[1]=descr(data1)

jh[2],sum[2]=descr(data2)

jh[3],sum[3]=descr(data3)

pinyin,wordnum=py.readtxt()
freq,charnum=py.freqpy()
jh[0]=q.quan(freq,charnum)
ssum=0
for key in charnum:
    ssum += charnum[key]
sum[0]=ssum


x=["original","rep1","rep2","rep3"]

for i,item in enumerate(sum):
    effi[i]=sy.eff(hanzisum,item)
print("不均衡系数：",end=' ')
print(jh)
print("各方案使用的理论码数：",end=' ')
print(sum)
print("效率（平均码长）：",end=' ')
print(effi)

#绘制原编码和三个新编码 均衡系数和效率的比对折线图
fig = plt.figure()
ax1 = fig.add_subplot(121)

# 设置图中图例内容和位置
ax1=plt.plot(x, effi, label='efficient', color='r',linewidth=2, linestyle='-.')

plt.xlabel('programme')
plt.ylabel('value')  #
plt.title("efficient")

ax2 = fig.add_subplot(122)
ax2=plt.plot(x, jh, label='equilibrium', color='b', linewidth=2,linestyle='--')
plt.xlabel('programme')
plt.ylabel('value')
plt.title("equilibrium")
#plt.savefig('Overall comparison.jpg')
plt.show()

'''
    选择均衡性和效率较为合适的方案2作为新的编码方案
'''



'''
rep2=rep

for i in rep2.keys():   #计算各组合韵母的出现频率
    rep2[i]=str1.count(i)

print(rep2)
'''