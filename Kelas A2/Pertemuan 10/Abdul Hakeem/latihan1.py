class sim_cache:
    def __new__(cls):
        if not hasattr(cls, 'cache'):
            cls.cache = super().__new__(cls)
        return cls.cache
    
    def __init__(self):
        self.namaweb = 'PBOTRI'
        self.createcache()
    
    def createcache(self):
        self.cachesource = self.namaweb + ".txt"
        self.cachename = "cache_"+self.namaweb+".txt"
        sf = open(self.cachesource, 'r') #opening source file
        cf = open(self.cachename, 'w') #opening cache file
        cf.write(f"Ini adalah file cache dari web {self.namaweb}\n")
        line1 = False
        for l in sf:
            if "Startcache" in l:
                line1 = True
            if line1 == True:
                cf.write(l)
    def getcache(self):
        if not self.cache:
            self.cache = sim_cache()
        print(f'Nama file cache adalah {self.cache.cachename}')
        cf = open(self.cache.cachename, 'r')
        print(cf.read())

print('=====First instantiation=====')
cache1 = sim_cache()
cache1.getcache()

print('=====Second instantiation=====') 
cache2 = sim_cache()
add_cache = open("cache_PBOTRI.txt", "a")
add_cache.write('\n**extra line in cache**')
add_cache.close()
cache2.getcache()