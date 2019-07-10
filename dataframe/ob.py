import time

#每10秒查询一次数据库数据总数
while True:
    print('数据库已写入--{}--条数据'.format(list_info.find().count()))
    time.sleep(10)

