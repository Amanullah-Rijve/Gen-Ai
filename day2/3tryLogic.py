import random

max_try = 3
attempt = 1

while attempt <= max_try:
    print(f"Attempt {attempt}: calling the api...")
    success = random.choice([True,False])
    
    if success:
        print("Response recieved")
        break
    else:
        print("Failled")
        attempt+=1
else:
    print("All try failled")