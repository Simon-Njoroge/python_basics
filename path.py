from pathlib import Path

path=Path("class")
for file in path.glob("*"):
 print(file)