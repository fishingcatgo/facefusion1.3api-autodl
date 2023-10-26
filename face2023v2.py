
import os  
from facefusion import core2
import argparse


if __name__ == '__main__':
    
        
    data={
            'source_path': 'myimg/face/lun.jpg',
            'target_path': 'myimg/int/12s.mp4',
            'output_path': 'myimg/out',


            'skip_download': True,
            'headless': True,


            'execution_providers': ['cuda'],
            'execution_thread_count': 1,
            'execution_queue_count': 1,
            'max_memory': None,



            'face_recognition': 'reference',
            'face_analyser_direction': 'left-right',
            'face_analyser_age': None,
            'face_analyser_gender': None,
            'reference_face_position': 0,
            'reference_face_distance': 1.5,
            'reference_frame_number': 0,


            'trim_frame_start': None,
            'trim_frame_end': None,
            'temp_frame_format': 'jpg',
            'temp_frame_quality': 100,
            'keep_temp': False,


            'output_image_quality': 80,
            'output_video_encoder': 'libx264',
            'output_video_quality': 80,
            'keep_fps': False,
            'skip_audio': False,


            'frame_processors': ['face_swapper','face_enhancer'], #参数修改API必须用2 ,'frame_enhancer'
            'face_enhancer_model': 'gfpgan_1.4',
            'face_enhancer_blend': 100,
            'face_swapper_model': 'inswapper_128',
            'frame_enhancer_model': 'realesrgan_x2plus',
            'frame_enhancer_blend': 100,
            
            'ui_layouts': ['default']
        }
    

    # import argparse
    # args = argparse.Namespace(**data)
    # print('类型argparser：', type(args))
    # print('参数：',args)
    
    # core2.run(args)
    # print('处理完成')

    path_imgs = 'multivideo/'

    # os.makedirs(path_imgs+'/int')
    # os.makedirs(path_imgs+'/face')
    # os.makedirs(path_imgs+'/out')
   
    # import shutil
    # shutil.rmtree(path_imgs+'/out', ignore_errors=True)
    # os.makedirs(path_imgs+'/out')
    # quit('测试')


    imglist = os.listdir(path_imgs+'/int')
    facelist=os.listdir(path_imgs+'/face')
    
    print('视频路径：',imglist)
    print('脸路径：',facelist)

    imglist = list(filter(lambda x: x.endswith(('jpg','png','jpeg','bmp')), imglist))
    facelist = list(filter(lambda x: x.endswith(('jpg','png','jpeg','bmp')), facelist))
    print('过滤后：',imglist)
    print('过滤后：',facelist)

   
    for face in facelist:
        data['source_path']=path_imgs+'face/'+face
        (nameface, suffix) = os.path.splitext(face)
        print('文件名分割',nameface, suffix)
        
        dir_name=path_imgs+'out/'+'face'+nameface
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
    
        for value in imglist:
            # print('值：',path_imgs+value)
            # data['source_path']=path_imgs+'face/717.jpg'
            data['target_path']=path_imgs+'int/'+value
            data['output_path']=dir_name+'/'+value
            # data['output_path']=path_imgs+'out/'+'face'+nameface+'/'+value
            # print('数据：',data)
            args = argparse.Namespace(**data)
            core2.run(args)

    print('处理完成')
   
    

    
   



  