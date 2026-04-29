# Project 06: Neuro-Priority Radar
# An algorithmic approach to task management

def calculate_priority(tasks):
    print("\n--- Optimized Task Priority ---")
    # Sort tasks based on the calculated score (highest first)
    sorted_tasks = sorted(tasks, key=lambda x: x['score'], reverse=True)
    
    for i, task in enumerate(sorted_tasks, 1):
        print(f"{i}. {task['name']} [Score: {task['score']:.2f}]")

def main():
    print("--- Neuro-Priority Radar v1.0 ---")
    tasks = []
    
    print("Enter tasks. For Importance/Urgency, use scale 1-10.")
    while True:
        name = input("\nTask Name (or 'stop' to calculate): ")
        if name.lower() == 'stop': break
        
        try:
            imp = int(input(f"Importance of '{name}': "))
            urg = int(input(f"Urgency of '{name}': "))
            
            # Logic: Weighted average for priority score
            score = (imp * 0.6) + (urg * 0.4)
            tasks.append({'name': name, 'score': score})
            
        except ValueError:
            print("Invalid input. Please use numbers 1-10.")

    if tasks:
        calculate_priority(tasks)
    else:
        print("No tasks to prioritize.")

if __name__ == "__main__":
    main()