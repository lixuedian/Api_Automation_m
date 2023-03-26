"""
封装删除的方法
"""
import os
import shutil

from Common import Log


def delete_file(file_path):
    if os.path.exists(file_path):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        os.remove(file_path)
    else:
        Log.MyLog().info('删除文件不存在:%s' % file_path)  # 则返回文件不存在


def deletes_file(file_path):
    """删除一个非空目录"""
    if os.path.exists(file_path):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        shutil.rmtree(file_path)
        Log.MyLog().info('执行前先清除文件，文件删除成功:%s' % file_path)
    else:
        Log.MyLog().info('文件不存在请忽略信息:%s' % file_path)  # 则返回文件不存在


def delete_jpg(file_paths):
    if os.path.exists(file_paths) is False:
        print('输入的文件夹目录有误，请检查')
        return False
    try:
        for root, dirs, files in os.walk(file_paths):
            for file in files:
                file_path = os.path.join(root, file)
                if str(file_path.split('.')[-1]).upper() == 'JPG':
                    os.remove(file_path)
                    print('删除{}照片成功'.format(file_path))
    except Exception as e:
        print(e)

