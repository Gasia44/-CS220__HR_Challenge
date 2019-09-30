import os

if __name__ =='__main__':
    for i in range(10):
        command = "dd if=/dev/zero of=/Users/gasia/Desktop/hw/assesment_2/test_1/filename_{:s}.txt count=1024000 bs=1024".format(str(i))
        os.system(command)

