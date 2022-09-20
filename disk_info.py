import shutil

def disk_percent_usage(directory);

'''
Return percentage usage of disk where percentage resides
'''
disk_info = shitil.disk_usage(directory)
return round(disk_info.used * 100 / disk_info.total, 2)