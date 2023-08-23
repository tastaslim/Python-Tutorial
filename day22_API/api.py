import json
import os
import time
from wsgiref import simple_server

import falcon
import requests

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

start_time = time.time()


class FalconTest:
    @staticmethod
    def on_post_bar(req, resp):
        req1 = json.loads(req.stream.read())
        img_bytes = requests.get(req1['img_url']).content
        img_name = req1['img_url'].split('/')[3]
        img_name = f'{img_name}.jpg'
        with open(img_name, 'wb') as img_file:
            img_file.write(img_bytes)
            print(f'{img_name} was downloaded...')
        resp.status = falcon.HTTP_200
        resp.text = json.dumps({'message': 'Image downloaded successfully'})
        return resp

    @staticmethod
    def on_get_demo(req, resp):
        resp.text = json.dumps(
            {"author": "Jack", "name": "Pirates"})
        resp.status = falcon.HTTP_200
        return resp


app = application = falcon.App()
app.add_route("/demo", FalconTest(), suffix="demo")
app.add_route("/bar", FalconTest(), suffix="bar")

if __name__ == '__main__':
    with simple_server.make_server('', os.getenv('PORT', 5200), app) as httpd:
        print("Serving on port 5200...")
        httpd.serve_forever()
