
import re
def reg_search(text):
    regex_list = []
    regex_list_dic={
        '标的证券':None,
        '换股日期':None

    }


    #re取key作result_one
    result_one=re.findall(r'\d*[.]\w*',text,re.S)
    #re取value作result_two
    result_two=re.findall(r'\d{4}年\d{1,3}月\d{1,4}日',text,re.S)
    regex_list_dic['标的证券']=result_one
    list=[]
    for i in result_two:
        list.append(i)
    regex_list_dic['换股日期']=list
    regex_list.append(regex_list_dic)
    print(regex_list)

if __name__=='__main__':
    #原文
    text="""标的证券：本期发行的证券为可交换为发行人所持中国长江电力股份有限公司股票（股票代码：600900.SH，股票简称：长江电力）的可交换公司债券。
换股期限：本期可交换公司债券换股期限自可交换公司债券发行结束
之日满 12 个月后的第一个交易日起至可交换债券到期日止，即2023年6月2日至2027年6月1日止。"""
    #运行代码
    reg_search(text)
