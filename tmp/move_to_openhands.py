import os
import shutil
import glob

workspace_root = r"f:\AIML projects\synthetic-feedback-panel"
source_dir = os.path.join(workspace_root, ".agents", "skills")
target_dir = os.path.join(workspace_root, ".openhands", "microagents")

if not os.path.exists(source_dir):
    print(f"Source directory {source_dir} does not exist.")
    exit(1)

# Create target directory if it doesn't exist
os.makedirs(target_dir, exist_ok=True)

files = glob.glob(os.path.join(source_dir, "*"))

if not files:
    print("No files found to move.")
    exit(0)

count = 0
for file_path in files:
    filename = os.path.basename(file_path)
    target_path = os.path.join(target_dir, filename)
    
    print(f"Moving {filename} to {target_dir}...")
    shutil.move(file_path, target_path)
    count += 1

print(f"Moved {count} files.")

# Remove source directory if empty
try:
    os.rmdir(source_dir)
    print(f"Removed empty source directory {source_dir}")
except OSError as e:
    print(f"Could not remove source directory (maybe not empty): {e}")

print("Move complete.")
