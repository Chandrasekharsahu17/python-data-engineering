import subprocess
import sys
import os

def run_script(script_path):
    """Run a Python script and display its output."""
    print(f"\n{'='*50}")
    print(f"Running: {script_path}")
    print('='*50)
    result = subprocess.run([sys.executable, script_path], capture_output=False)
    return result.returncode

def main():
    """Main entry point to run practice scripts."""
    daily_practice_dir = "daily_practice"
    
    scripts = [
        "day1_Variable_Function.py",
        "day2_Print_functio.py",
        "Day_6_list.py",
        "Day_6_list_2.py",
    ]
    
    interactive_scripts = [
        "Day_4_operator.py",
        "day_5-if_else.py",
    ]
    
    print("Python Data Engineering Practice")
    print("================================")
    
    for script in scripts:
        script_path = os.path.join(daily_practice_dir, script)
        if os.path.exists(script_path):
            run_script(script_path)
    
    print("\n" + "="*50)
    print("All non-interactive practice scripts completed!")
    print("="*50)
    
    if interactive_scripts:
        print("\nNote: The following scripts require user input and")
        print("can be run individually in the Shell:")
        for script in interactive_scripts:
            print(f"  python daily_practice/{script}")

if __name__ == "__main__":
    main()
