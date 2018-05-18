import pandas as pd
import re

num = {'java':0,'php':0,'cpp':0,'web':0,'unity':0,'python':0,'other':0}

job = pd.read_csv("job_list.csv",encoding="gbk")
#print(job['title'])

for j in job['title']:
    #引入re(正则表达式)模块，忽略大小写
    if(re.search('java',j,re.IGNORECASE)):
        #print(j)
        num['java'] += 1
    elif(re.search('php',j,re.IGNORECASE)):
        num['php'] += 1
    elif(re.search('c\+\+',j,re.IGNORECASE)):
        num['cpp'] += 1
    elif(re.search('web',j,re.IGNORECASE)):
        num['web'] += 1
    elif(re.search('unity',j,re.IGNORECASE)):
        num['unity'] += 1
    elif(re.search('python',j,re.IGNORECASE)):
        num['python'] += 1
    else:
        num['other'] += 1

print(num)

title = []
number = []

for key in num.keys():
    title.append(key)
for value in num.values():
    number.append(value)


dataframe = pd.DataFrame({"number":number,"title":title})
dataframe.to_csv("deal.csv",index=None,sep=',')

dataframe = dataframe.sort_values('number',ascending=True)[:6]

dataframe_plot = dataframe.plot(kind="barh",x=dataframe["title"],
                                title="job",legend=False)
fig = dataframe_plot.get_figure()
fig.show()
fig.savefig("job.png")
