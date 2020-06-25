## By Kat Sullivan

import pandas as pd
import sys

with open(sys.argv[1], "r") as file:
	filedata = file.read()

df = pd.read_csv(sys.argv[2])
fuse_names = df['NonApple']
apple_names = df['Apple']

for idx,name in enumerate(fuse_names):
	# print(apple_names[idx])
	filedata = filedata.replace(name, apple_names[idx])

with open(sys.argv[1], 'w') as file:
	file.write(filedata)



