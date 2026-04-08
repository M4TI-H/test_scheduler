from core.servers import ServerNode
from core.hardware import GPU, CPU
from parser.log_reader import create_dummy_logs, gen_logs
from parser.decorators import timer
from engine.scheduler import JobScheduler, ValidationJob

@timer
def analyze_logs(filename: str) -> int:
    error_count = 0
    generated_logs_list = gen_logs(filename)

    for line in generated_logs_list:
        if line.find("ERROR") > 0:
            error_count += 1

    return error_count

def main():
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

    filename = "test_results.txt"
    total_errors = analyze_logs(filename)
    print(f"Errors found: {total_errors}")

    print("\n ##################################### \n")

    scheduler = JobScheduler(server)
    scheduler.submit_job(ValidationJob("JOB-001", required_vram=12)) 
    scheduler.submit_job(ValidationJob("JOB-002", required_vram=6)) 
    scheduler.submit_job(ValidationJob("JOB-003", required_vram=8)) 

    scheduler.run_queue()

if __name__ == "__main__":
    main()