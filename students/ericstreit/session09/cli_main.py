#Lesson09
#Objected Oriented Mailroom Exercise 09 - CLI Menu
#
#!/usr/bin/env python3
#importe modules
from donor_models import *
from pathlib import Path
from sys import exit
import os

## OK so this ended up turning more into a config file than the menu cli since
# the menus were all created as classes in the donor_models.py file.



#define variables

data_folder = r'C:\pythonuw\Fall2018-PY210A\students\ericstreit\files'
# note to self: make another one like above for the instructor that points to the current folder?

#define menus
# This creates the menu as a class

#should the other menus be subclasses??? probably! (DONE!)

main_menu  = Menu("MAIN MENU")
report_menu = Report("REPORT MENU")
thankyou_menu = ThankYou("SEND A THANK YOU")


# define menu options
# These are the choices that will display to the user in a menu
# Be sure to create a dictionary below that will tie to the choices

main_menu.menu_options = ["(R)eport Menu", "(S)end a Thank You",
                          "(A)dd a new donation",
                          "(Q)uit"]


report_menu.menu_options = ["Create report of (A)ll donors",
                            "Create report of a (S)ingle donor",
                            "(B)ack to Main Menu",
                            "(Q)uit"]



thankyou_menu.menu_options = ["Send a Thank You to a (S)ingle donor",
                              "Send a Thank You to (A)ll donors",
                              "(B)ack to Main Menu",
                              "(Q)uit"]



#define the menu dictionaries
#each selection should point to a function

main_menu.dict = {"r": report_menu.menu, "s": thankyou_menu.menu, "a": main_menu.new_donation, "q": main_menu.quit}
report_menu.dict = {"a": report_menu.full_donor_report, "s": report_menu.single_donor_report, "b": main_menu.menu, "q": report_menu.quit}
thankyou_menu.dict = {"a": thankyou_menu.all_donor_thankyou, "s": thankyou_menu.single_donor_thankyou, "b": main_menu.menu, "q": thankyou_menu.quit}

#let's put some donors in here for testing!

hestershaw = Donors("Hester Shaw")
donor_dict['hestershaw'] = hestershaw
hestershaw.add_donations(500)
hestershaw.add_donations(34)

grike = Donors("Grike")
donor_dict['grike'] = grike
grike.add_donations(3)

tomnatsworthy = Donors("Tom Natsworthy")
donor_dict['tomnatsworthy'] = tomnatsworthy
tomnatsworthy.add_donations(1003)
tomnatsworthy.add_donations(745)
tomnatsworthy.add_donations(10)

# run the program!

main_menu.menu()

#for testing
if __name__=="__main__":
    main_menu.menu
