class student:
    def __init__(self, name, sid, batch):
        self.name = name
        self.id = sid
        self.batch = batch
    
    def showdata(self):
        print('Name:', self.name)
        print('ID:', self.id)
        print('Batch:', self.batch)

    
