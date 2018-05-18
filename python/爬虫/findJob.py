import urllib.request
import urllib.parse
import pandas as pd
import csv
from lxml import etree

def find():
    
    '''
    with open("job_list.csv","a") as csvfile:
        writer = csv.writer(csvfile,lineterminator='\n')
        writer.writerow(["page","title"])
    '''

    joblist = []
    for i in range(1,33):
        print("第" + str(i) + "页")
        url = 'https://search.51job.com/list/110200,000000,0100,01,9,99,%2B,2,'+\
                str(i) +'.html?\
                lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99\
                &jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&\
                ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&\
                line=&specialarea=00&from=&welfare='

        req = urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
        html = urllib.request.urlopen(req).read().decode("gbk")
        #print(html)

        for j in search(html):
            joblist.append(["第" + str(i) + "页",j])

    #print(joblist)
    #{"page":i,"title":title}
    dataframe = pd.DataFrame(joblist,columns=["page","title"])
    dataframe.to_csv("job_list.csv",index=False,sep=',',encoding='gbk')

    '''
    ii = []
    for t in title:
        ii.append(["第" + str(i) + "页",t])
    #print(ii)
    with open("job_list.csv","a") as csvfile:
        writer = csv.writer(csvfile,lineterminator='\n')
        writer.writerows(ii)
    '''

def search(html):
    page = etree.HTML(html)
    for each in page.xpath('//*[@id="resultList"]'):
        title = each.xpath('div/p/span/a/@title')
        #print(title)
        return title


    '''
    for each in title:
        if 'java' in each:
            print(each)
    '''

if __name__ == '__main__':
    find()
    
#//*[@id="resultList"]/div[14]/p/span/a
