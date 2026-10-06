import socket
import os
import webbrowser

target = input("Enter the domain or IP: ")

while True:
    print()
    print("1. Find IP of domain")
    print("2. Google dorking")
    print("3. DNS details")
    print("4. Emails and employee details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
       
        ip = socket.gethostbyname(target)
        print("IP address:", ip)

    elif choice == "2":
       
        link = "https://www.google.com/search?q=site:" + target + " inurl:admin"
        print(link)
        webbrowser.open(link)

    elif choice == "3":
       
        os.system("nslookup " + target)

    elif choice == "4":
       
        link1 = "https://www.google.com/search?q=intext:@" + target
        link2 = "https://www.google.com/search?q=site:linkedin.com " + target
        print("Emails:", link1)
        print("Employees:", link2)
        webbrowser.open(link1)

    elif choice == "5":
        print("Bye")
        break

    else:
        print("Wrong choice, try again")