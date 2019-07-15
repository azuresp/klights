class color:
    def __init__(self):
        self.r=0
        self.g=0
        self.b=0
        self.label="black"

    def __init__(self, label,r,g,b):
        self.r=r
        self.g=g
        self.b=b
        self.label=label
        
    def text(self):
        return self.label + '(' + str(self.r) + ',' + str(self.g) + ',' + str(self.b) + ')'

    #color table from https://www.w3schools.com/colors/colors_picker.asp?colorhex=ff0000
    def red():
        return color("red", 255, 0,0)
    
    def orange():
        return color("orange", 255, 128, 0)

    def yellow():
        return color("yellow",255,255,0)

    def blue():
        return color("blue",0,0,255)
    
    def indigo():
        return color("indigo", 128,0,255)

    def violet():
        return color("violet", 255,0,255)
    
    def white():
        return color("white", 255,255,255)
    def black():
        return color("black",0,0,0)
    def green():
        return color("green",0,255,0)

