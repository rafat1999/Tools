import time
import os
from colorama import Fore, Style, init
import pandas as pd

# Initialize colorama
init(autoreset=True)

def print_hacker_face():
    # Define the hacker face pattern using multi-line string
    face = """
      *****       *****
    *       *   *       *
    *       *   *       *
      *****       *****
            *   *
          *       *
        *           *

        
    * * * * * *       * * * * * *      * * * * * *        * * * * * *
    *         *       * * * * * *      * * * * * *        * * * * * *
    * * * * * *           * *              * *                * *
    * *                   * *              * *                * *
    * *                   * *              * *                * *
    * *                   * *              * *                * *
    * *                   * *              * *                * *
    * * * * * *           * *              * *                * *
    *         *       * * * * * *          * *            * * * * * *
    * * * * * *       * * * * * *          * *            * * * * * *
    """
    # Clear screen
    os.system("clear")

    # Print each line of the face pattern
    for line in face.splitlines():
        print(Fore.GREEN + line)
        time.sleep(0.1)  # Adjust time for faster or slower animation

def match_input_with_excel():
    # Load Excel file
    file_path = "database.xlsx"  # Replace with your Excel file path
    try:
        df = pd.read_excel(file_path)

        # Take input from the user
        user_input = input("\nEnter the value to search: ")

        # Check if user input exists in the DataFrame
        if user_input in df.values:
            print(Fore.GREEN + "Match found in the database!")
        else:
            print(Fore.RED + "No match found.")
    except FileNotFoundError:
        print(Fore.RED + f"Error: '{file_path}' not found. Please check the file path.")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")

# Execute the functions
print_hacker_face()
match_input_with_excel()
