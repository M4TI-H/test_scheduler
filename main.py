from core.servers import ServerNode
from core.hardware import GPU, CPU
from parser.log_reader import create_dummy_logs, gen_logs
from parser.decorators import timer

server = ServerNode("SRV-001")
cpu = CPU("CPU-001", 100, "Core I5")
gpu1 = GPU("GPU-001", 8, "Arc")
gpu2 = GPU("GPU-002", 16, "Arc Pro")

server.add_device(cpu)
server.add_device(gpu1)
server.add_device(gpu2)

print(cpu)
print(f"Devices connected to the server: {len(server)}")
print(f"Total server VRAM: {server.total_gpu_memory}")

print("\n ##################################### \n")

create_dummy_logs("test_results.txt")


@timer
def analyze_logs(filename: str) -> int:
  error_count = 0
  generated_logs_list = gen_logs(filename)

  for line in generated_logs_list:
    if line.find("ERROR") > 0:
      error_count += 1

  return error_count

if __name__ == "__main__":
  filename = "test_results.txt"
  total_errors = analyze_logs(filename)
  print(f"Errors found: {total_errors}")