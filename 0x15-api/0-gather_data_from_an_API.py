import requests

def get_employee_todo_progress(employee_id):
    # Make a GET request to fetch the employee's TODO list
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    
    if response.status_code == 200:
        todos = response.json()
        completed_tasks = []
        
        # Count the number of completed tasks and collect their titles
        for todo in todos:
            if todo["completed"]:
                completed_tasks.append(todo["title"])
        
        # Display the progress information
        print(f"Employee {todos[0]['username']} is done with tasks({len(completed_tasks)}/{len(todos)}):")
        
        # Display the titles of completed tasks
        for task in completed_tasks:
            print("\t", task)
    else:
        print("Error:", response.status_code)

# Example usage with employee ID 1
employee_id = 1
get_employee_todo_progress(employee_id)
