import argparse
import os
from shutil import copyfile
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--concurrency', choices=['none','thread','process'], type=str,
                        default='none')
    parser.add_argument('--source', type=str,
                        default='/Users/gasia/Desktop/hw/assesment_2/test_1/')
    parser.add_argument('--destination', type=str,
                        default='/Users/gasia/Desktop/hw/assesment_2/test_2/')
    return parser.parse_args()


def copy_file(source_dest):
    return copyfile(source_dest[0], source_dest[1])

def run(src, dst, concurrency):
    if not os.path.exists(dst):
        os.makedirs(dst)
    files = os.listdir(src)
    source_destination_list = [[os.path.join(src, item), os.path.join(dst, item)] for item in files]

    print('Copying {:d} files... \n\t from {:s} \n\t to {:s}'.format(len(source_destination_list), src, dst))

    if concurrency == 'none':
        #result = [copy_file(src_dst) for src_dst in source_destination_list]
        result = map(copy_file, source_destination_list)

    elif concurrency == 'thread':
        print("Thread...")
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_list = [executor.submit(copy_file, (src_dst)) for src_dst in source_destination_list]
            result = [future.result() for future in future_list]
            #result = executor.map(copy_file, source_destination_list)

    elif concurrency == 'process':
        print("Process...")
        with ProcessPoolExecutor(max_workers=10) as executor:
            future_list = [executor.submit(copy_file, (src_dst)) for src_dst in source_destination_list]
            result = [future.result() for future in future_list]
            #result = executor.map(copy_file, source_destination_list)

    print('Copied files: \n\t{}'.format('\n\t'.join(list(result))))
    print('Copying files done.')

    
if __name__ == '__main__':
    args = parse_args()
    src = args.source
    dst = args.destination
    concurrency= args.concurrency

    run(src, dst, concurrency)
