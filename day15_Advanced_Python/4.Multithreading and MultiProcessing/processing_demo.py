from concurrent.futures import ProcessPoolExecutor
from time import perf_counter

from PIL import Image, ImageFilter

img_names = [
    "photos/photo-1549692520-acc6669e2f0c.jpg",
    "photos/photo-1550439062-609e1531270e.jpg",
    "photos/photo-1493976040374-85c8e12f0c0e.jpg",
    "photos/photo-1504198453319-5ce911bafcde.jpg",
    "photos/photo-1507143550189-fed454f93097.jpg",
    "photos/photo-1513938709626-033611b8cc03.jpg",
    "photos/photo-1516117172878-fd2c41f4a759.jpg",
    "photos/photo-1516972810927-80185027ca84.jpg",
    "photos/photo-1522364723953-452d3431c267.jpg",
    "photos/photo-1524429656589-6633a470097c.jpg",
    "photos/photo-1530122037265-a5f1f91d3b99.jpg",
    "photos/photo-1530224264768-7ff8c1789d79.jpg",
    "photos/photo-1532009324734-20a7a5813719.jpg",
    "photos/photo-1541698444083-023c97d3f4b6.jpg",
    "photos/photo-1564135624576-c5c88640f235.jpg"
]


def process_image(img_name):
    size = (1200, 1200)
    img = Image.open(img_name)
    print(f'{img_name} is being processed...')
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'{img_name}')
    print(f'{img_name} was processed...')


if __name__ == "__main__":
    t1 = perf_counter()
    with ProcessPoolExecutor() as executor:
        executor.map(process_image, img_names)
    t2 = perf_counter()
    print(f'Finished in {t2 - t1} seconds')
