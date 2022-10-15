jobs = [int(el) for el in input().split(', ')]
index = int(input())
min_number = 999999999
clock_cycles = 0
stack = []
job_found = False

while True:
    if job_found:
        break

    smallest_num = min(jobs)
    clock_cycles += smallest_num

    i_smallest_num = jobs.index(smallest_num)
    if i_smallest_num == index:
        job_found = True
        break

    jobs[i_smallest_num] = float("inf")

print(clock_cycles)