from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
import time
from PIL import Image
from io import BytesIO
import socket
import argparse
import os
import json
from urllib.request import Request
import urllib

socket.setdefaulttimeout(50)


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


def download(arg):
    url = "https://www.google.co.in/search?q=" + arg['searchterm'] + "&source=lnms&tbm=isch"
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get(url)
    sucessfull = 0
    errors = 0
    temp1 = AppURLopener()

    n_scrolls = arg['n_images'] // 100
    for _ in range(n_scrolls):
        hits = len(driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'))
        driver.execute_script("window.scrollBy(0,10000)")
        time.sleep(2)
        if hits == len(driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')):
            try:
                driver.find_element_by_xpath('//*[@id="smb"]').click()
            except ElementNotVisibleException:
                print('End of page, no more images can be found')
                break

    time.sleep(5)
    images = driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')
    print('Found {} results'.format(len(images)))
    if not os.path.exists(arg['savedir']):
        os.makedirs(arg['savedir'])

    for image in images:
        img_url = json.loads(image.get_attribute('innerHTML'))["ou"]
        try:
            response = temp1.open(img_url).read()
            im = Image.open(BytesIO(response))
            if arg['gray']:
                im = im.convert('L')
            if arg['target_size'] != None:
                x, y = map(int, arg['target_size'].split(','))
                if x < im.width or y < im.height:
                    im = im.resize((x, y), Image.ANTIALIAS)
                else:
                    im = im.resize((x, y))
            im.save('{0}/scraped_{1}.png'.format(arg["savedir"], sucessfull))
            sucessfull += 1
        except:
            errors += 1
        print('\rImages downloaded: {0}, errors: {1}'.format(sucessfull, errors), flush=True, end='')
    print()
    driver.close()


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-se', '--searchterm', required=True, help='The string you want to search for')
    ap.add_argument('-ni', '--n_images', help='Number of scrolls to perform', type=int, default=100)
    ap.add_argument('-sd', '--savedir', help='Where to save the data', default='data/')
    ap.add_argument('-gr', '--gray', help='1 for grayscale, 0 otherwise', type=int, default=0)
    ap.add_argument('-ts', '--target_size', help='Target size of images', default=None)
    args = vars(ap.parse_args())
    download(args)
