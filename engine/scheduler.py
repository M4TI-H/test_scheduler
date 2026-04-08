from collections import deque
from core.servers import ServerNode
from core.hardware import GPU

# represents single task to validate
class ValidationJob:
    def __init__(self, job_id: str, required_vram: int):
        self.job_id = job_id
        self.required_vram = required_vram
        self.status = "PENDING"

    def __str__(self):
        return f"<Job {self.job_id} | Requires {self.required_vram}GB VRAM | Status: {self.status}>"
    
class JobScheduler:
    def __init__(self, server: ServerNode):
        self.server = server
        self.queue = deque()
    
    def submit_job(self, job: ValidationJob):
        self.queue.append(job)
        print(f"[SCHEDULER] Job {job.job_id} added to queue.")

    def run_queue(self):
        while self.queue:
            job = self.queue.popleft()
            job_assigned = False
            
            for device in self.server.devices:
                if device.status == "IDLE" and isinstance(device, GPU) and device.vram >= job.required_vram:
                    device.status = "IN_USE"
                    job.status = "RUNNING"
                    print(f"Job {job.job_id} has been assigned to {device.device_id} GPU.")
                    job_assigned = True
                    break

            if not job_assigned:
                print(f"Insufficient resources to assign job {job.job_id} to a device.")