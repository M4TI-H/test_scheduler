from typing import List
from core.hardware import HardwareDevice, GPU

class ServerNode:
    def __init__(self, server_id: str):
        self.server_id = server_id
        self.devices: List[HardwareDevice] = []

    def add_device(self, device: HardwareDevice):
        self.devices.append(device)
        print(f"[SERVER {self.server_id}] new device connected: {device.device_id}")

    @property   # allows to use the method as it was a property
    def total_gpu_memory(self) -> int:
        total = 0
        for device in self.devices:
            if isinstance(device, GPU):
                total += device.vram

        return total
    
    def __len__(self) -> int:
        return len(self.devices)