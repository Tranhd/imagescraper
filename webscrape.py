from selenium import webdriver
from requests import get
from PIL import Image
from io import BytesIO
import argparse
import os


def download(arg):
    url = "https://www.google.co.in/search?q=" + arg['searchterm'] + "&source=lnms&tbm=isch"
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get(url)
    sucessfull = 0
    errors = 0

    for _ in range(arg['scrolls']):
        driver.execute_script("window.scrollBy(0,10000)")

    images = driver.find_elements_by_tag_name('img')
    print(f'log: Found {len(images)} results')
    if not os.path.exists(arg['savedir']):
        os.mkdir(arg['savedir'])

    for image in images:
        src = image.get_attribute('src')
        print(f'\rImages downloaded: {sucessfull}, errors: {0}', flush=True, end='')
        try:
            d = get(src)
            im = Image.open(BytesIO(d.content))
            if arg['gray']:
                im = im.convert('L')
            if arg['target_size'] != None:
                x, y = map(int, arg['target_size'].split(','))
                if x < im.width or y < im.height:
                    im = im.resize((x, y), Image.ANTIALIAS)
                else:
                    im = im.resize((x, y))
            im.save(f'{arg["savedir"]}/scraped_{sucessfull}.jpg')
            sucessfull += 1
        except:
            errors += 1
    print()
    driver.close()


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-se', '--searchterm', required=True, help='The string you want to search for')
    ap.add_argument('-sc', '--scrolls', help='Number of scrolls to perform', type=int, default=0)
    ap.add_argument('-sd', '--savedir', help='Where to save the data', default='data/')
    ap.add_argument('-gr', '--gray', help='1 for grayscale, 0 otherwise', type=int, default=0)
    ap.add_argument('-ts', '--target_size', help='Target size of images', default="200,50")
    args = vars(ap.parse_args())
    download(args)
