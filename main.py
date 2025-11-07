# Main application script that simulates program execution.
import data_manager

def run_sih_app():
    """Simulates the main application flow."""
    print("--- Running SIH Waste Management App ---")
    
    # This shows a dependency on data_manager.add_waste_record
    print("Adding a new plastic bottle record for user 1...")
    data_manager.add_waste_record(1, "Plastic Bottle", 0.0, 5.0, 10, 2)
    
    # This shows a dependency on data_manager.get_records_by_user
    print("\nFetching all records for user 1...")
    user_records = data_manager.get_records_by_user(1)
    print(user_records)
    
    print("\n--- Application Finished ---")

if __name__ == "__main__":
    run_sih_app()