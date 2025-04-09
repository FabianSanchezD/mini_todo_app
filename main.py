import datetime
import sqlite3

connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS Tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL
);
'''

cursor.execute(create_table_query)
connection.commit()

a = datetime.datetime.now()

def main():
    print("Welcome to my Task Manager!👋")
    print(f"Current date and time: {a.day}/{a.month}/{a.year} {a.hour}:{a.minute}")

    while True:
        option = int(input("Main Menu\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit\nSelect an option: "))

        match option:
            case 1: 
                add_task()

            case 2:
                see_all()
            
            case 3:
                remove_task()

            case 4:
                print("Exiting...")
                print("Thanks for using this small program!")
                connection.close()
                break

            case _:
                print("Invalid option. Please try again.")
                main()

def add_task():
    task = input("Enter a task: ")
    cursor.execute("INSERT INTO Tasks(task) VALUES (?);", (task,))
    connection.commit()
    print(f"Added {task} to the list.")

                

def see_all():
    cursor.execute("SELECT id, task FROM Tasks;")
    tasks = cursor.fetchall()
    if not tasks:
        print("No tasks available.")
    else:
        print("All tasks:")
        for task in tasks:
            print(task)

def remove_task():
    print("Unsure of what the ID is? Click Y.")
    idtask = input("Enter the ID of the task to remove: ")

    if idtask == "Y":
        see_all()
        idtask = input("Enter the ID of the task to remove: ")

    try:
        idtask = int(idtask)
    except ValueError:
        print("Invalid ID. An actual number.")
        return
    cursor.execute("DELETE FROM Tasks WHERE id = ?;", (idtask,))
    connection.commit()

    if cursor.rowcount > 0:
        print(f"Removed task with ID {idtask}.")
    else:
        print(f"No task found with ID {idtask}.")


main()
