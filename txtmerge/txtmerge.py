import os
print (os.getcwd())
path= '/Users/wangtaiyi/Desktop/搜狐实习/game pic'
os.chdir(path)
print (os.getcwd())
filedir = os.getcwd()+'/5'
#获取当前文件夹中的文件名称列表
filenames=os.listdir(filedir)
#filenames.remove('.DS_Store')
print (filenames)
#打开当前目录下的result.txt文件，如果没有则创建
f=open('result1234.txt','r+')
#先遍历文件名
for filename in filenames:
    filepath = filedir+'/'+filename
    f1 = open(filepath,'r+')
    print (f1)
    #遍历单个文件，读取行数
    for line in f1:
        f.writelines(line)
    f.write('\n')
#关闭文件
f.close()

