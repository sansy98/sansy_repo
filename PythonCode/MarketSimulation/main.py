from random import randint, randrange, choice, shuffle, uniform
import time
import keyboard
import numpy as np

#======CONSTANTS======#

WHOLESALE_PRICE = 70    #Price corps pay for replenishing their product inventory
MAX_INVSPACE = 50       #Max inventory storage a corp has
MARKET_FEE = 50         #Daily cost corps need to pay to say in the market

#=====================#

class Market():
    def __init__(self, consumers = [], corps = [], vacantConsumerIDs = [], vacantCorpIDs = []):
        self.consumers = consumers;
        self.corps = corps;
        self.vacantConsumerIDs = vacantConsumerIDs; #When a consumer exits the market, its ID gets stored here for a new consumer to come and take
        self.vacantCorpIDs = vacantCorpIDs;         #Same as above but for corps
    

    #Populates the market at the begining of the simulation
    def populate(self):
        #Populate consumers
        for i in range(1, 1001):
            self.consumers.append(Consumer(ID = str(i)))

        #Populate corps
        for i in range(1, 101):
            self.corps.append(Corp(ID = 'Cx' + str(i), price = randint(190, 210)))


    #Repopulates the market
    def repopulate(self):
        #Try to repopulate consumers (60% chance of replenishing per vacant)
        for i in self.vacantConsumerIDs:
            if randint(1, 100) <= 60: self.consumers.append(Consumer(ID = i))

        #Try to repopulate corps (30% chance of replenishing per vacant)
        for i in self.vacantCorpsIDs:
            if randint(1, 100) <= 30: self.corps.append(Corp(ID = i))


    #Checks for broke corps and unsatisfied consumers. Called in self.newDay()
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


    #Simulates a full day in the market
    def newDay(self):
        #The new day's parameters get set
        shuffle(self.consumers);    #Shuffle the customer list for changing buying order each day

        #Today's simulation begins
        for consumer in self.consumers:
            shuffle(self.corps);            #Shuffle the corps list for changing access for each customer
            for corp in self.corps:
                consumer.searchProduct(corp.price, corp.inventory, corp.ID) #[consumer] searches for a product in [corp]
                if consumer.hasBought:
                    corp.inventory -= 1;    #Consumer has bought, the product gets removed from [corp]'s inventory
                    corp.demand += 1;
                    corp.money += corp.price;
                    break;                  #Consumer ends the day
        self.update()


class Consumer():
    def __init__(self, lastBoughtID = None, ID = 0, hasBought = False, inMarket = True):
        self.ID = ID;                              #Consumer's IDs are numeric
        self.lastBoughtID = lastBoughtID;          #Saves the last corp's ID from which the customer has bought
        self.buyingPrice = randint(5000, 10000);   #Maximum price the consumer will pay for a product
        self.hasBought = hasBought;                #Bool, indicates if the consumer was able to buy something
        self.inMarket = inMarket;                  #Bool, flag var for deleting consumers when they leave the market
    

    #Iterates through corps in the market searching for a product to buy with a valid price
    def searchProduct(self, price, products, cID):
        if products > 0 and price <= self.buyingPrice:
            self.hasBought = True;
            self.buyingPrice = price;
            self.lastBoughtID = cID;
        else: self.hasBought = False;


    #Checks if consumer has bought, if he hasnt it sets inMarket bool to False for him to exit
    def update(self):   
        if not self.hasBought: self.inMarket = False;


class Corp():
    def __init__(self, demand = 0, willInvest = False, money = randint(100000, 200000), ID = 'Cx', price = 0, inventory = MAX_INVSPACE, inBusiness = True, history = []):
        self.ID = ID;               #Corp's IDs are in the form of Cx plus numeric id
        self.money = money;
        self.demand = demand;               #Daily sold products
        self.price = price;                 #Initial price always between (190, 210)
        self.inventory = inventory;         #Products in the corp's storage waiting to be sold (MAX len == 50)
        self.willInvest = willInvest;       #Random var that decides if the corp replenishes inv each day
        self.inBusiness = inBusiness;       #Bool, indicates if the corp is alive marketwise
        self.history = [str(hex(id(self)))] #List with (price, demand) historic pairs, [0] = object hex mem adress, this is to avoid all Corp.history arrays to have the same mem adress


    #Replenishes corp's inventory with new products
    def replenishInv(self):
        if len(self.inventory) <= 5 or self.willInvest:
            self.willInvest = False;
            while self.inventory <= MAX_INVSPACE and self.money >= WHOLESALE_PRICE:
                inventory += 1;
                self.money -= WHOLESALE_PRICE;


    #Sets the random bool that determines random inventory replenishing     
    def setInvestment(self): 
        if randint(1, 100) <= 25: self.willInvest = True;


    #Algorythm for price adjustment simulation, only called if we have 2 data tuples to start working with
    def setPrice(self):
        '''
        try:
            #1st: Find q(p) by solving a system of linear equations, this is done by understanding q(p) function as matrixes in the form of AX=B
            A = np.array([[1, self.history[-2][0]], [1, self.history[-1][0]]]);
            B = np.array([self.history[-2][1], self.history[-1][1]]);
            X = np.linalg.solve(A, B);                   #RETURNS -> (n, m) of q(p) = m*p + n so: q(p) = X[1]*p + X[0]
        
            #2nd: Calculate price flexibility epsilon (e)
            try:
                q = int(X[1])*self.history[-1][0]+int(X[0])
                q_prime = int(X[1])
                e = (self.history[-1][0]/q)*q_prime
            except ZeroDivisionError:
                print(f"ID: {self.ID}")
                print(f"Last 2 historic pairs: {self.history[-1]}{self.history[-2]}")
                e = uniform(0.5, 1.5);

        except np.linalg.LinAlgError:   e = uniform(0.5, 1.5);

        #3rd: Compare abs(e) with one to determine what to do with the price
        if abs(e) < 1:      self.price += int(20 * (1-e))
        elif abs(e) > 1:    self.price -= int(20 * (e-1))
        else:               pass    
        '''

    #Pays market fee, checks if corp has gone bankrupt and records day's (pi, qi) pairs
    #Called in Market.update()
    def update(self):
        #print(f"BONKED corp.update(), history memdir = {hex(id(self.history))} !!!: ID: {self.ID}")
        if type(self.history[0]) is str: self.history.pop(0);  #Delete mem.access hex
        if len(self.history) >= 2: self.setPrice();            #Adjust price when enough historic data is available
        self.history.append((self.price, self.demand))
        self.money -= MARKET_FEE;                              #Corp pays the daily market fee
        if self.money < 0: self.inBusiness = False;            #Checks if corp went bankrupt, if so its kicked out



#===============SIMULATION {MAIN} CONTROL PROCESS================#

market = Market();
market.populate();
isRunning = True;
day = 0

debugTags =['Cx1', 'Cx2', 'Cx3', '1', '2', '3']

while isRunning:
    #check escape input
    try:
        pass;
        #if keyboard.is_pressed("q"): isRunning = False;
    except: pass;
    #Simulate new day is called
    market.newDay();
    day += 1
    #newDay not simulated until space is pressed for debbuging purposes
    print(f"=========DAY {day}=========")
    print("")
    print("CORPS (only 3 first by id): ")
    print("")
    for i in range(0, len(market.corps)):
        if market.corps[i].ID in debugTags:
            print(f"ID: {market.corps[i].ID}")
            print(f"Money: {market.corps[i].money}")
            print(f"Price: {market.corps[i].price}")
            print(f"Demand: {market.corps[i].demand}")
            print(f"Stock: {market.corps[i].inventory}/{MAX_INVSPACE}")
            print(f"Historic price/demand: {market.corps[i].history}")
            print(f"Number of corps: {len(market.corps)}")
            print("")
    
    print("CONSUMERS (only 3 first by id): ")
    print("")
    for i in range(0, len(market.consumers)):
        if market.consumers[i].ID in debugTags:
            print(f"ID: {market.consumers[i].ID}")
            print(f"MaxPrice: {market.consumers[i].buyingPrice}")
            print(f"HasBought?: {market.consumers[i].hasBought}")
            print(f"LastBoughtAt: Corp {market.consumers[i].lastBoughtID}")
            print(f"TotConsumers: {len(market.consumers)}")
            print("")
    while True:
        debugFlag = input("Input any key to continue: ");
        if debugFlag == 'q': raise ValueError("Ending simulation...");
        if debugFlag or not debugFlag: break;
    #time.sleep(3)       #Wait 3 seconds between simulated days for reviewing and debugging purpose



#================TO - DO================#

#Algorythm for corp price adjustment in response to products sold More products == Higher prices and vicev.
#ALGORYHM FORMULA: R(p) = p * q(p)   ||| p = price | q(p) = demand function | R(p) = Revenue |||[Maximize R]
#d(p) estimated from historical sales data composed by pairs of the type (pi, qi) 
#   ||| pi = i(th) day's price | qi = i(th) day's demand|||
#WE NEED AT LEAST 2 PAIRS (pi, qi) FOR THE ALGORYTHM TO WORK WITH
#
#Determine the price profitability with PRICE ELASTICITY OF DEMAND: e = (p/q)*(dq/dp) || e = p/q(p) * q'(p) 
#|e| > 1, the price is ELASTIC      (%∆Q > %∆P)     => DECREASE PRICE
#|e| < 1, the price is INELASTIC    (%∆Q < %∆P)     => INCREASE PRICE
#|e| = 1, the price is UNIT ELASTIC (%∆Q = %∆P)     => MANTAIN PRICE  (price is optimal)

#

#LINKS:
#
#https://math.ucr.edu/~joselg/teachingS13/elasticity.pdf
#https://stackabuse.com/solving-systems-of-linear-equations-with-pythons-numpy/
#https://www.geeksforgeeks.org/scipy-curve-fitting/ !!! -> IMPORTANT, q(p) IS NOT A LINE, ITS A CURVE, OBTAIN IT WITH THIS AND USING ALL HISTORIC PAIR DATA AVAILABLE