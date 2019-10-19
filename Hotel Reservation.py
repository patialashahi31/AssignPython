def menuOfHotel():
    print("Welcome to the Hotel")
    print()
    print()
    print("1. Add Guest")
    print("2. Add Room")
    print("3. Add Booking")
    print("4. View Booking")
    print("5. Quit")
    option = int(input())
    if option == 1:
        Guest()
    elif option == 2:
        Room()
    elif option == 3:
        addReservation()
    elif option == 4:
        viewReservation()
    elif option == 5:
        Quit()
    else:
        print("Invalid Input")
        menuOfHotel()



def Quit():
    print("Thanks for using hotel booking service")


guestinfo = []
roominfo = []
bookinginfo = []

def Guest():
    print("Please Enter Guest Name: ")
    name = input()
    if (len(guestinfo) == 0):
        id = 1
    else:
        id = len(guestinfo) + 1;


    guestinfo.append({
        'id': id,
        'name': name
    })
    print("Guest " + str(name) + " has been created with Guest ID: " + str(id))
    print("Would you like to [A]dd a new guest or [R]eturn to the previous menu?");
    option = input().lower()
    while (True):
        if (option == 'a'):
            Guest()
        elif option == 'r':
            menuOfHotel()
        else:
            print("Invalid input")
            print("Would you like to [A]dd a new guest or [R]eturn to the previous menu?");
            option = input().lower()

def Room():
    print("Please enter room number: ")
    number = int(input())
    for room in roominfo:
        if room['number'] == number:
            print("Room already exists")
            Room()

    print("Please enter room capacity")
    capacity = int(input())

    bookinginfo.append({
        'number': number,
        'id': 0,
        'numberOfGuests': 0,
        'starting': 0,
        'ending': 0,
        'checkin_Mon': 0,
        'checkin_Day': 0,
        'checkout_Mon': 0,
        'checkout_Day': 0
    })
    roominfo.append({
        'number' : number,
        'capacity' : capacity
    })
    print("Would you like to [A]dd a new room or [R]eturn to the previous menu?")
    option = input().lower()
    while (True):
        if option == 'a':
            Room()
        elif option == 'r':
            menuOfHotel()
        else:
            print("Invalid input")
            print("Would you like to [A]dd a new guest or [R]eturn to the previous menu?");
            option = input().lower()



def dayToDayNumber(month,day):
    if (month < 1 or month > 12 or day < 1 or day > 31) :
        return 0


    if (month == 1):
        return day

    if(month==2):
        return 31 + day

    if (month == 3) :
        return 59 + day


    if (month == 4):
        return 90 + day;



    if (month == 5) :
        return 120 + day

    if (month == 6):
        return 151 + day

    if (month == 7):
        return 181 + day

    if (month == 8) :
        return 212 + day

    if (month == 9) :
        return 243 + day;

    if (month == 10) :
        return 273 + day

    if (month == 11):
        return 304 + day

    return 334 + day





def addReservation():
    print("Please enter Guest ID: ")
    id = int(input())
    flag=0
    for guest in guestinfo:
        if guest['id'] == id:
            flag = 1

    if flag==0:
        print("Invalid Guest ID")
        addReservation()

    print("Please enter room number")
    number = int(input())
    flag1=0
    flag2=0
    while (True):
        for room in roominfo:
            if room['number'] == number:
                flag1 = 1
                break

        if flag1 == 0:
            print("Room does not exists")
            print("Please enter room number")
            flag2=1
            number = int(input())
        else:
            print("Please enter number of guests: ")
            numberOfGuests = int(input())
            for room in roominfo:

                if room['number'] == number:
                    if (numberOfGuests > room['capacity']):
                        print("Guest count exceeds room capacity of: " + str(room['capacity']))
                        print("Please enter room number")
                        flag2=1
                        number = int(input())
                    else:
                        flag2=0
                        break
        if flag2==0:
            break



    print("Please enter check-in month:")
    checkin_Mon = int(input())
    while (True):
        if checkin_Mon > 12:
            print("Invalid month. Please enter check-in month")
            checkin_Mon = int(input())
        else:
            break

    print("Please enter check-in day")
    checkin_Day = int(input())
    while (True):
        if checkin_Day > numberofDays(checkin_Mon):
            print("Invalid Day. Please enter check-in day")
            checkin_Day = int(input())
        else:
            break

    print("Please enter check-out month")
    chekout_Mon = int(input())
    print("Please enter check-out day")
    chekout_Day = int(input())
    starting = dayToDayNumber(checkin_Mon, checkin_Day)
    ending = dayToDayNumber(chekout_Mon, chekout_Day)
    for booking in bookinginfo:
        if booking['number'] == number:
            if (booking['ending'] < starting or booking['starting'] > ending):
                print("Booking successful")

                booking.update(number=number, id=id, numberOfGuests=numberOfGuests,
                               starting=starting, ending=ending, checkin_Mon=checkin_Mon
                               , checkin_Day=checkin_Day, checkout_Mon=chekout_Mon, checkout_Day=chekout_Day)

                print("Would you like to [A]dd a new booking or [R]eturn to the previous menu?")
                option = input().lower()
                while (True):
                    if (option == 'a'):
                        addReservation()
                    elif option == 'r':
                        menuOfHotel()
                    else:
                        print("Invalid input")
                        print("Would you like to [A]dd a new guest or [R]eturn to the previous menu?");
                        option = input().lower()
            else:
                print("Room is not available for that period")
                addReservation()



def viewReservation():
    print("Would you like to view [G]uest bookings, [R]oom booking, or e[X]it?")
    option = input().lower()
    if (option == 'g'):
        byGuest()
    elif option == 'r':
        byRoom()
    elif option=='x':
        menuOfHotel()
    else:
        print("Invalid Input")
        viewReservation()



def byGuest():
    print("Please enter guest Id")
    id = int(input())
    flag=0
    for guest in guestinfo:
        if guest['id'] == id:
            flag=1
            break

    if flag==0:
        print("Guest does not exists")
        byGuest()



    name = ""
    for guest in guestinfo:
        if guest['id'] == id:
            name = name + guest['name']

    for booking in bookinginfo:
        if booking['id'] == id:
            print("Guest " + str(id) + " : " + name)
            print("Booking : " + "Room " + str(booking['number']) + " ," + str(booking['numberOfGuests']) +
                  " guest[s] from " + str(booking['checkin_Mon']) + "/" + str(booking['checkin_Day']) + " to "
                  + str(booking['checkout_Mon']) + "/" + str(booking['checkout_Day']))
            viewReservation()


def byRoom():
    print("Please enter Room number")
    number = int(input())
    flag = 0
    for room in roominfo:
        if room['number'] == number:
            flag = 1
            break

    if flag == 0:
        print("Room number does not exists")
        byRoom()

    print("Room " + str(number) + " Bookings :")
    id = ""

    name = ""

    for booking in bookinginfo:
        if booking['number'] == number:
            id = "".join(str(booking['id']))

    for guest in guestinfo:
        if guest['id'] == int(id):
            name = "".join( guest['name'])

    for booking in bookinginfo:
        if booking['number'] == number:
            print("Guest  " + str(id) + " : " + str(name) + ", " + str(booking['numberOfGuests']) +

                  " guest[s] from " + str(booking['checkin_Mon']) + "/" + str(booking['checkin_Day']) + " to "
                  + str(booking['checkout_Mon']) + "/" + str(booking['checkout_Day']))
            viewReservation()






def numberofDays(month):
    if (month==2):
        return 28
    elif (month==4 or month==6 or month==9 or month==10):
        return 30
    else:
        return 31



menuOfHotel()