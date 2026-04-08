from abc import ABC, abstractmethod

# abstract base class for all hardware classes
class HardwareDevice(ABC):
    MANUFACTURER = "Intel"


    def __init__(self, device_id: str):
        self.device_id = device_id
        self.status = "IDLE"
    

    @abstractmethod     # requires every inheriting method to implement the run_diagnostics method
    def run_diagnostics(self) -> bool:
        pass


class GPU(HardwareDevice):
    def __init__(self, device_id: str, vram: int, model: str):
        super().__init__(device_id) # call HardwareDevice __init__ method
        self.vram = vram
        self.model = model

    def __str__(self) -> str:
        return f"<{HardwareDevice.MANUFACTURER} GPU {self.model} | ID: {self.device_id} | VRAM: {self.vram}GB | Status: {self.status}>"

    def run_diagnostics(self) -> bool:
        print(f"Running diagnostics on GPU {self.model} (ID: {self.device_id})...")
        self.status = "IN_USE"
        return True
    
    
class CPU(HardwareDevice):
    def __init__(self, device_id: str, cores: int, model: str):
        super().__init__(device_id)
        self.cores = cores
        self.model = model

    def __str__(self) -> str:
        return f"<{HardwareDevice.MANUFACTURER} CPU {self.model} | ID: {self.device_id} | cores: {self.cores} | Status: {self.status}>"


    def run_diagnostics(self) -> bool:
        print(f"Running diagnostics on CPU {self.model} (ID: {self.device_id})...")
        self.status = "IN_USE"
        return True

