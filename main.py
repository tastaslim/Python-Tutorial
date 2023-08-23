from threading import Thread
from time import time

import requests
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    url: list[str]


app = FastAPI()


@app.post("/")
def download_images(item: Item):
    try:
        start_time = time()

        def download_image(img_url):
            print(f"Downloading {img_url}")
            img_bytes = requests.get(img_url).content
            img_name = img_url.split('/')[3]
            img_name = f'{img_name}.jpg'
            with open(f'photos/{img_name}', 'wb') as img_file:
                img_file.write(img_bytes)
                print(f'{img_name} was downloaded...')

        img_urls = item.url
        threads = [Thread(target=download_image, args=[image]) for image in img_urls]
        for thread in threads:
            thread.start()
        print(f'Time taken: {time() - start_time}')
        return {"message": "Downloading the images"}
    except Exception as e:
        print(e)
