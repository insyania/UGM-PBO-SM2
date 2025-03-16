class Indonesia: 
    def pemimpin(self): 
        print("Presiden") 
    
    def bentuk_negara(self): 
        print("Republik") 
        
class Saudi: 
    def pemimpin(self): 
        print("Raja") 
        
    def bentuk_negara(self): 
        print("Kerajaan") 
        
indo = Indonesia() 
arab = Saudi() 
# iterate objects of same type 
for negara in (indo, arab): 
    # call methods without checking class of object 
    negara.pemimpin() 
    negara.bentuk_negara()