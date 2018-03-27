import datetime

def generate(err):
    try:
        f = open('./logs/log_'+getTime()+'.txt', 'w')
        f.write(str(err))
        f.close()
    except Exception as ex:
        raise ex

def getTime():
    now = datetime.datetime.now().strftime("%Y-%m-%d %Hh%Mm%S")
    date = now[0:10]
    time = now[11:19]
    return date+'_'+time