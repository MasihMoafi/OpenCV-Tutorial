# Run All Assignments - Computer Vision Session 2
# Masih Moafi - Isfahan University of Technology
# Dr. Mohammad Davarpanah Jazi

import subprocess
import sys

assignments = [
    "assignment1_sampling.py",
    "assignment2_quantization.py", 
    "assignment3_colorspaces.py",
    "assignment4_noise.py",
    "assignment5_filters.py"
]

print("Running all Computer Vision assignments...")
print("=" * 50)

for i, assignment in enumerate(assignments, 1):
    print(f"\n[{i}/5] Running {assignment}...")
    try:
        result = subprocess.run([sys.executable, assignment], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ {assignment} completed successfully")
        else:
            print(f"✗ {assignment} failed:")
            print(result.stderr)
    except Exception as e:
        print(f"✗ Error running {assignment}: {e}")

print("\n" + "=" * 50)
print("All assignments completed!")
print("Check the generated PNG files for results.")