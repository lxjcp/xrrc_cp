
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
def action():
    #执行操作,获取数据
    driver.find_element(By.XPATH, '//*[@id="Bond_Type_select"]').click()
    driver.find_element(By.XPATH, '//*[@id="Bond_Type_select"]/option[2]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="Issue_Year_select"]').click()
    driver.find_element(By.XPATH, '//*[@id="Issue_Year_select"]/option[3]').click()
    driver.find_element(By.XPATH, '//*[@id="resetValue"]/div/div[8]/a[1]').click()
    sleep(3)
    driver.execute_script('var q=document.documentElement.scrollTop=100000')
    value = int(driver.find_element(By.XPATH, '//*[@id="pagi-bond-market"]/li[1]/span/span').text)
    new_items = []
    for i in range(1,int(value)+1):
        if i==1:
            text= driver.find_element(By.XPATH,'//*[@id="sheet-bond-market"]/div[1]/div').text
            sleep(2)
            #数据整理
            items=[]
            items=text.split('\n')
            for value in items:
                new_item=[]
                new_item=value.split()
                new_items.append(new_item)
            driver.execute_script('var q=document.documentElement.scrollTop=10000')
            sleep(1)
            driver.find_element(By.XPATH, '//*[@id="pagi-bond-market"]/li[4]/a').click()
        else:
            text = driver.find_element(By.XPATH, '//*[@id="sheet-bond-market"]/div[1]/div').text
            sleep(1)
            # 数据整理
            items = []
            items = text.split('\n')
            for value in items[1:]:
                new_item = []
                new_item = value.split()
                new_items.append(new_item)
            driver.execute_script('var q=document.documentElement.scrollTop=10000')

            driver.find_element(By.XPATH, '//*[@id="pagi-bond-market"]/li[4]/a').click()

    return new_items
def save_css(items):
    indexv=[0,1,12,13,14]
    new_itens=[['ISIN','Bond Code','Issuer','Bond Type','Issue Date','Lates Rating'],]
    for i,item in enumerate(items):
        if i !=0:
            new = []
            for j ,value in enumerate(item):
                if j in indexv:
                    new.append(value)
                elif j == 3:
                    new.append(item[3]+item[4]+item[5]+item[6]+item[7]
                               +item[8]+item[9]+item[10]+item[11])
                new_itens.append(new)
    #将数据存为csv文件
    path='C:\\Users\\CV\\PycharmProjects\\pythonProject1\\xrrc\\xr.csv'
    with open(path,'w',encoding='gbk',newline='',  errors='ignore') as file:
        writer=csv.writer(file)
        writer.writerows(new_itens)




if __name__=='__main__':

    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)  # 避免因程序运行完或报错导致浏览器自动关闭
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(30)
    url='https://iftp.chinamoney.com.cn/english/bdInfo/'
    driver.get(url)
    text=action()
    save_css(text)
    driver.quit()
