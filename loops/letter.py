def main():
    people = int(input("How many people do you want to invite?  "))
    
    
    for person in  range(people):
        receiver = input("Enter the receiver name: ").strip()
        sender = input("Enter sender name: ").strip()
        print(write_letter(receiver, sender)) 
        person  = person -1
        
        
    
def write_letter(receiver, sender):
    
    return f"""
=================================================
   Dear {receiver}
   You are cordially invited to a ball at 
   a Peach's Castle this evening, 7:00PM.
   Sincerely,
   {sender}
   
"""


main()