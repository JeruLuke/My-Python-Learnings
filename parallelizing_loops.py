import cv2
import os
import time
from joblib import Parallel, delayed

start_time = time.time()

path = r'C:\Users\selwyn77\Desktop'

#--- Check whether directory exists if not make one
new_dir = os.path.join(path, 'add_Weighted_3')
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

def weight(im):
    addweighted = cv2.addWeighted(im, 0.7, cv2.GaussianBlur(im, (15, 15), 0), 0.3, 0)
    return addweighted

for f in os.listdir(path):
    if f.endswith('.jpg') :
        img = cv2.imread(os.path.join(path, f))
        r = weight(img)
        cv2.imwrite(os.path.join(new_dir, f + '_add_weighted_.jpg'), r)
        

elapsed_time = time.time() - start_time
print(elapsed_time)


#--- Using joblib -----
start_time = time.time()

new_dir = os.path.join(path, 'add_Weighted__3_joblib')
if not os.path.exists(new_dir):
    os.makedirs(new_dir)
    
def joblib_loop():
#    Parallel(n_jobs=4)(delayed(weight)(f) if f.endswith('.jpg') for f in os.listdir(path))
    for f in os.listdir(path):
        if f.endswith('.jpg') :
            img = cv2.imread(os.path.join(path, f))
            r = delayed(weight)(img)
            cv2.imwrite(os.path.join(new_dir, f + '_add_weighted_.jpg'), r)

elapsed_time = time.time() - start_time
print(elapsed_time)