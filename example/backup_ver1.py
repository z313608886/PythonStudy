import os
import time
source = ['E:\\aaaa']
target_dir = 'E:\\backup'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  #创建目录

zip_command = 'zip - r {0} {1}'.format(target, ''.join(source))

print(zip_command)
if os.system(zip_command) == 0:
    print('successful',target)
else:
    print('backup failed')
