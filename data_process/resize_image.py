# coding:utf-8
import os

path = 'C:/Users/yunxu/Desktop/taotao/bag'
i = 1
for file in os.listdir(path):
	if os.path.isfile(os.path.join(path, file)):
		if os.path.splitext(os.path.join(path, file))[1] == '.jpg':
			newname = '%06d' % (i) + '.jpg'
			os.rename(os.path.join(path, file), os.path.join(path, newname))
			# join 将路径和文件名合并
			i = i+1
			print(file, 'ok')
		# print (file.split('.')[-1])
		# 按照路径将文件名和路径分割开
