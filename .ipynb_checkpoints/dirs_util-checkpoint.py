import os
import shutil

#清空文件夹
def del_dirs(dir_path):
    # os.walk会得到dir_path下各个后代文件夹和其中的文件的三元组列表，顺序自内而外排列，
    # 如 log下有111文件夹，111下有222文件夹：[('D:\\log\\111\\222', [], ['22.py']), ('D:\\log\\111', ['222'], ['11.py']), ('D:\\log', ['111'], ['00.py'])]
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print('创建目录')
    else:   
        for root, dirs, files in os.walk(dir_path, topdown=False):
            # print(root) # 各级文件夹绝对路径
            # print(dirs) # root下一级文件夹名称列表，如 ['文件夹1','文件夹2']
            # print(files)  # root下文件名列表，如 ['文件1','文件2']
            # 第一步：删除文件
            for name in files:
                os.remove(os.path.join(root, name))  # 删除文件
            # 第二步：删除空文件夹
            for name in dirs:
                os.rmdir(os.path.join(root, name)) # 删除一个空目录

#创建文件夹
def cre_dirs(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print('创建目录')


#复制文件夹
def copy_dir(src_path,target_path):
    del_dirs(target_path)

    filelist_src = os.listdir(src_path)#用于返回一个文件名和目录名
    for file in filelist_src:#遍历所有的文件或文件夹
        src_path_read_new =os.path.join(os.path.abspath(src_path),file)
        target_path_write_new = os.path.join(os.path.abspath(target_path),file)
        if os.path.isdir(src_path_read_new):#判断该读入路径是否是目录文件夹，如果是文件夹执行递归
            if not os.path.exists(target_path_write_new):#判断目标路径是否存在该文件夹
                os.mkdir(target_path_write_new)#没有就创建文件夹
            copy_dir(src_path_read_new,target_path_write_new)#递归
        else:#如果是文件，执行复制
            shutil.copy(src_path_read_new,target_path_write_new)

    
#测试
if __name__ == "__main__":
    cre_dirs('./mydir/test/the/mygo/')
    del_dirs('./mydir/test')
    copy_dir('../mnt/tmp/config','../test')