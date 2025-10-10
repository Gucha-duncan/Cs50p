def main():
    names = ['Gucha', 'Mamu', 'Gecha', 'Jayv', 'Clinton', 'Duncan', 'Bowser']
    
    for name in names:
        sender = 'Faith'
        print(write_letter(name, sender))

        
        
    
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