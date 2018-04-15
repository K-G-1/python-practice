#coding:utf-8
import logging

logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)

#输出到文件
fh = logging.FileHandler("/home/kg/log2.log")
fh.setLevel(logging.INFO)
#设置日志格式
fomatter = logging.Formatter('%(asctime)s -%(name)s-%(levelname)s-%(module)s:%(message)s')
fh.setFormatter(fomatter)
logger.addHandler(fh)
logger.debug("debug message")
name ='顾影'
logger.info(name)
logger.warning("warning 信息")
logger.error("error 信息")
logger.critical("critical message")