from multiprocessing import Lock, Pool
import time
 
 
def function(index):
    print 'Start process: ', index
    time.sleep(3)
    print 'End process', index
 
 
if __name__ == '__main__':
    pool = Pool(processes=2)
    for i in xrange(4):
        pool.apply_async(function, (i,))
 
    print "Started processes"
    pool.close()
    pool.join()
    print "Subprocess done."