class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2},
        'sms': {'number': 1000, 'price': 10},
        'voice': {'number': 1000, 'price': 15},
    }

class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc, '')

    def list_pricing(self, services):
        for svc in services:
            print("For", Model.services[svc]['number'],
                  svc, "message you pay $", Model.services[svc]['price'])

class View2(object):
    def list_services(self, services):
        for svc in services:
            print(svc, '')

    def list_pricing(self, services):
        for svc in services:
            print("Untuk", Model.services[svc]['number'],
                  svc, "pesan yang anda bayar $", Model.services[svc]['price'])

# Controller
class Controller(object):
    def __init__(self, lang_choice):
        self.model = Model()
        if lang_choice == '1':
            self.view = View2()
        else:
            self.view = View()

    def get_services(self):
        services = self.model.services.keys()
        return self.view.list_services(services)

    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)

while True:
    print("Choose Language / Pilih Bahasa :")
    print("1. Bahasa Indonesia")
    print("2. English")
    jawab = input("Masukkan pilihan Anda (1/2): ")

    if jawab == '1':
        print("Anda memilih Bahasa Indonesia.")
        break
    elif jawab == '2':
        print("You chose English.")
        break
    else:
        print("Pilihan yang anda masukkan salah. Silakan coba lagi.\n")
4
controller = Controller(jawab)
print("Services Provided:" if jawab != '1' else "Layanan Tersedia:")
controller.get_services()
print("Pricing for Services:" if jawab != '1' else "Harga Layanan:")
controller.get_pricing()

