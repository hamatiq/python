from datetime import datetime
class Tweet:
    def __init__(self,auther,text):
        
        self.__auther = auther
        self.__text = text
        self.__age = datetime.now()
    
    def get_auther(self):
        return (str(self.__auther))
    
    def get_text(self):
        return (str(self.__text))

    def get_age(self):
        x = datetime.now()-self.__age
        return (x)

    def print_tweet(self):
        x= self.get_age()
        x = str(x).split()
        if (len(x) > 1):
            x = x[1].split('.')
            x = x[0].split(':')
            if(int(x[0])>0):
                x=(str(x[0]+'h,'))
            elif (int(x[1]) > 0):
                x=(str(x[1]+'m,'))
            else:
                x=(str(x[2]+'s.'))
        else:
            x = x[0].split('.')
            x = x[0].split(':')
            if(int(x[0])>0):
                x=(str(x[0]+'h,'))
            elif (int(x[1]) > 0):
                x=(str(x[1]+'m,'))
            else:
                x=(str(x[2]+'s.'))
        print(self.get_auther()+ ' - '+ x)
        print(self.get_text())
