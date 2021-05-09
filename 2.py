class Car:
 
    def __init__(self, model):
        self.model = model
 
    @property
    def model(self):
        return self.__model
 
    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model
 
    def getCarModel(self):
        return "Год выпуска модели " + str(self.model)
 
carA = Car(2088)  
print(carA.getCarModel())
