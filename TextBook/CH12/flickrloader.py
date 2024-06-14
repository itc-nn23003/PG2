import requests, sys, os, bs4

MAX_IMAGES = 10

print('Serching...')
res = requests.get('https://flickr.com/search/?text=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

os.makedirs('images', exist_ok=True)

soup = bs4.BeautifulSoup(res.text, 'html.parser')
imgs = soup.select('.photo-list-photo-view img')

for i in range(min(MAX_IMAGES, len(imgs))):
    img_url = imgs[i].get('src')
    print('https:' + img_url)

    img_res = requests.get('https:' + img_url)
    img_res.raise_for_status()
    img_file = open(os.path.join('images', os.path.basename(img_url)), 'wb')
    for chunk in img_res.iter_content(100000):
        img_file.write(chunk)
    img_file.close()

