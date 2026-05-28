class Instagram:
    def __init__(self,username,password,cf):
        self.username=username
        self.__password=password
        self._cf=cf
    def getpassword(self):
        return self.__password
    def setpassword(self, new_password):
        self.__password=new_password
        
    @property
    def accesscf(self):
        return self._cf
    
    @accesscf.setter
    def accesscf(self,new_friend):
        self._cf.append(new_friend)


charan=Instagram("charan","charan@26",["surya","prince","varun"])
print("username:",charan.username)
charan.username="sahil"
print("After username:",charan.username)

print("Before password:",charan.getpassword())
charan.setpassword('sahil@123')
print("after password:",charan.getpassword())

print("before close friend:",charan.accesscf)
charan.accesscf='laksmikanth'
print("After closefriend:",charan.accesscf)
