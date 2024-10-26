import numpy as np
import requests
from matplotlib import pyplot as plt

request_ = requests.get('https://urban-university.ru')
print(request_)
request_ = requests.post('https://urban-university.ru/post', data = {'key':'value'})
print(request_)
request_ = requests.head('https://urban-university.ru/get')
print(request_)
request_ = requests.options('https://urban-university.ru/get')
print(request_)


array = np.arange(15).reshape(3,5)
print(array)
array_a = np.arange(15).reshape(3,5)
array_b = np.arange(15).reshape(3,5)
array_c = array_a * array_b
print(array_c)
array = np.arange(15).reshape(3,5)
print(np.cos(array))


fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4, 3, 8, 6, 9, 2,], [1, 4, 2, 3, 8, 5, 3, 5, 6])
plt.show()

