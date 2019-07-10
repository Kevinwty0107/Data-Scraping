from multiprocessing import  Pool
from webspider import get_list_info
from webspider import url_host
from webspider import mainUrlStrs

#因为在观察赶集网的链接是我们发现o1..o2..是对应页面的页码，所有这里拼接每个页面的链接，这里以最多100页为测试
def get_all_list_info(url):
    for p in range(1,100):
        get_list_info(url + 'o' + str(p))


if __name__ == '__main__':#需加上这句代码，这时是一种固定的写法，作用是这句代码会把他上下分开两部分，避免我们改变地址时的名字混乱
    # 创建一个进程池，所有我们设计的爬虫，都会被放到进程池内，然后自动分配系统资源来执行
    # pool()有一个参数，processes，表示有多少个进程,比如processes=2
    pool = Pool()
    # 从所有频道列表中得到链接，
    # map()函数：会把后面的集合一个一个的放到第一个函数中执行
    # 参数1:一个函数
    # 参数2:一个集合
    for mainUrlStr in mainUrlStrs:
        # 拼接
        Urlstr = url_host + mainUrlStr.get('href')
        pool.map(get_all_list_info,Urlstr.split())
    pool.close()
    pool.join()