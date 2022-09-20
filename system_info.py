import platform

def kernel_info():
    '''
    Return linux kernel information
    '''
    kernel_info = platform.uname();
    return {"details": kernel_info.release, "version": kernel_info.version}
