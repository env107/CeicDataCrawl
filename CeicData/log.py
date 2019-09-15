import time
import traceback
import os
_logLevel = [ 'debug' , 'error' , "warn"]
_logpath = "pylog/"

def debug(text):
    return write(text,'debug');

def warn(text):
    return write(text,'warn');

def error(text):
    return write(text,'error');

#将内容写到日志文件中
def write(text,level = 'debug'):
    level = str(level).lower()
    if (level not in _logLevel) :
        level = 'debug' #默认选择debug级别的日志
    pass
    timefmat = "%Y%m%d"
    text = " > [" + _localTime("%Y-%m-%d %H:%M:%S") +" #" + level+"] " + str(text) + "\n" #强制将内容转换成字符串
    path = os.getcwd()+ "/" +_logpath + level + "/" + _localTime(timefmat)
     #首先检查目录是否存在
    if not os.path.exists(path):
        os.makedirs(path,0o755); 
    return _writeFile(path,text)
pass


#将内容写入文本
def _writeFile(path , text):  
    try:
        file = path + "/" + _localTime("%H") + ".log"
        return open(file , "a").write(text)
    except BaseException:
        print("[Python Program Error]:" , traceback.format_exc());

#按格式输出时间
def _localTime(fmat = "%Y-%m-%d %H:%M:%S"):
    return str(time.strftime(fmat,time.localtime()))
        



    
