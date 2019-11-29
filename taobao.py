import re
import requests
def getHTMLText(url):
    try:
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0','cookie':'x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; UM_distinctid=16e125e5a10229-09e0d7a010e66a-5a4c2571-100200-16e125e5a1126d; thw=cn; t=90f91ed2488d822c744e82f599950726; enc=wR3l2pI09AiAf%2BNS1DSQD6rb9NYToosUwQ43U4arwDjUHUrN91%2FxfOhtcqWHqbaMTLb9SaEZgOpIScotLeodug%3D%3D; cna=XLy/EhaG+0wCAd9o1DLah0s+; tracknick=%5Cu6211%5Cu4EEC%5Cu7EC8%5Cu7A76%5Cu8D70%5Cu6563%5Cu4E86; tg=0; miid=1571420093237246978; v=0; cookie2=11d77de2fdb61fe20c79f0d3a19ff2c8; _tb_token_=ea73833ee6e78; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; hng=CN%7Czh-CN%7CCNY%7C156; JSESSIONID=07AC30435CB76F5AEF973E212C2C851A; unb=1859456835; uc3=vt3=F8dByuQGG9uUvqX9OIc%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&id2=Uone%2BXHBPl67Cg%3D%3D&nk2=rUtN8Ly5N3yGX3JVUis%3D; csg=07b92c69; lgc=%5Cu6211%5Cu4EEC%5Cu7EC8%5Cu7A76%5Cu8D70%5Cu6563%5Cu4E86; cookie17=Uone%2BXHBPl67Cg%3D%3D; dnk=%5Cu6211%5Cu4EEC%5Cu7EC8%5Cu7A76%5Cu8D70%5Cu6563%5Cu4E86; skt=0ba77eac64a99555; existShop=MTU3NDk5NzU2Mg%3D%3D; uc4=id4=0%40UOE0A6S3iB%2FKEht77p20BXDY5yQs&nk4=0%40r7rLGdg7S0g7h3XngFX%2FR5A87cwOlgfq%2Bw%3D%3D; _cc_=Vq8l%2BKCLiw%3D%3D; _l_g_=Ug%3D%3D; sg=%E4%BA%865f; _nk_=%5Cu6211%5Cu4EEC%5Cu7EC8%5Cu7A76%5Cu8D70%5Cu6563%5Cu4E86; cookie1=VvqvoNDwY6ywIKqOhnLHvSFPL%2FQXaLivg1eEZmrCHaE%3D; mt=ci=22_1; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=UIHiLt3xSifiVqTH8o%2F0Qw%3D%3D&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&existShop=false&pas=0&cookie14=UoTbmVndNdhzFQ%3D%3D&tag=10&lng=zh_CN; l=dBMsRO_4vCXJX1jMKOCNVqIHPDQTkBdbYukAtxrJi_5B21Y1Nh_OknEEdev6cjWcMxTW455IUh2TBFwzJyMjJ0YEaj-fvdHDBef..; isg=BDQ0bGwh1YfEsUAV0h55igrNC_Kcys5Mrfbp886Vf79COdaD_h0oh-q_vXHh2pBP'}
        re = requests.get(url, headers = headers)
        re.raise_for_status()
        re.encoding = re.apparent_encoding
        return re.text
    except:
        return ""
def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(":")[1])
            ilt.append([price,title])
    except:
        print("")
def printGoodsList(ilt):
    tplt ="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count+1
        print(tplt.format(count,g[0],g[1]))
def main():
    goods = '书包'
    depth = 10
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)
main()