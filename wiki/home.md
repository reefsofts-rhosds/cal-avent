# Welcome to Cal-Avent's wiki!
### What is Cal-Avent?
Cal-Avent is a solution for a class's advents calendar. It was developped by me when i was 13. The principle is simlpe: every student is typed in in the Database (table Eleve) and is affected a random number from 1 to 32 (or the value configured in the webapp/backend/models.py by bootstrap.sh). Every day, the program picks you some random students.
### What technologies does it use?
It uses python3.10, django 5.1 and Django-Unfold.
### How to set it up?
a. Local install (recommended if possible) (only on Linux or MacOS/any Unix)
You need to install git, pyhton3.10 or greater (which is probably already installed) and any version of Django over 5.0, and to be in your favourite terminal
1. Clone this repo:
''' 
git clone https://github.com/reefsofts-rhosds/cal-avent.git
'''
2. Get to the folder:
'''
cd ./cal-avent
'''
3. Allow the setup to run:
'''
chmod +x ./bootstrap.sh
'''
4. Run the setup:
'''
./bootstrap.sh
'''
5. Answer it questions
6. Run the server:
'''
cd webapp && python3 manage.py runserver
'''
