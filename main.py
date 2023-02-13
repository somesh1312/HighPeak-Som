def find_remaining_jobs(jobs):
    n = len(jobs)
    jobs.sort(key=lambda x: x[1])  # sort by end time
    selected_job = jobs[0]
    remaining_jobs = []
    total_earnings = 0
    for i in range(1, n):
        job = jobs[i]
        if job[0] >= selected_job[1]:
            # this job doesn't overlap with the selected job
            total_earnings += selected_job[2]
            selected_job = job
        else:
            remaining_jobs.append(job)
    total_earnings += selected_job[2]
    num_remaining_jobs = len(remaining_jobs)
    return [num_remaining_jobs, total_earnings]

# Example usage:
n = int(input("Enter the number of Jobs\n"))
jobs = []
for i in range(n):
    print("Enter job start time, end time, and earnings")
    start_time = int(input())
    end_time = int(input())
    earnings = int(input())
    jobs.append((start_time, end_time, earnings))
result = find_remaining_jobs(jobs)
print("The number of tasks and earnings available for others")
print("Task:", result[0])
print("Earnings:", result[1])