import random

def create_dummy_logs(filename: str, lines: int = 100000):
  print(f"Creating file {filename} with {lines} lines")

  with open(filename, "w") as file:
    for i in range(lines):
      if random.random() < 0.05:
        file.write(f"[{i}] ERROR: GPU memory leak!\n")
      else:
        file.write(f"[{i}] INFO: Test passed.\n")
  print("File ready")

def gen_logs(filename: str):
  with open(filename, "r") as file:
    for line in file:
      yield line.strip()