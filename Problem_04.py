M = input()
N = int(input())
F = float(input())

def calculate_fine(name, days, rate):
    fine = days * rate
    
    if fine > 150:
        fine = 150.0
    
    print(f"Book: {name}")
    print(f"Days overdue: {days}")
    print(f"Fine: Rs. {fine}")
    
    if days * rate > 150:
        print("You have accumulated the maximum fine of INR: 150.0")
    
    return fine

f = calculate_fine(M, N, F)
