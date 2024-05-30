import qrcode

def createqr(cls):
    def newqr(self, data, fn):
        qr = qrcode.make(data)
        qr.save(f"{fn}.png")
    cls.newqr = newqr
    return cls

@createqr
class qrclass:
    pass

obj = qrclass()
obj.newqr(data="porfiriko.live/laprak", fn = "laprak") 