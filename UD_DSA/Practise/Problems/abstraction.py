from abc import ABC,abstractmethod

class Device(ABC):

    def __init__(self,value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def deviceTask(self):
        print("I will print something now")
        pass

class Phone(Device):

    def __init__(self,value,company):
        self.company = company
        super().__init__(value)
    
    def deviceTask(self):
        super().deviceTask()
        print("Device value: ",self.value)
        print("Device company: ",self.company)

# device = Device() #This will throw an error
phone1 = Phone("SmartPhone","LG")
phone2 = Phone("FeaturePhone","Samsung")

phone1.deviceTask()
phone2.deviceTask()