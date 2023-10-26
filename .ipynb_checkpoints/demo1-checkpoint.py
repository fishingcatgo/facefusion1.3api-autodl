
import os  
from facefusion import core2

if __name__ == '__main__':
    
        
    data={
            'source_path': 'myimg/face/lun.jpg',
            'target_path': 'myimg/int/12s.mp4',
            'output_path': 'myimg/out',


            'skip_download': False,
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


            'frame_processors': ['face_swapper', 'face_enhancer'], #参数修改API必须用2
            'face_enhancer_model': 'gfpgan_1.4',
            'face_enhancer_blend': 100,
            'face_swapper_model': 'inswapper_128',
            'frame_enhancer_model': 'realesrgan_x2plus',
            'frame_enhancer_blend': 100,
            
            'ui_layouts': ['default']
        }
    import argparse
    args = argparse.Namespace(**data)
    print('类型argparser：', type(args))
    print('参数：',args)
    
    core2.run(args)
    print('处理完成')
    
    
    # data={
    #     'source_path':'myimg/face/lun.jpg',
    #     'target_path':'myimg/int/12s.mp4',
    #     'output_path':'myimg/out',
    #     'frame_processor':['face_swapper', 'face_enhancer'],  #是否开启：face_swapper换脸，face_enhancer脸部修复，['face_swapper', 'face_enhancer']
    #     'keep_fps':True, 
    #     'keep_frames':False, 
    #     'skip_audio':True,
    #     'many_faces':False,
    #     'reference_face_position':0,   #图片中选取要换的脸（处理要换脸图片人脸位置,指定图片中的哪张脸）
    #     'reference_frame_number':0,    #视频中选取要换的脸（处理视频时用指定要换哪个人脸，reference_frame_number是视频的哪一帧，reference_face_position所在帧的哪个脸是本视频要换的）
    #     'similar_face_distance':0.85, #设置脸的识别距离
    #     'temp_frame_format':'png', 
    #     'temp_frame_quality':0, 
    #     'output_video_encoder':'libx264',
    #     'output_video_quality':50, #设置输出视频的质量，[0-100] 
    #     'max_memory':60, 
    #     'execution_provider':['cuda'],
    #     'execution_threads':12
    #     }
    
#     path_imgs = 'multivideo/'
#     imglist = os.listdir(path_imgs+'/int')
#     facelist=os.listdir(path_imgs+'/face')
    
#     print('视频路径：',imglist)
#     print('脸路径：',facelist)
    
#     for face in facelist:
#         data['source_path']=path_imgs+'face/'+face
        
# #         (nameface, suffix) = os.path.splitext(face)
# #         print('文件名分割',nameface, suffix)
        
# #         dir_name=path_imgs+'out/'+'face'+nameface
# #         if not os.path.isdir(dir_name):
# #             os.makedirs(dir_name)
    
#         for value in imglist:
#             # print('值：',path_imgs+value)


#             # data['source_path']=path_imgs+'face/717.jpg'
#             data['target_path']=path_imgs+'int/'+value
#             # data['output_path']=dir_name+'/'+value
#             data['output_path']=path_imgs+'out/'+value
#             # print('数据：',data)
#             core3.run(data)



  