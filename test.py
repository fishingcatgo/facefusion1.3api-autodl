import os
 
# folder path
dir_path = r'./myimg/testimg'
 
# list file and directories
res = os.listdir(dir_path)
print('',res)


Absolute_Path=os.path.abspath(dir_path)
# file_list = os.listdir(dirname)

print('绝对路径：',Absolute_Path)


#返回指定路径下所有的文件名（不含目录）
def get_file(dir):
    file_list = []
    for item in os.listdir(dir):
        file_list.append(os.path.join(dir,item))
    return file_list


print('文件相对路径：',get_file(dir_path))


