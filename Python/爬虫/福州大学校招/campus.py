import threading

import urllib.request
from lxml import etree

def open_html(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
    html = urllib.request.urlopen(req).read().decode()
    return html

def run(start):
    host = "http://www.fjrclh.com/"

    for i in range(start,start+5):
        print(threading.current_thread().name + "\t" + str(i))
        url = host + "newslistnew.asp?page={i}&classid=16&Nclassid=42".format(i=i)
        html = open_html(url)

        page = etree.HTML(html)

        for each in page.xpath("/html/body/div[2]/div[2]/table//ul/li"):
            title = each.xpath("a/text()")
            url = each.xpath("a/@href")
            result.append(title[0] + "\t" + url[0] + "\n")

def main():
    global result
    result = []

    ts = []
    for i in range(10):
        t = threading.Thread(target=run, args=(i*5+1,))
        t.start()
        ts.append(t)
    for t in ts:
        t.join()

    with open("福州大学宣讲会.txt", "w", encoding="utf-8") as f:
        for each in result:
            f.write(each)



if __name__ == "__main__":
    main()