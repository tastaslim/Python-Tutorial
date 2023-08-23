import json
import threading
import time

import requests
from flask import Flask, Response

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    # 'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    # 'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    # 'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    # 'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    # 'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    # 'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    # 'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    # 'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    # 'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    # 'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    # 'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    # 'https://images.unsplash.com/photo-1550439062-609e1531270e',
    # 'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

start_time = time.time()

# from src.Amazon.AWS.s3.test import download_folders

app = Flask(__name__)


# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.

def home(img_url):
    print(f"Downloading {img_url}")
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


def second_home():
    threads = [threading.Thread(target=home, args=(url,)) for url in img_urls]
    for thread in threads:
        thread.start()

    # for thread in threads:
    #     thread.join()

    # with concurrent.futures.ThreadPoolExecutor() as executor:  # Introduced in python 3.2
    #     executor.map(home, img_urls)


@app.route('/test', methods=['POST'])
def exposed_controller():
    second_home()
    return Response(
        response=json.dumps({
            "data": {
                "message": 'file is being downloaded...'
            }
        }),
        status=200,
        mimetype="application/json"
    )


if __name__ == '__main__':
    app.run(debug=True)
