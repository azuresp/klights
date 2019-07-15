from datetime import datetime, timedelta
import kitetalker

class null():
    def setcolor(self, newcolor, ignorecolor):
        x=1
    def runtick(self):
        x=1

class plain():
    def __init__(self, kite, startcolor):
        self.color = startcolor
        self.kite = kite
        self.setcolor(startcolor, startcolor)

    def setcolor(self, newcolor, ignorecolor):
        self.color = newcolor
        print("setting " + newcolor.text() + ", " + newcolor.text())
        self.kite.send(newcolor,ignorecolor)

    def runtick(self):
        noop=True
        #no-op

class alternating():
    def __init__(self, kite, startcolor1, startcolor2):
        self.kite=kite
        self.pattern_duration=timedelta(microseconds=1000*1000)
        self.show_primary=1
        self.show_secondary=2
        self.show_current=0
        self.color1=startcolor1
        self.color2=startcolor2
        self.pattern_start=datetime.now()

    def setcolor(self, newcolor1, newcolor2):
        self.color1=newcolor1
        self.color2=newcolor2

    def __showcolor(self, leftcolor, rightcolor):
        print("setting " + leftcolor.text() + ", " + rightcolor.text())
        self.kite.send(leftcolor,rightcolor)

    def reset_show(self, showmode):
        self.pattern_start=datetime.now()
        if(showmode==self.show_primary):
            #print('changing from primary')
            self.__showcolor(self.color1,self.color2)
        elif(showmode==self.show_secondary):
            #print('changing from secondary')
            self.__showcolor(self.color2,self.color1)
        self.show_current = showmode

        
    def runtick(self):
        tdelta = datetime.now()-self.pattern_start
        if tdelta > self.pattern_duration:
            if(self.show_current==self.show_primary):
                self.reset_show(self.show_secondary)
            else:
                self.reset_show(self.show_primary)
