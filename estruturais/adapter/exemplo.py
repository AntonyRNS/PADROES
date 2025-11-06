class Target:
    def request(self):
        return "Target: The default target's behaviour."

class Adaptee:
    def  specific_request(self):
        return "Different behaviour."

class Adapter(Target):
    def __init__(self, aux):
        self.adaptee = aux
    def request(self):
        aux = self.adaptee.specific_request()
        return aux



def client_code(target: "Target"):
    print(target.request())

if __name__ == "__main__":
    print("=======1=========")
    target = Target()
    client_code(target)
    print("================")
    print("=======2=========")
    adaptee = Adaptee() 
    adapter = Adapter(adaptee)
    target = Target()
    client_code(adapter)
    print("================")