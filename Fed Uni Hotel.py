def Menu():
    print("Welcome to FedUni Hotel")
    print()
    print("1. Add Guest")
    print("2. Add Room")
    print("3. Add Booking")
    print("4. View Bookings")
    print("5. Quit")
    choice_number = int(input())
    if choice_number == 1:
        guestAdd()
    elif choice_number == 2:
        roomAdd()
    elif choice_number == 3:
        bookingAdd()
    elif choice_number == 4:
        bookingView()
    elif choice_number == 5:
        quit()
    else:
        print("Invalid Input")
        Menu()



guests = []
names = []
rooms = []
bookings = []




def guestAdd():
    print("Please Enter Guest Name: ")
    guestName = input()
    if (len(guests) == 0):
        guestId = 1
    else:
        guestId = len(guests) + 1;
    guests.append(guestId)
    names.append({
        'guestId': guestId,
        'guestName': guestName
    })
    print("Guest " + str(guestName) + " has been created with Guest ID: " + str(guestId))
    print("Would you like to [A]dd a new guest or [R]eturn to the previous menu?");

    answer = input()
    while(True):
        if answer == 'a' or answer== 'A':
            guestAdd()
            break
        elif answer == 'r' or answer=='R':
            Menu()
            break
        else:
            print("Invalid input")
            print("Would you like to [A]dd a new guest or [R]eturn to the previous menu?");
            answer = input()



def roomAdd():
    print("Please enter room number: ")
    roomNumber = int(input())
    if roomNumber in rooms:
        print("Room already exists")
        roomAdd()

    print("Please enter room capacity")
    rooms.append(roomNumber)
    capacity = int(input())
    bookings.append({
        'roomNumber': roomNumber,
        'capacity' : capacity,
        'guestId': 0,
        'noOfGuests': 0,
        'startday': 0,
        'endday': 0,
        'checkinMonth': 0,
        'checkinDay': 0,
        'checkoutMonth': 0,
        'checkoutDay': 0
    })

    print("Would you like to [A]dd a new room or [R]eturn to the previous menu?")
    answer = input()
    while (True):
        if answer == 'a' or answer == 'A':
            roomAdd()
            break
        elif answer == 'r' or answer == 'R':
            Menu()
            break
        else:
            print("Invalid input")
            print("Would you like to [A]dd a new guest or [R]eturn to the previous menu?");
            answer = input()





def bookingAdd():
    print("Please enter Guest ID: ")
    guestId = int(input())
    if guestId not in guests:
        print("Guest ID does not exists")
        bookingAdd()

    print("Please enter room number")
    roomNumber = int(input())
    while(True):
        if roomNumber not in rooms:
            print("Room does not exists")
            print("Please enter room number")
            roomNumber = int(input())
        else:
            break

    print("Please enter number of guests")
    noOfGuests = int(input())
    for room in rooms:

        if room == roomNumber:
            if (noOfGuests > getCapacity(roomNumber)):
                print("Guest count exceeds room capacity of: " + str(getCapacity(roomNumber)))
                bookingAdd()

    print("Please enter check-in month:")
    checkinMonth = int(input())
    while(True):
        if checkinMonth > 12:
            print("Invalid month. Please enter check-in month")
            checkinMonth = int(input())
        else:
            break

    print("Please enter check-in day")
    checkinDay = int(input())
    while(True):
        if checkinDay > getDayofMonth(checkinMonth):
            print("Invalid Day. Please enter check-in day")
            checkinDay = int(input())
        else:
            break

    print("Please enter check-out month")
    chekoutMonth = int(input())
    print("Please enter check-out day")
    chekoutDay = int(input())
    startday = dayToDayNumber(checkinMonth, checkinDay)
    endday = dayToDayNumber(chekoutMonth, chekoutDay)
    for booking in bookings:
        if booking['roomNumber'] == roomNumber:
            if (booking['endday'] < startday or booking['startday'] > endday):
                print("Booking successful")

                booking.update(roomNumber=roomNumber, capacity=getCapacity(roomNumber),guestId=guestId, noOfGuests=noOfGuests,
                               startday=startday, endday=endday, checkinMonth=checkinMonth
                               , checkinDay=checkinDay, checkoutMonth=chekoutMonth, checkoutDay=chekoutDay)

                print("Would you like to [A]dd a new booking or [R]eturn to the previous menu?")
                answer = input()
                while (True):
                    if answer == 'a' or answer == 'A':
                        bookingAdd()
                        break
                    elif answer == 'r' or answer == 'R':
                        Menu()
                        break
                    else:
                        print("Invalid input")
                        print("Would you like to [A]dd a new guest or [R]eturn to the previous menu?");
                        answer = input()

            else:
                print("Room is not available for that period")
                bookingAdd()


def bookingView():
    print("Would you like to view [G]uest bookings, [R]oom booking, or e[X]it?")
    answer = input().lower()
    if (answer == 'g'):
        bookingofguests()
    elif answer == 'r':
        bookingofrooms()
    elif answer == 'x':
        Menu()
    else:
        print("Invalid Input")
        bookingView()



def bookingofguests():
    print("Please enter guest Id")
    guestId = int(input())
    if guestId not in guests:
        print("Guest does not exists")
        bookingofguests()

    guestName = ""
    for guest in names:
        if guest['guestId'] == guestId:
            guestName = guestName + guest['guestName']

    for booking in bookings:
        if booking['guestId'] == guestId:
            print("Guest " + str(guestId) + " : " + guestName)
            print("Booking : " + "Room " + str(booking['roomNumber']) + " ," + str(booking['noOfGuests']) +
                  " guest[s] from " + str(booking['checkinMonth']) + "/" + str(booking['checkinDay']) + " to "
                  + str(booking['checkoutMonth']) + "/" + str(booking['checkoutDay']))
            bookingView()



def bookingofrooms():
    print("Please enter Room number")
    roomNumber = int(input())
    if roomNumber not in rooms:
        print("Room does not exists")
        bookingofrooms()


    print("Room " + str(roomNumber) + " Bookings :")
    guestId= ""

    guestName = ""

    for booking in bookings:
        if booking['roomNumber'] == roomNumber:
            guestId = guestId + str(booking['guestId'])

    for guest in names:
        if guest['guestId'] == int(guestId):
            guestName = guestName + guest['guestName']

    for booking in bookings:
        if booking['roomNumber'] == roomNumber:
            print("Guest  " + str(guestId) + " : " + str(guestName) + ", " + str(booking['noOfGuests']) +

                  " guest[s] from " + str(booking['checkinMonth']) + "/" + str(booking['checkinDay']) + " to "
                  + str(booking['checkoutMonth']) + "/" + str(booking['checkoutDay']))
            bookingView()




def quit():
    print("Thanks for using FedUni Bookings")


def dayToDayNumber(mon,day):
    if (mon < 1 or mon > 12 or day < 1 or day > 31) :
        return 0


    if (mon == 1):
        return day

    if(mon==2):
        return 31 + day

    if (mon == 3) :
        return 59 + day


    if (mon == 4):
        return 90 + day;



    if (mon == 5) :
        return 120 + day

    if (mon == 6):
        return 151 + day

    if (mon == 7):
        return 181 + day

    if (mon == 8) :
        return 212 + day

    if (mon == 9) :
        return 243 + day;

    if (mon == 10) :
        return 273 + day

    if (mon == 11):
        return 304 + day

    return 334 + day


def getCapacity(roomNumber):
    for booking in bookings:
        if booking['roomNumber'] == roomNumber:
            return booking['capacity']


def getDayofMonth(month):
    if(month == 1 or month == 3 or month==5 or month==7 or month==8 or month==10 or month==12):
        return 31
    elif(month==2):
        return 28
    else:
        return 30


Menu()