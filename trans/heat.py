import cv2
from PIL import Image
import numpy as np
from pyheatmap.heatmap import HeatMap
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pinyin as pyin

import operator
'''
    绘制原文档中各拼音字母出现的热力图
'''
fraq,dict=pyin.freqpy()


f=pd.DataFrame.from_dict(fraq, orient='index', columns=['26 key frequency'])
#print(f)

ax=sns.heatmap(f,cmap="YlGnBu",annot=True,yticklabels=True,fmt='.4g')
ax.set(title= "26 key Heatmap %")
#plt.savefig('a.jpg')
plt.show()