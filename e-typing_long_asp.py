from selenium import webdriver # Webブラウザを自動操作する（python -m pip install selenium)
from selenium.webdriver.chrome.options import Options # オプションを使うために必要
from time import sleep
from selenium.webdriver.common.keys import Keys
import selenium
import time
import sys

start = time.time() #処理時間の測定開始
# option = Options()                          # オプションを用意
# option.add_argument('--headless')           # ヘッドレスモードの設定を付与

# driver = webdriver.Chrome(options=option, executable_path='yourpath/chromedriver')   # Chromeを準備(optionでシークレットモードにしている）
driver = webdriver.Chrome(executable_path='yourpath/chromedriver')   # Chromeを準備(optionでシークレットモードにしている）

url = "https://www.e-typing.ne.jp/roma/variety/long.asp"
driver.get(url) #googleを開く

sleep(2)
print(driver.current_url)

check_btns = driver.find_elements_by_xpath("//a[@class='keybo']")
for check_btn in check_btns:
    check_btn.click()
    break

sleep(2)
print(driver.current_url)

try:
    #frameの切り替え
    driver.switch_to_frame('typing_content')
    print("Change iframe")
    driver.find_element_by_id('start_btn').click()
    print("click start_btn")
    sleep(2)

    #スペースキーを入力してスタートする
    body_element = driver.find_element_by_tag_name('body')
    body_element.send_keys(Keys.SPACE)
    time.sleep(3.5)

    #入力するテキストを習得
    # sentence = driver.find_element_by_xpath('//div[@id="sentenceText"]').text
    # print(sentence)
    sentence = driver.find_element_by_xpath('//div[@id="sentenceText"]').text
    print(sentence)
    #取得したテキストを１文字ずつ入力する
    for key in(sentence):
        body_element.send_keys(key)
        sleep(0.03)
        
except selenium.common.exceptions.NoSuchElementException:
    driver.quit()
    sys.exit()

# driver.quit()
# sys.exit()
