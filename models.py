
class Dog:
    def __init__(self, dog_id, name, age, breed, adopted=False): # Doble guion bajo
        self.id = dog_id
        self.name = name
        self.age = age
        self.breed = breed
        self.adopted = adopted

class Adopter:
    def __init__(self, adopter_id, name, lastName, address, id_card=None): # Doble guion bajo
        self.adopter_id = adopter_id 
        self.name = name
        self.lastName = lastName
        self.address = address
        self.id_card = id_card