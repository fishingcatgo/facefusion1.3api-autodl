
import dirs_util
   
#测试
if __name__ == "__main__":
    # dirs_util.cre_dirs('./mydir/test/the/mygo/')
    # dirs_util.del_dirs('./mydir/test')
    # dirs_util.copy_dir('../mnt/tmp/config','../test')

    dirs_util.del_dirs('./multivideo')
    for i in ['face','int','out']:
        print(i)
        dirs_util.cre_dirs(f'./multivideo/{i}')