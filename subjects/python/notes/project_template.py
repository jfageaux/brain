"""
Python Project Template for Comment-Driven Development
====================================================

This template embodies the core learning philosophy: extensive documentation and comments
that serve as both functional code and educational content.

Project: [Replace with your project name]
Author: [Your name]
Date: [Today's date]
Learning Goals: [What CS concepts are you exploring?]
Cross-Subject Integration: [How does this connect to other subjects?]
Estimated Lines of Code: [Your target - helps track complexity growth]

Purpose:
[Write 2-3 sentences describing what this script does and why it's useful]

Learning Context:
[Explain what you're trying to learn or practice with this project]

Design Decisions:
[Document major choices you made and why - data structures, algorithms, libraries]
"""

# ==================================================================================
# IMPORT SECTION - Document why each import is needed
# ==================================================================================

# Standard library imports (built into Python)
import os          # For file and directory operations
import sys         # For system-specific parameters and functions
import json        # For JSON data parsing and generation
import argparse    # For command-line argument parsing

# Third-party imports (need to be installed via pip)
# import requests  # For HTTP requests and API interactions
# import pandas as pd  # For data manipulation and analysis
# import matplotlib.pyplot as plt  # For data visualization

# Local imports (your own modules)
# from my_utilities import helper_functions

# ==================================================================================
# GLOBAL CONSTANTS - Use ALL_CAPS for constants
# ==================================================================================

# Document why each constant exists and how its value was chosen
DEFAULT_CONFIG_FILE = "config.json"  # Standard location for configuration
MAX_RETRY_ATTEMPTS = 3  # Reasonable retry limit for network operations
DEBUG_MODE = True  # Set to False for production, True for development

# ==================================================================================
# HELPER FUNCTIONS - Each function should have a single, clear purpose
# ==================================================================================

def validate_input(user_input):
    """
    Validate user input to ensure it meets requirements.
    
    Args:
        user_input (str): The input string to validate
        
    Returns:
        bool: True if valid, False otherwise
        
    Raises:
        ValueError: If input is empty or contains invalid characters
        
    Learning Notes:
        - Input validation is crucial for robust programs
        - Always validate external data (user input, file content, API responses)
        - Clear error messages help users understand what went wrong
    """
    # Check for empty input - this is a common edge case to handle
    if not user_input or not user_input.strip():
        raise ValueError("Input cannot be empty or only whitespace")
    
    # Add your specific validation logic here
    # Example: Check for forbidden characters, length limits, format requirements
    forbidden_chars = ['<', '>', '&']  # Common problematic characters
    for char in forbidden_chars:
        if char in user_input:
            raise ValueError(f"Input contains forbidden character: {char}")
    
    return True


def process_data(data):
    """
    Process the input data according to business logic.
    
    Args:
        data: Input data to process (type depends on your use case)
        
    Returns:
        Processed data in the appropriate format
        
    Learning Notes:
        - This is where your main algorithm/logic lives
        - Break complex processing into smaller, testable functions
        - Document the transformation your function performs
        - Consider edge cases: empty data, unexpected formats, etc.
    """
    # Document your processing steps clearly
    # Step 1: Data cleaning and preprocessing
    if not data:
        print("Warning: No data to process")
        return None
    
    # Step 2: Main processing logic
    # (Replace this with your actual processing)
    processed_result = f"Processed: {data}"
    
    # Step 3: Post-processing and validation
    # Ensure the result meets expected criteria
    
    return processed_result


def save_results(results, filename):
    """
    Save processing results to a file.
    
    Args:
        results: The data to save
        filename (str): Path to the output file
        
    Learning Notes:
        - File I/O is a common source of errors - handle exceptions
        - Consider different file formats (JSON, CSV, plain text)
        - Always close files properly (using 'with' statement)
        - Think about file permissions and directory existence
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        # Use 'with' statement for automatic file closing
        with open(filename, 'w', encoding='utf-8') as file:
            # Choose appropriate format based on data type
            if isinstance(results, (dict, list)):
                json.dump(results, file, indent=2)  # Pretty-printed JSON
            else:
                file.write(str(results))
                
        print(f"Results saved successfully to {filename}")
        
    except PermissionError:
        print(f"Error: Permission denied when writing to {filename}")
    except OSError as e:
        print(f"Error: Could not write file {filename}: {e}")


# ==================================================================================
# MAIN FUNCTION - The entry point of your program
# ==================================================================================

def main():
    """
    Main program execution function.
    
    This function orchestrates the entire program flow:
    1. Parse command-line arguments (if any)
    2. Load configuration
    3. Get user input
    4. Process the data
    5. Save and display results
    
    Learning Notes:
        - Keep main() focused on coordination, not detailed logic
        - Handle exceptions at the appropriate level
        - Provide clear feedback to the user
        - Structure code for easy testing and debugging
    """
    
    # ============================================================================
    # STEP 1: Setup and Configuration
    # ============================================================================
    
    print("="*60)
    print("PYTHON PROJECT TEMPLATE - Comment-Driven Development")
    print("="*60)
    print()
    
    # Set up command-line argument parsing (useful for many projects)
    parser = argparse.ArgumentParser(description="Template for Python learning projects")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("--config", default=DEFAULT_CONFIG_FILE, help="Configuration file path")
    args = parser.parse_args()
    
    # Enable debug mode if requested
    global DEBUG_MODE
    DEBUG_MODE = args.debug
    
    if DEBUG_MODE:
        print("[DEBUG] Debug mode enabled")
        print(f"[DEBUG] Using config file: {args.config}")
    
    # ============================================================================
    # STEP 2: Get User Input
    # ============================================================================
    
    try:
        # Prompt user for input with clear instructions
        print("Please enter some data to process:")
        user_input = input("> ").strip()
        
        # Validate the input before proceeding
        validate_input(user_input)
        
        if DEBUG_MODE:
            print(f"[DEBUG] Received input: '{user_input}'")
    
    except ValueError as e:
        print(f"Error: {e}")
        print("Please try again with valid input.")
        return 1  # Return non-zero to indicate error
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return 0
    
    # ============================================================================
    # STEP 3: Process the Data
    # ============================================================================
    
    print("\nProcessing data...")
    
    try:
        # Call your main processing function
        results = process_data(user_input)
        
        if results is None:
            print("No results to display.")
            return 1
        
        if DEBUG_MODE:
            print(f"[DEBUG] Processing complete. Results: {results}")
    
    except Exception as e:
        print(f"Error during processing: {e}")
        if DEBUG_MODE:
            import traceback
            traceback.print_exc()
        return 1
    
    # ============================================================================
    # STEP 4: Display and Save Results
    # ============================================================================
    
    # Display results to user
    print("\nResults:")
    print("-" * 40)
    print(results)
    print("-" * 40)
    
    # Ask user if they want to save results
    save_choice = input("\nWould you like to save these results? (y/n): ").lower()
    
    if save_choice in ['y', 'yes']:
        # Generate output filename with timestamp
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"results_{timestamp}.txt"
        
        # Save the results
        save_results(results, output_file)
    
    # ============================================================================
    # STEP 5: Cleanup and Exit
    # ============================================================================
    
    print("\nProgram completed successfully!")
    return 0  # Return 0 to indicate success


# ==================================================================================
# ADDITIONAL HELPER FUNCTIONS - Add more as your project grows
# ==================================================================================

def load_config(config_file):
    """
    Load configuration from a JSON file.
    
    Args:
        config_file (str): Path to configuration file
        
    Returns:
        dict: Configuration data
        
    Learning Notes:
        - Configuration files make programs more flexible
        - JSON is a common, human-readable format
        - Always handle missing or malformed config files
    """
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file {config_file} not found, using defaults")
        return {}
    except json.JSONDecodeError:
        print(f"Error parsing config file {config_file}")
        return {}


def setup_logging():
    """
    Set up logging for the application.
    
    Learning Notes:
        - Logging is better than print statements for real applications
        - Different log levels (DEBUG, INFO, WARNING, ERROR) serve different purposes
        - Logs help debug issues and understand program behavior
    """
    import logging
    
    # Configure logging format
    logging.basicConfig(
        level=logging.DEBUG if DEBUG_MODE else logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('application.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    return logging.getLogger(__name__)


# ==================================================================================
# TESTING FUNCTIONS - Write tests for your functions
# ==================================================================================

def test_validate_input():
    """
    Test the validate_input function with various inputs.
    
    Learning Notes:
        - Writing tests helps catch bugs early
        - Test both valid and invalid inputs
        - Consider edge cases and boundary conditions
    """
    # Test valid input
    try:
        assert validate_input("valid input") == True
        print("✓ Valid input test passed")
    except AssertionError:
        print("✗ Valid input test failed")
    
    # Test invalid input (empty)
    try:
        validate_input("")
        print("✗ Empty input test failed - should have raised ValueError")
    except ValueError:
        print("✓ Empty input test passed")
    
    # Add more tests as needed


def run_tests():
    """
    Run all test functions.
    
    Learning Notes:
        - Automated testing saves time and prevents regressions
        - Run tests frequently during development
        - Good tests document expected behavior
    """
    print("Running tests...")
    test_validate_input()
    print("All tests completed.")


# ==================================================================================
# PROGRAM ENTRY POINT
# ==================================================================================

if __name__ == "__main__":
    """
    This block only runs when the script is executed directly, not when imported.
    
    Learning Notes:
        - This is a Python idiom that makes modules more reusable
        - Allows your script to be both a program and a library
        - Makes testing easier since you can import functions without running main()
    """
    
    # Uncomment this line to run tests before main execution
    # run_tests()
    
    # Run the main program and exit with the return code
    exit_code = main()
    sys.exit(exit_code)


# ==================================================================================
# LEARNING REFLECTION SECTION
# ==================================================================================

"""
REFLECTION QUESTIONS (Answer these after completing your project):

1. What was the most challenging part of this project?

2. What new Python concepts did you learn or practice?

3. How does this project connect to your other subjects (AI, Chinese, Philosophy)?

4. What would you do differently if you started this project again?

5. What features could you add to make this project more useful or interesting?

6. How could you optimize this code for better performance?

7. What security considerations should you think about for this type of application?

8. How could you make this code more testable and maintainable?

NEXT STEPS:
- [ ] Add error handling for edge cases you discovered
- [ ] Write comprehensive tests for all functions
- [ ] Add logging instead of print statements
- [ ] Consider adding a GUI interface
- [ ] Think about how to deploy this for others to use
- [ ] Document any performance optimizations needed
- [ ] Plan integration with your other learning projects
"""
