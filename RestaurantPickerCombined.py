def restriction():
        yes=["McDonald’s", "Jack Astor", "Trump", "America Restaurant", "Thai Kitchen", "Ki Restaurant", "Banjara", "259 Host", "Crepes Club", "Europe Bar"]
        no=["McDonald’s","Tim Hortons", "Jack Astor", "Trump", "America Restaurant", "Milestone", "Dailo", "Thai Kitchen", "Ki Restaurant", "Little India", "Banjara", "259 Host", "Amber", "Crepes Club", "Europe Bar"]
        print("Do you have any dietary restriction? (type Yes or No)")
        restriction = input()
        if restriction == "Yes":
                print (*yes)
        else:
                print (*no)

def type():
        fastfood=["McDonald’s", "Tim Hortons"]
        american=["Jack Astor", "Trump", "America Restaurant", "Milestone"]
        asian=["Dailo", "Thai Kitchen", "Ki Restaurant"]
        indian=["Little India", "Banjara", "259 Host"]
        european=["Amber", "Crepes Club", "Europe Bar"]
        print("Type (Please enter fastfood, American, Asian, Indian, or European):")
        type = input()
        if type == "fastfood":
                print (*fastfood)
        elif type == "American":
                print (*american)
        elif type == "Asian":
                print (*asian)
        elif type == "Indian":
                print (*indian)
        else:
                print (*european)

def price():
        price4=["McDonald’s","Tim Hortons", "Jack Astor", "Trump", "America Restaurant", "Milestone", "Dailo", "Thai Kitchen", "Ki Restaurant", "Little India", "Banjara", "259 Host", "Amber", "Crepes Club", "Europe Bar"]
        price3=["McDonald’s","Tim Hortons", "Jack Astor", "America Restaurant", "Milestone", "Dailo", "Thai Kitchen", "Little India", "Banjara", "259 Host", "Amber", "Crepes Club"]
        price2=["McDonald’s","Tim Hortons", "Jack Astor", "Milestone", "Dailo", "Little India", "259 Host", "Crepes Club"]
        price1=["McDonald’s","Tim Hortons", "Dailo", "259 Host"]
        print ("Price (Please enter 1-4):")
        price = eval(input())
        if price == 4: 
                print (*price4)
        elif price == 3:
                print (*price3)
        elif price == 2:
                print (*price2)
        else:
                print (*price1)

def demographic():
        downtown=["Trump", "Little India", "Crepes Club"]
        westToronto=["Tim Hortons", "Milestone", "Ki Restaurant", "259 Host"]
        eastToronto=["Jack Astor", "Dailo", "Banjara", "Europe Bar"]
        northToronto=["McDonald’s","America Restaurant", "Thai Kitchen", "Amber"]
        print ("Demographic (Please enter downtown, east Toronto, west Toronto, or north Toronto):")
        demographic = input()
        if demographic == "downtown":
                print (*downtown)
        elif demographic == "west Toronto":
                print (*westToronto)
        elif demographic == "east Toronto":
                print (*eastToronto)
        else:
                print (*northToronto)

def pickChoice():
    print("please select an option")
    print("1. Find restaurant by common taste")
    print("2. Rate restaurants")
    print("3. Tell us what you like")
    print("4. Find restaurant by category")
    choice = 0
    while (1 <= choice <= 4) == False:
        choice = eval(input("Please select a number between 1 and 4\n"))
    return choice


def find(ratings, people):
    connectedPeople = []
    for person in list(people.keys()):
        for restaurant in list(ratings.keys()):
            if restaurant in people[person] and people[person][restaurant] > 3:
                connectedPeople += [person]
    [[x,connectedPeople.count(x)] for x in set(connectedPeople)] #counts each persons occurence
    connectedPeople = list(set(connectedPeople)) #removes duplicates
    suggestedRestaurants=[]
    for person in connectedPeople:
        for suggestedRestaurant in list(people[person].keys()):
            if people[person][suggestedRestaurant] > 3:
                suggestedRestaurants += [suggestedRestaurant]
    restaurantRating = [[x,suggestedRestaurants.count(x)] for x in set(suggestedRestaurants)] #counts each persons occurence
    restaurantRating = sorted(restaurantRating, key = lambda x: int(x[1]))
    suggestions=[]
    print("Your suggested restaurants are: \n")
    for i in range(len(restaurantRating)):
              print(restaurantRating[len(restaurantRating)-i-1][0])
    
        

def rate(ratings):
    restaurant = input("Which restaurant would you like to rate?\n")
    rate = 0
    while (1 <= rate <= 5) == False:
        rate = eval(input("What would you like to rate it?\n"))
    ratings[restaurant]  = rate
    return ratings

def survey():
    pass

    
def category():
	print ("1. Find by price range")
	print ("2. Find by demographic")
	print ("3. Find by food type")
	print ("4. Find by dietary restriction")
	print ("Please enter 1, 2, 3, or 4.")
	find = eval(input())
	if find == 1:
		price()

	elif find == 2:
            
		demographic()
	
	elif find ==3:
		type()
	
	else:
		restriction()
def logIn():
    print("Welcome to Restaurant Reccomender")
    print("Please enter your login information")
    username = "tract9"
    password = "coffee"
    inputtedUsername = "blank"
    inputtedPassword = "blank"
    while username != inputtedUsername or password != inputtedPassword:
        inputtedUsername = input("Please enter username: ")
        inputtedPassword = input("please enter password: ")
        if username != inputtedUsername or password != inputtedPassword:
            print("Login failed. Please try again.\n")
    print("Login Successful!\n")



def main():
    logIn()
    cont = True
    ratings = {"Tim Hortons":5, "Jack Astor":3}
    people = {"Tom":{"Thai Kitchen":5, "Ki Restaurant":3, "Lemon land":5}, "Julia":{"Tim Hortons":5, "Wendy's":5, "Lemon land":5}, "Joe":{"Tim Hortons":5, "Lemon land":5}, "Sarah":{"Tim Hortons":5, "Monkey":5, "Lemon land":5}, "Mark":{"Tim Hortons":5, "Wendy's":3}, "Lydia":{"Tim Hortons":5, "Jack Astor":3, "Lemon land":5}, "Christa":{"Tim Hortons":5, "Monkey":5, "Lemon land":5}, "Dilbert":{"Tim Hortons":5, "Monkey":5}, "Lizzy":{"Tim Hortons":5, "Jack Astor":3, "Lemon land":5,"Wendy's":5}} 

    while cont == True:
        choice = pickChoice()
        if choice == 1:
            find(ratings, people)
        elif choice == 2:
            ratings = rate(ratings)
        elif choice ==3:
            survey()
        elif choice ==4:
        	category()
        print("\n")
        print("Would you like another action?")
        repeat = input("y for yes, n for no\n")
        if repeat == "n":
            cont = False
    
        
main()
   
