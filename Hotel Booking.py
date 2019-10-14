guests = []
guestnames = []
bookings = []
rooms = []
justrooms = []


def mainMenu():
    print("Welcome to FedUni Hotel")
    print()
    print()
    print("1. Add Guest")
    print("2. Add Room")
    print("3. Add Booking")
    print("4. View Booking")
    print("5. Quit")
    choice = int(input())
    if choice == 1:
        addGuest()
    elif choice == 2:
        addRoom()
    elif choice == 3:
        addBooking()
    elif choice == 4:
        viewBooking()
    elif choice == 5:
        quit()
    else:
        print("Invalid Input")
        mainMenu()

def addGuest():
    print("Please Enter Guest Name: ")
    guest_name = input()
    if(len(guests)==0):
        guest_id = 1
    else:
        guest_id = len(guests) + 1;

    guests.append(guest_id)
    guestnames.append({
        'guest_id' : guest_id,
        'guest_name' : guest_name
    })
    print("Guest " + str(guest_name) + " has been created with Guest ID: " + str(guest_id))
    print("Would you like to [A]dd a new guest or [R]eturn to the previous menu?");
    choice = input().lower()
    while(True):
        if(choice=='a'):
            addGuest()
            break
        elif choice=='r':
            mainMenu()
            break
        else:
            print("Invalid input")
            print("Would you like to [A]dd a new guest or [R]eturn to the previous menu?");
            choice = input().lower()





def addRoom():
    print("Please enter room number: ")
    room_number = int(input())
    for i in rooms:
        if(i[0]==room_number):

            print("Room already exists")
            addRoom()



    print("Please enter room capacity")
    capacity = int(input())
    rooms.append((room_number,capacity))
    justrooms.append(room_number)
    bookings.append({
        'room_number' : room_number,
        'guest_id' : 0,
        'number_of_guests' : 0,
        'start' : 0,
        'end' : 0,
        'checkin_month':0,
        'checkin_day' :0,
        'checkout_month' :0,
        'checkout_day' :0
    })

    print("Would you like to [A]dd a new room or [R]eturn to the previous menu?")
    choice = input().lower()
    while (True):
        if (choice == 'a'):
            addRoom()
            break
        elif choice == 'r':
            mainMenu()
            break
        else:
            print("Invalid input")
            print("Would you like to [A]dd a new guest or [R]eturn to the previous menu?");
            choice = input().lower()


def addBooking():
    print("Please enter Guest ID: ")
    guest_id = int(input())
    if guest_id not  in guests:
        print("Guest ID does not exists")
        addBooking()

    print("Please enter room number")
    room_number = int(input())
    while(True):

        if room_number not in justrooms:

            print("Room does not exists")
            room_number = int(input())
        else:
            break

    print("Please enter number of guests: ")
    number_of_guests = int(input())
    for room in rooms:

            if room[0] == room_number:
                if(number_of_guests>room[1]):
                    print("Guest count exceeds room capacity of: " + str(room[1]))
                    addBooking()

    print("Please enter check-in month:")
    checkin_month = int(input())
    while(True):
        if checkin_month > 12:
            print("Invalid month. Please enter check-in month")
            checkin_month = int(input())
        else:
            break

    print("Please enter check-in day")
    checkin_day = int(input())
    while(True):
        if checkin_day>getDay(checkin_month):
            print("Invalid Day. Please enter check-in day")
            checkin_day = int(input())
        else:
            break

    print("Please enter check-out month")
    chekout_month = int(input())
    print("Please enter check-out day")
    chekout_day = int(input())
    start = dayToDayNumber(checkin_month,checkin_day)
    end = dayToDayNumber(chekout_month,chekout_day)
    for booking in bookings:
        if booking['room_number'] == room_number:
           if (booking['end'] < start or booking['start']>end):
               print("Booking successful")


               booking.update(room_number=room_number,guest_id = guest_id,number_of_guests=number_of_guests,start=start,end=end,checkin_month=checkin_month
                              ,checkin_day=checkin_day,checkout_month=chekout_month,checkout_day=chekout_day)

               print("Would you like to [A]dd a new booking or [R]eturn to the previous menu?")
               choice = input().lower()
               while (True):
                   if (choice == 'a'):
                       addBooking()
                       break
                   elif choice == 'r':
                       mainMenu()
                       break
                   else:
                       print("Invalid input")
                       print("Would you like to [A]dd a new guest or [R]eturn to the previous menu?");
                       choice = input().lower()
           else:
               print("Room is not available for that period")
               addBooking()


def showrooms(bookings):
    for room in bookings:
        print(room)


def guestBookings(bookings):
    print("Please enter guest Id")
    guest_id = int(input())
    if guest_id not in guests:
        print("Guest does not exists")
        guestBookings(bookings)


    guest_name = ""
    for guest in guestnames:
        if guest['guest_id'] == guest_id:
            guest_name  = guest_name + guest['guest_name']


    for booking in bookings:
        if booking['guest_id'] == guest_id:
            print("Guest " + str(guest_id) + " : " + guest_name)
            print("Booking : " + "Room " + str(booking['room_number']) + " ," + str(booking['number_of_guests']) +
                                  " guest[s] from " + str(booking['checkin_month']) + "/" + str(booking['checkin_day']) + " to "
                                  + str(booking['checkout_month']) + "/" + str(booking['checkout_day']))
            viewBooking()


def roomBookings(bookings):
    print("Please enter Room number")
    room_number = int(input())
    flag=0
    for room in rooms:
        if room[0] == room_number:
            flag=1
            break

    if flag==0:
        print("Room number does not exists")
        roomBookings(bookings)

    print("Room " + str(room_number) + " Bookings :")
    guest_id = ""

    guest_name = ""


    for booking in bookings:
        if booking['room_number'] == room_number:
            guest_id = guest_id  + str(booking['guest_id'])

    for guest in guestnames:
        if guest['guest_id'] == int(guest_id):
            guest_name = guest_name + guest['guest_name']


    for booking in bookings:
        if booking['room_number'] == room_number:
            print("Guest  " + str(guest_id) + " : " + str(guest_name) + ", " + str(booking['number_of_guests'] )+

                  " guest[s] from " + str(booking['checkin_month']) + "/" + str(booking['checkin_day']) + " to "
                  + str(booking['checkout_month']) + "/" + str(booking['checkout_day']))
            viewBooking()





def viewBooking():
    print("Would you like to view [G]uest bookings, [R]oom booking, or e[X]it?")
    choice = input().lower()
    if (choice == 'g'):
        guestBookings(bookings)
    elif choice == 'r':
        roomBookings(bookings)
    else:
        mainMenu()




def quit():
    print("Thanks for using FedUni Hotel bookings")


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


def getDay(month):
    if(month == 1 or month == 3 or month==5 or month==7 or month==8 or month==10 or month==12):
        return 31
    elif(month==2):
        return 28
    else:
        return 30


mainMenu()

