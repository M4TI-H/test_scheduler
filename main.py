from core.servers import ServerNode
from core.hardware import GPU, CPU

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