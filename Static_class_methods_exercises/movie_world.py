class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10


    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)
            return

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)
            return

    def rent_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if dvd in customer.rented_dvds:
                            return f'{customer.name} has already rented {dvd.name}'
                        elif dvd not in customer.rented_dvds and dvd.is_rented:
                            return f'DVD is already rented'
                        elif not dvd.is_rented and customer.age >= dvd.age_restriction:
                            customer.rented_dvds.append(dvd)
                            dvd.is_rented = True
                            return f'{customer.name} has successfully rented {dvd.name}'
                        elif not dvd.is_rented and customer.age < dvd.age_restriction:
                            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        dvd.is_rented = False
                        customer.rented_dvds.remove(dvd)
                        return f'{customer.name} has successfully returned {dvd.name}'

                return f'{customer.name} does not have that DVD'




    def __repr__(self):
        result = ''

        for custom in self.customers:
            result += custom.__repr__()
            result += '\n'

        for dvd in self.dvds:
            result += dvd.__repr__()
            result += '\n'

        return result
