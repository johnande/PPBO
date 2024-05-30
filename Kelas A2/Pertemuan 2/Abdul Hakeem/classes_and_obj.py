import qrcode

class qr:
    def __init__(self, l, fn):
        self.link = l
        self.name = fn
    
    def showattr(self):
        print('Link:', self.link)
        print('Name:', self.name)

    def createqr(self):
        img = qrcode.make(self.link)
        img.save(f'''{self.name}.png''')

qr1 = qr('https://www.google.com', 'Google') # this is an object