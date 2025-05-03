active_db_file = 'app.db'
backup_db_file = 'backup.db'

def create_backup():
    """
    Create a backup of the active database file.
    """
    import shutil
    try:
        shutil.copyfile(active_db_file, backup_db_file)
        print(f"Backup of {active_db_file} created as {backup_db_file}.")
    except Exception as e:
        print(f"Error creating backup: {e}")

def restore_backup():
    """
    Restore the active database file from the backup.
    """
    import shutil
    try:
        shutil.copyfile(backup_db_file, active_db_file)
        print(f"Backup {backup_db_file} restored to {active_db_file}.")
    except Exception as e:
        print(f"Error restoring backup: {e}")

# create a function to evaluate the user input after informing the user the options
def evaluate_user_input():
    """
    Evaluate the user input after informing the user of the options.
    """
    print("Please choose an option:")
    print("1. Create Backup")
    print("2. Restore Backup")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == '1':
        create_backup()
    elif choice == '2':
        restore_backup()
    elif choice == '3':
        print("Exiting the program.")
        return
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Call the function to evaluate user input
    evaluate_user_input()
    # Uncomment the following lines to test the backup and restore functions directly
    # create_backup()
    # restore_backup() 