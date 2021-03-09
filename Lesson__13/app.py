class Car:
    def __init__(self, model):
        self.model = model
        self.engine_started = False
        self.trip_started = False
    
    def engine_start(self):
        if not self.engine_started:
            print(f"Машина {self.model} завелась")
            self.engine_started = True
    
    def engine_stop(self):
        if self.engine_started:
            print(f"Машина {self.model} заглохла")
            self.engine_started = False
            if self.trip_started:
                self.trip_end()
    
    def trip_start(self):
        if self.engine_started and not self.trip_started:
            print(f"У машины {self.model} началась поездка")
            self.trip_started = True

    def trip_end(self):
        if self.trip_started:
            print(f"У машины {self.model} поездка закончилась")
            self.trip_started = False
        

car_1 = Car("BMW")
car_1.engine_start()
car_1.trip_start()
car_1.engine_stop()

# car_2 = Car("Audi")
# car_2.engine_start()

# car_2.engine_stop()
