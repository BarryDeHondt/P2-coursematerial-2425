class Ticket:
    def __init__(self, ticket_id, ticket_type, price):
        self.ticket_id = ticket_id
        self.ticket_type = ticket_type
        self.price = price
        
    @property
    def ticket_id(self):
        return self.__ticket_id
    
    @ticket_id.setter
    def ticket_id(self, ticket_id):
        if not Ticket.validate_ticket_id(ticket_id):
            raise ValueError("Invalid ticket ID")
        else:
            self.__ticket_id = ticket_id
    #Statische methode puur om het programma te strucutureren        
    @staticmethod
    def validate_ticket_id(ticket_id):
        if len(ticket_id) != 8:
            return False
    
        if not ticket_id[:3].isalpha() or not ticket_id[:3].isupper():
            return False
    
        if not ticket_id[3:].isdigit():
            return False
        return True
    
            
    def __str__(self):
        return f"This a ticket with type {self.ticket_type}, the price is {self.price} and the ID is {self.ticket_id}"


from abc import ABC, abstractmethod

class Event(ABC):
    def __init__(self, name, capacity):
        self.name = name 
        self.capacity = capacity
        self.__tickets = {}
        
    
    def add_ticket(self,ticket):
            if self.total_tickets >= self.max_capacity:
                raise ValueError("Max capacity reached!")
            self.__tickets[ticket.ticket_id] = ticket   
            
    def remove_ticket(self, ticket_id):
        if ticket_id not in self.__tickets:
            raise ValueError("Ticket not found!")
        del self.__tickets[ticket_id]
        
    @property
    def total_tickets(self):
        return len(self.__tickets)
    
    @abstractmethod
    def generate_event_summary(self):
        pass

    
class Concert(Event):
    def __init__(self,name, capacity, artists, tickets):
        super().__init__(name, capacity, tickets)  
        self.artists = artists
        
        
        
    def generate_event_summary(self):
        summary = f"Name: {self.name}\nTotal tickets: {self.total_tickets}\nArtists:"
        for artist in self.artists:
            summary += f"\n - {artist}" 
        return summary
    
    
class PrivateEvent(Event):
    def __init__(self, name, artist):
        super().__init__(name, 50)  
        self.artists = artist
        
    def generate_event_summary(self):
        summary = f"Name: {self.name}\nTotal tickets: {self.total_tickets}\nArtists: {self.artist}"
        return summary   
    
# Maak een concert aan
festival = Concert("Festival", 5000, ["Joost", "Terno", "DJ X"], 3)

# Maak tickets aan
ticket1 = Ticket("VIP12345", "VIP", 399)
ticket2 = Ticket("REG67890", "Regular", 99)

# Voeg tickets toe aan het concert
festival.tickets[ticket1.ticket_id] = ticket1
festival.tickets[ticket2.ticket_id] = ticket2

# Print tickets
print("\nTickets:")
for ticket in festival.tickets.values():
    print(ticket)

# Print concert details
print("\nConcert details:")
print(festival.generate_event_summary())

# Maak een privé-evenement aan
jazz_night = PrivateEvent("Exclusive Jazz Night", "Shakira")

# Maak tickets aan
ticket1 = Ticket("JAZ12345", "VIP", 250)
ticket2 = Ticket("JAZ67890", "Regular", 100)

# Voeg tickets toe aan het private event
jazz_night.tickets[ticket1.ticket_id] = ticket1
jazz_night.tickets[ticket2.ticket_id] = ticket2

# Print tickets
print("\nTickets for Private Event:")
for ticket in jazz_night.tickets.values():
    print(ticket)

# Print PrivateEvent details
print("\nPrivate Event details:")
print(jazz_night.generate_event_summary())
    

                
        
    
    
    
        
        
             