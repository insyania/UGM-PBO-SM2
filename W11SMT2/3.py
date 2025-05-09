class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2},
        'sms': {'number': 1000, 'price': 10},
        'voice': {'number': 1000, 'price': 15},
    }

# View
class View(object):
    def list_services(self, services):
        print("Services Provided:")
        for svc in services:
            print(f"- {svc}")

    def list_pricing(self, services):
        print("Pricing for Services:")
        for svc in services:
            data = Model.services[svc]
            print(f"For {data['number']} {svc} messages, you pay ${data['price']}")
            
class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_services(self):
        services = self.model.services.keys()
        self.view.list_services(services)

    def get_pricing(self):
        services = self.model.services.keys()
        self.view.list_pricing(services)

    def bid_price(self):
        while True:
            tawar = input("Enter the service you want to bid on (email/sms/voice): ").lower()
            if tawar in self.model.services:
                harga = int(input("Enter your bid price: "))
                self.model.services[tawar]['price'] = harga
                print("Price according to your bid")
                self.get_pricing()
                break
            else:
                print("Service not found!")

# Main program
controller = Controller()
controller.get_services()
controller.bid_price()
