'''
    评价均衡性
    均衡性理解为 两手打字工作的均衡性+各字母的出现频率均衡性 两个影响因子
    按标准指法来说，左手应按qwertasdfgzxcvb 15个字母 右手应按yuiophjklnm 11个字母
    评价左右手的工作均衡性应是左右手按键比值接近15/11
    而各字母的使用均衡性，采用变异系数，即标准差/平均数  使用频率越相近，变异系数越小

    最后对两个影响因子组合为一个量化值
    公式为：变异系数+（实际左手按键次数/实际右手按键次数-理论按键次数比（15/11））的绝对值

'''
import pinyin as pin
import numpy as np
import matplotlib.pyplot as plt
def quan(freq,cout):


    key=list(cout.keys())
    count=list(cout.values())
    ave=np.mean(count)
    var=np.var(count)
    std=np.std(count)
    left='qwertasdfgzxcvb'
    right='yuiophjklnm'

    lcount=0
    rcount=0
    for i in cout:
        if i in left:
            lcount+=cout[i]
        else:
            rcount+=cout[i]

    standard=len(left)/len(right)
    s=lcount/rcount    #分析左右手均衡性
    cv=std/ave
    jhx=cv+abs(standard-s)   #左右手比值与标准指法分布比值差+变异系数    数值越小越均衡
    #print(jhx,cv,lcount,rcount,s,standard)
    return jhx  #不均衡系数 数值越小越均衡

if __name__ == '__main__':

    freq,cout=pin.freqpy()
    print("原键盘输入的不均衡系数：",quan(freq,cout))

    key = list(cout.keys())
    count = list(cout.values())
    plt.bar(key,count)

    plt.xlabel('key')
    plt.ylabel('count')
    #plt.savefig('count.jpg')
    plt.show() #画出26个字母各自在该文章中出现的次数 条形图



