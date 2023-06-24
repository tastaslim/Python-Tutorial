import concurrent.futures
import time

import requests

# Step - 1 : --------------------- Without Multithreading ----------------------------
"""
# Blocking peace of code. Where each line will be executed one after another. and code will
# take around 2 seconds to execute.

start_time = time.time()
def test():
    print("Hello")
    time.sleep(1)
    print("World")

test()
test()

print(f'End time : {time.time() - start_time}')

"""

# Step - 2 : --------------------- With Multithreading ----------------------------

"""
# Non blocking peace of code. Where function will be executed in parallel using multiple threads.

start_time = time.time()
def test():
    print("Hello")
    time.sleep(1)
    print("World")

t1 = threading.Thread(target=test)
t2 = threading.Thread(target=test)
t1.start()  # to start thread execution
t2.start()
t1.join()  # to wait for thread to finish execution. Once thread has finished execution, it will kill the thread and continue with the code.
t2.join()
print(f'End time : {time.time() - start_time}')

"""

# Step - 3 : --------------------- Without Multithreading real life example----------------------------
"""
# To download multiple files from internet. This approach will download files one by one .

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

def download_image(img_url):
    print(f"Downloading {img_url}")
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


for url in img_urls:
    download_image(url)

print(f'Total time : {time.time() - start_time}')
"""

# Step - 4 : --------------------- With Multithreading real life example----------------------------

# img_urls = [
#     'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
#     'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
#     'https://images.unsplash.com/photo-1524429656589-6633a470097c',
#     'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
#     'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
#     'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
#     'https://images.unsplash.com/photo-1522364723953-452d3431c267',
#     'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
#     'https://images.unsplash.com/photo-1507143550189-fed454f93097',
#     'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
#     'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
#     'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
#     'https://images.unsplash.com/photo-1516972810927-80185027ca84',
#     'https://images.unsplash.com/photo-1550439062-609e1531270e',
#     'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
# ]

# start_time = time.time()
# print(start_time)
#
#
# def download_image(img_url):
#     print(f"Downloading {img_url}")
#     img_bytes = requests.get(img_url).content
#     img_name = img_url.split('/')[3]
#     img_name = f'{img_name}.jpg'
#     with open(img_name, 'wb') as img_file:
#         img_file.write(img_bytes)
#         print(f'{img_name} was downloaded...')
#

"""
threads = []
for url in img_urls:
    t = threading.Thread(target=download_image, args=(url,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print(f'Total time : {time.time() - start_time}')

"""
# Above code is same as below code
# threads = [threading.Thread(target=download_image, args=(img_url,)) for img_url in img_urls]
# for thread in threads:
#     thread.start()
#
# for thread in threads:
#     thread.join()
# print(f'Time taken: {time.time() - start_time}')

# Step - 5 : --------------------- With Multithreading real life example ( Clean code using threadPool executer) ----------------------------


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


def download_image(img_url):
    print(f"Downloading {img_url}")
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


"""
Best part about ThreadPoolExecutor is that it will automatically create threads for us and will also manage the threads for us.
It will also wait for all the threads to finish before moving on to the next line of code. Checks for idle threads and assigns. Creates new
threads if needed. Implements Semaphore under the hood to handle thread deadlock. implements thread locking etc.
Lock that ensures that new workers are not created while the interpreter is shutting down. Must be held while mutating 
_threads_queues and _shutdown.
Also same module can be used for multiprocessing. Just replace ThreadPoolExecutor with ProcessPoolExecutor. We will check 
this in next tutorial.
"""
with concurrent.futures.ThreadPoolExecutor() as executor:  # Introduced in python 3.2
    executor.map(download_image, img_urls)

print(f'Total time : {time.time() - start_time}')
