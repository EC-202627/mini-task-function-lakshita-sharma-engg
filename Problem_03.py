def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
    
    if fine > max_fine:
        fine = max_fine
        max_flag = True
    else:
        max_flag = False
    
    print(f"Book: {book_title}")
    print(f"Days overdue: {days_overdue}")
    print(f"Fine: Rs. {fine}")
    
    if max_flag:
        print(f"You have accumulated the maximum fine of INR: {max_fine}")

data = input().split()
book_title = " ".join(data[:-1])
days_overdue = int(data[-1])

calculate_fine(book_title, days_overdue)
