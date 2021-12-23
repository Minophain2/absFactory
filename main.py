from abc import abstractmethod, ABC
# абстрактная фабрика
class auto_factory(ABC):

    @abstractmethod
    def create_car(self):
        return Car

    @abstractmethod
    def create_bike(self):
        return Bike

class Car(ABC):

    @abstractmethod
    def set_wheels(self, wheels):
        pass

    @abstractmethod
    def set_seats(self, seats):
        pass

    @abstractmethod
    def set_engine(self, engine):
        pass

    @abstractmethod
    def set_airbags(self, airbags):
        pass

    @abstractmethod
    def set_gps(self, gps):
        pass


    @abstractmethod
    def get_wheels(self):
        pass

    @abstractmethod
    def get_seats(self):
        pass

    @abstractmethod
    def get_engine(self):
        pass

    @abstractmethod
    def get_airbags(self):
        pass

    @abstractmethod
    def get_gps(self):
        pass

class Bike(ABC):

    @abstractmethod
    def set_wheels(self, wheels):
        pass

    @abstractmethod
    def set_seats(self, seats):
        pass

    @abstractmethod
    def set_engine(self, engine):
        pass

    @abstractmethod
    def set_gps(self, gps):
        pass

    @abstractmethod
    def get_wheels(self):
        pass

    @abstractmethod
    def get_seats(self):
        pass

    @abstractmethod
    def get_engine(self):
        pass

    @abstractmethod
    def get_gps(self):
        pass

class Civilian_bike(Bike):

    def __init__(self):
        self.wheels = 0
        self.seats = 0
        self.engine = 0


    def set_seats(self, seats):
        self.seats = seats
        return self

    def set_wheels(self, wheels):
        self.wheels = wheels
        return self

    def set_engine(self, engine):
        self.engine = engine
        return self

    def get_wheels(self):
        return self.wheels

    def get_seats(self):
        return self.seats

    def get_engine(self):
        return self.engine

class Civilian_car(Car):

    def __init__(self):
        self.wheels = 0
        self.seats = 0
        self.engine = 0
        self.airbags = 0
        self.gps = False


    def set_seats(self, seats):
        self.seats = seats
        return self

    def set_wheels(self, wheels):
        self.wheels = wheels
        return self

    def set_engine(self, engine):
        self.engine = engine
        return self

    def set_airbags(self, airbags):
        self.airbags = airbags
        return self

    def set_gps(self, gps):
        self.gps = gps
        return self

    def get_wheels(self):
        return self.wheels

    def get_seats(self):
        return self.seats

    def get_engine(self):
        return self.engine

    def get_airbags(self):
        return self.airbags

    def get_gps(self):
        return self.gps

class civilian_auto_factory(auto_factory):

    def create_bike(self,wheels, seats, engine):
        civil_bike = Civilian_bike().set_wheels(wheels).set_seats(seats).set_engine(engine)
        return civil_bike


    def create_car(self,wheels,seats,engine,airbags,gps):
        civilian_car = Civilian_car().set_wheels(wheels).set_seats(seats).set_engine(engine).set_airbags(airbags).set_gps(gps)
        return civilian_car

bike_factory = civilian_auto_factory()
my_bike = bike_factory.create_car(2,1,'z-500',3,True)

print('wheels:\t'+str(my_bike.get_wheels()))
print('seats:\t'+str(my_bike.get_seats()))
print('engine:\t'+my_bike.get_engine())
