"""Extract info from an email address
Bianca"""

servers = {"gmail": "Google", "yahoo": "Yahoo", "hotmail": "Microsoft", "outlook": "Microsoft"}

print("\nProgram that Extract important info from an email address\n")

while (True):

    address = input("\nEmail address: ").strip()

    if '@' in address:

        at = address.index('@')

        name = address[:at]

        domain = address[at+1:]

        host = domain[:domain.index('.')]

        print("Name: ", name.capitalize())

        print("Domain is: ", domain)

        print("From: ", servers[host])

    else:
        print("\nPlease add a valid email")

    cond = input("\nPress "" X "" for exit ").strip()

    if cond == "x" or cond == "X":
        break
