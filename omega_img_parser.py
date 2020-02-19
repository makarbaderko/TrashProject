import urllib.request
ur = "http://omega-48a1.local:8080/?action=snapshot"
filename = 'image_to_train'

def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

dl_jpg(ur, '/Users/makar/Documents/Programming/Project/imgs/', filename)
    