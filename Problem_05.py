M = input()
N = int(input())
F = int(input())
X = int(input())

def calculate_fine(name, days, rate, max_fine):
    fine = days * rate
    
    if fine > max_fine:
        fine = float(max_fine)
        print(f"You have accumulated the maximum fine of INR: {max_fine}")
    
    print(f"Book: {name}")
    print(f"Days overdue: {days}")
    print(f"Fine: Rs. {float(fine)}")
    
    return fine

f = calculate_fine(M, N, F, X)
