class SingletonClass():
#this singleton class can only be instantiated once

    __instance = None #this ensures that this class cannot be called outside of this code

    @staticmethod
    def getInstance():
        if SingletonClass.__instance == None:
            SingletonClass()
        return SingletonClass.__instance


    def __init__(self):
        if SingletonClass.__instance != None:
            raise Exception('this is a singleton')
        else:
            SingletonClass.__instance = self

test = SingletonClass()
print(test)
s = SingletonClass.getInstance()
print(s)

