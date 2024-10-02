from pathlib import Path

folder_original = Path(input("Provide original path")[1:-1])
folder_destination = Path(input("Provide destination path")[1:-1])

folder_destination.mkdir(exist_ok=True)

for entry in folder_original.iterdir():
    if entry.is_file():
        destination_path = folder_destination / entry.name
        entry.rename(destination_path)
        print(f"Moved: {entry} to {destination_path}")

print("All files have been moved")
