import time
from tqdm import tqdm_gui

my_list = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']

for i in tqdm_gui(my_list):
    time.sleep(2)
    print(i)