import pandas as pd
from pyreadstat import pyreadstat
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHer"]#设置字体


def 读取spss数据文件(文件位置信息,是否保留标签值:bool):
        数据表,metadata = pyreadstat.read_sav(数据位置及名称,apply_value_formats=True,format_as_ordered_category=True)
        return 数据表

def 生成有序类别变量描述统计表(表名,变量名):
        
                     result = 表名[变量名].value_counts(sort=False)
                     描述统计表 = pd.DataFrame(result)
                     描述统计表['比例']=描述统计表['count']/描述统计表['count'].sum()
                     描述统计表['累计求和'] = df_result['count'].cumsum()
                     df_result['比例'] = 描述统计表['比例'].cumsum()
                     return 描述统计表

def 绘制直方图(表名,y):
        x = 表名.index
        y = 表名[y].values
        fig,ax2 = plt.subplot()
        ax2.bar(x,y)
        plt.show()