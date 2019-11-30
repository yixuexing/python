import re
from bs4 import BeautifulSoup
import requests
import traceback
def getHTMLText(url,code = 'utf-8'):
    try:
        re = requests.get(url,timeout = 30)
        re.raise_for_status()
        re.encoding = code
        return re.text
    except:
        return ""
def getStockList(lst,stockURL):
    html = getHTMLText(stockURL,'GB2312')
    soup = BeautifulSoup(html,"html.parser")
    a = soup.find_all("a")
    for i in a:
        try:
            href = a.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}",href)[0])
        except:
            continue
def getStockInfoList(stockinfoURL,lst,fpath):
    for stock in lst:
        url = stockinfoURL + stock +".html"
        html = getHTMLText(stockinfoURL)
        try:
            if html=="":
                continue
            infoDict = {}
            soup = BeautifulSoup(html,"html.parser")
            stockInfo = soup.find("div",attrs={'class':'stock-bets'})
            name = stockInfo.find_all(attrs = {'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                value = valueList[i].text
                infoDict[key]=value
            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict)+'\n')
        except:
            traceback.print_exc()
            continue
def main():
    stock_list_url = "http://www.eastmoney.com/"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    output_file = "E:/StockInfoList.txt"
    sList = []
    getStockList(stock_list_url,sList)
    getStockInfoList(stock_info_url,sList,output_file)
main()