candidates = {
    "BJP" : 0,
    "AAP" : 0,
    "CONGRESS" : 0,
    "OTHERS" : 0
}

def vote():
    print("======CANDIDATES======")
    for name in candidates:
        print("->",name)

    choice = input("Enter candidate name : ")

    if choice in candidates:
        candidates[choice] = candidates[choice]+1
        print(f"Vote recorded for {choice}")
    else:
        print("Invalid candidate name!!!")

def result():
    print("=====VOTING RESULT=====")
    
    for name , votes in candidates.items():
        print(f"{name} : {votes} votes")

    max_votes = 0
    winners = []

    # Step 1: Find the maximum votes
    for votes in candidates.values():
        if votes > max_votes:
            max_votes = votes

   # Step 2: Find candidate(s) with max votes
    for name, votes in candidates.items():
        if votes == max_votes:
            winners.append(name)

    print("Winner(s): ", winners)    

while True:
    print("==== Voting Menu ====")
    print("1. Vote")
    print("2. Show Results & Winner")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        vote()
    elif choice == "2":
        result()
    elif choice == "3":
        print("Exiting... Thank you for voting!")
        break
    else:
        print("Invalid choice. Try again.\n")    
    



