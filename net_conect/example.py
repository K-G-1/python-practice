#!/usr/bin/python
# coding:utf-8


def test1():
    import os
    return1 = os.system('ping www.baidu.com')
    if return1:
        print 'ping fail'
    else:
        print 'ping ok'


def test2():
    import os
    import subprocess

    fnull = open(os.devnull, 'w')
    return1 = subprocess.call(
        'ping www.baidu.com', shell=True, stdout=fnull, stderr=fnull)
    if return1:
        print 'ping fail'
    else:
        print 'ping ok'
    fnull.close()


if __name__ == '__main__':
    test1()
