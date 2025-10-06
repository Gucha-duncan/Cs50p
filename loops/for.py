
def main():
 while True:
  count = int(input("How many time do you want it to repeat? ").strip())
  if count > 0:
     break
 for _ in range(count):
    print("My bro is safe")
    
 greeting(5)
 
    
def greeting(greet):
   
    for _ in range(greet):
        print ("Hello Kenya!")

   
main()