def process_grades(input_string):
    raw_items = input_string.split(',')
    valid_scores = []
    
    for item in raw_items:
        item = item.strip() 
        
        try:
            val = float(item)
            if val.is_integer():
                val = int(val)
        except ValueError:
            continue
            
        if 0 <= val <= 100:
            valid_scores.append(val)
            
    if not valid_scores:
        print("Валидные оценки не найдены")
        return 
        
    valid_count = len(valid_scores)
    average = sum(valid_scores) / valid_count
    highest = max(valid_scores)
    lowest = min(valid_scores)
    
    passed_count = sum(1 for x in valid_scores if x >= 50)
    pass_rate = (passed_count / valid_count) * 100
    
    print(f"valid={valid_count}, avg {average:.2f}, high {highest}, low {lowest}, pass {pass_rate:.1f}%")


print("Кейс A:")
process_grades("85, 23, 45, 90, 92")

print("\nКейс B:")
process_grades("88, 47, -5, 101, abc, 73, 50, , 100")

print("\nКейс C:")
process_grades("10, 20, 30")

print("\nКейс D:")
process_grades("abc, , xyz")