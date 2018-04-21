# Google Images Webscraper
A simple python script to download any number of images from google images.

## Chromedriver
Since the script uses a chromedriver this need to be added to the same folder as the python file ('download_images.py')
download from: [link](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Arguments
| Argument      | Short         | Description                                                                                                               |
|------------   |-------------  |------------------------------------------------------------------------------------------------------------------------   |
| searchterm    | se            | The keyword you want to search for                                                                                        |
| n_images       | ni            |  Target number of images    |
| savedir       | sd            | Where to save the images                                                                                                  |
| gr            | gray          | 1 to save the images as grayscale, 0 otherwise                                                                            |
| ts            | target_size   | Target size of downloaded images.                                                                                         |
## Examples
#### Download 100 images of Pikachu
```console
MacBook-Pro:~ User$ python download_images.py -se 'Pikachu' -ni 100 -sd 'data/Pikachu_raw/'
Found 100 results
Images downloaded: 98, errors: 2
```
We ended up saving 98 images since we had two errors. Sample from data/Pikachu_raw/

![scraped_0.png](data/Pikachu_raw/scraped_0.png "scraped_0.png") ![scraped_1.png](data/Pikachu_raw/scraped_1.png "scraped_1.png")

However we might want them in the same size. Lets try using a target size.

#### Download 100 images of Pikachu with target size 128x128
```console
MacBook-Pro:~ User$ python download_images.py -se 'Pikachu' -ni 100 -sd 'data/Pikachu_128/' -ts 128,128
Found 100 results
Images downloaded: 98, errors: 2
```
We ended up saving 98 images since we had two errors. Sample from data/Pikachu_128/

![scraped_0.png](data/Pikachu_128/scraped_0.png "scraped_0.png") ![scraped_1.png](data/Pikachu_128/scraped_1.png "scraped_1.png")![scraped_2.png](data/Pikachu_128/scraped_2.png "scraped_2.png")![scraped_3.png](data/Pikachu_128/scraped_3.png "scraped_3.png")![scraped_4.png](data/Pikachu_128/scraped_4.png "scraped_4.png")![scraped_5.png](data/Pikachu_128/scraped_5.png "scraped_5.png")

Again, we might want something else. Lets try to download 600 images of Pikachu, in grayscale and with a smaller target size 64x64.

#### Download 600 images of Pikachu in grayscale with target size 64x64
```console
MacBook-Pro:~ User$ python python download_images.py -se 'Pikachu' -ni 600 -sd 'data/Pikachu_gr64/' -gr 1 -ts 64,64
Found 537 results
Images downloaded: 523, errors: 14
```
We ended up saving 523 images since we had 14 errors and only found 537 images to begin with. If this becomes a problem in terms of really wanting 600 images just increase the target number of images, I.g use '-ni 700' instead. 

Sample from data/Pikachu_128/

![scraped_0.png](data/Pikachu_gr64/scraped_0.png "scraped_0.png") ![scraped_1.png](data/Pikachu_gr64/scraped_1.png "scraped_1.png")![scraped_2.png](data/Pikachu_gr64/scraped_2.png "scraped_2.png")![scraped_3.png](data/Pikachu_gr64/scraped_3.png "scraped_3.png")![scraped_4.png](data/Pikachu_gr64/scraped_4.png "scraped_4.png")![scraped_5.png](data/Pikachu_gr64/scraped_5.png "scraped_5.png")![scraped_6.png](data/Pikachu_gr64/scraped_6.png "scraped_6.png")![scraped_7.png](data/Pikachu_gr64/scraped_7.png "scraped_7.png")![scraped_8.png](data/Pikachu_gr64/scraped_8.png "scraped_8.png")![scraped_9.png](data/Pikachu_gr64/scraped_9.png "scraped_9.png")![scraped_10.png](data/Pikachu_gr64/scraped_10.png "scraped_10.png")![scraped_11.png](data/Pikachu_gr64/scraped_11.png "scraped_11.png")![scraped_12.png](data/Pikachu_gr64/scraped_12.png "scraped_12.png")
