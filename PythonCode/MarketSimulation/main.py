from random import randint, randrange, choice, shuffle
import time

#======CONSTANTS======#

WHOLESALE_PRICE = 70    #Price corps pay for replenishing their product inventory
MAX_INVSPACE = 50            #Max inventory storage a corp has
MARKET_FEE = 50         #Daily cost corps need to pay to say in the market

#=====================#

class Market():
    def __init__(self, consumers = [], corps = [], vacantConsumerIDs = [], vacantCorpIDs = []):
        self.consumers = consumers;
        self.corps = corps;
        self.vacantConsumerIDs = vacantConsumerIDs; #When a consumer exits the market, its ID gets stored here for a new consumer to come and take
        self.vacantCorpIDs = vacantCorpIDs;         #Same as above but for corps
    
    def populate(self):
        #Populate consumers
        for i in range(1, 1001):
            self.consumers.append(Consumer(ID = str(i)))
        #Populate corps
        for i in range(1, 101):
            self.corps.append(Corp(ID = 'Cx' + str(i)))

    def repopulate(self):
        #Try to repopulate consumers (60% chance of replenishing per vacant)
        for i in self.vacantConsumerIDs:
            if randint(1, 100) <= 60: self.consumers.append(Consumer(ID = i))
        #Try to repopulate corps (30% chance of replenishing per vacant)
        for i in self.vacantCorpsIDs:
            if randint(1, 100) <= 30: self.corps.append(Corp(ID = i))

    def update(self):
        #Remove leaving consumers from the market and store their IDs for future costumers
        for consumer in self.consumers: 
            consumer.update();
            if not consumer.inMarket: 
                self.vacantConsumerIDs.append(consumer.ID);
                self.consumers.remove(consumer); 
        #Remove broke corps from the market and store their IDs for future corps
        for corp in self.corps:
            corp.update();
            if not corp.inBusiness: 
                self.vacantCorpIDs.append(corp.ID);
                self.corps.remove(corp);

    def newDay(self):
        #The new day's parameters get set

        self.corps.shuffle()        #Shuffle the corps list for changing access order each day
        self.consumers.shuffle()    #Same as above but for consumers
        #Today's simulation begins
        for consumer in self.consumers:
            for corp in self.corps:
                consumer.searchProduct(corp.price, corp.inventory) #[consumer] searches for a product in [corp]
                if consumer.hasBought:
                    corp.inventory -= 1;    #Consumer has bought, the product gets removed from [corp]'s inventory
                    break;  #Consumer ends the day
        self.update()


class Consumer():
    def __init__(self, money = randint(5000, 10000), ID = 0, hasBought = False, inMarket = True):
        self.ID = ID;               #Consumer's IDs are numeric
        #self.money = money;        #Deprecated mechanic, in sim. consumers have infinite money
        self.buyingPrice = money;   #Maximum price the consumer will pay for a product
        self.hasBought = hasBought; #Bool, indicates if the consumer was able to buy something
        self.inMarket = inMarket;   #Bool, flag var for deleting consumers when they leave the market
    
    def searchProduct(self, price, products):
        if products > 0 and price <= buyingPrice:
            self.hasBought = True;
            self.buyingPrice = price;
        else: self.hasBought = False;

    def update(self):   #When a consumer can't find a product he leaves the market
        if not self.hasBought: self.inMarket = False;


class Corp():
    def __init__(self, money = randint(100000, 200000), ID = 'Cx', price = randint(190, 210), inventory = MAX_INVSPACE, inBusiness = True):
        self.ID = ID;               #Corp's IDs are in the form of Cx plus numeric id
        self.money = money;
        self.price = price;           #Initial price always between (190, 210)
        self.inventory = inventory;   #Products in the corp's storage waiting to be sold (MAX len == 50)
        self.willInvest = willInvest; #Random var that decides if the corp replenishes inv each day
        self.inBusiness = inBusiness; #Bool, indicates if the corp is alive marketwise 

    def replenishInv(self):
        if len(self.inventory) <= 5 or self.willInvest:
            self.willInvest = False;
            while self.inventory <= MAX_INVSPACE and self.money >= WHOLESALE_PRICE:
                inventory += 1;
                self.money -= WHOLESALE_PRICE;
                
    def setInvestment(self): 
        if randint(1, 100) <= 25: self.willInvest = True;
    
    def update(self):
        self.money -= MARKET_FEE;                 #Corp pays the daily market fee
        if money < 0: self.inBusiness = False;    #Checks if corp went bankrupt 

#Simulation main process
market = Market();
market.populate();
isRunning = True;
while isRunning:
    #check escape input
    market.newDay();
    time.sleep(3)       #Wait 3 seconds between simulated days for reviewing and debugging purpose
    

#To-Do
#Algorythm for corp price adjustment in response to products sold More products == Higher prices and vicev.