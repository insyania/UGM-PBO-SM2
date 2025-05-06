class SingletonClass: 
    _instance = None 
    def __new__(cls, *args, **kwargs):
        print("Status instance = ", cls._instance) 
        if not cls._instance: 
            cls._instance = super().__new__(cls) 
        return cls._instance 
    def __init__(self): 
        print("Method __init__ telah dipanggil\n") 
        print("Instansiasi pertama:") 
    
instance1 = SingletonClass() 
print("Instansiasi kedua:") 
instance2 = SingletonClass() 
print(instance1 is instance2) 
print(instance1) 
print(instance2)