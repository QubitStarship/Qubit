import unreal
import os
import shutil
import datetime

# Get Unreal's default screenshot directory
screenshot_base_path = unreal.Paths.project_saved_dir() + "Screenshots/Windows/"

# Create a timestamped folder
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
session_folder = os.path.join(screenshot_base_path, timestamp)

# Ensure the folder exists
os.makedirs(session_folder, exist_ok=True)

# Function to move new screenshots into the session folder
def move_screenshots():
    for file in os.listdir(screenshot_base_path):
        if file.endswith(".png"):  # Only move image files
            src = os.path.join(screenshot_base_path, file)
            dest = os.path.join(session_folder, file)
            shutil.move(src, dest)
            unreal.log(f"Moved screenshot: {file} to {session_folder}")

# Bind the function to Unreal's Tick event so it checks regularly
@unreal.uclass()
class ScreenshotMover(unreal.Actor):
    @unreal.ufunction(override=True)
    def tick(self, delta_time: float):
        move_screenshots()

# Register the mover
unreal.log("Screenshot manager started.")
actor = ScreenshotMover()