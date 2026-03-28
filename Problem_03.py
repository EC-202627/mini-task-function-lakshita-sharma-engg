M = input()
N = int(input())

def calculate_fine(name, days):
    fine = days * 5
    
    if fine > 150:
        fine = 150.0
    
    print(f"Book: {name}")
    print(f"Days overdue: {days}")
    print(f"Fine: Rs. {float(fine)}")
    
    if days * 5 > 150:
        print(f"You have accumulated the maximum fine of INR: 150.0")
    
    return fine

f = calculate_fine(M, N)
