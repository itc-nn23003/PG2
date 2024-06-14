# ブラウザが重く、動作確認が全くできておりません。ちゃんと動くかわかりません。

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# WebDriverのパスを指定
driver_path = 'path/to/chromedriver'  # ここにダウンロードしたChromeDriverのパスを指定

driver = webdriver.Chrome()
driver.get('https://play2048.co')

# ゲームボードを取得
game_board = driver.find_element_by_tag_name('body')

# キーの順序
keys = [Keys.ARROW_UP, Keys.ARROW_RIGHT, Keys.ARROW_DOWN, Keys.ARROW_LEFT]

try:
    while True:
        for key in keys:
            game_board.send_keys(key)
            time.sleep(0.2)  # 適宜スピードを調整
except KeyboardInterrupt:
    driver.quit()

