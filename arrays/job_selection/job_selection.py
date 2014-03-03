class JobSelection:

    def order_by_finish(self, jobs):
        jobs.sort(key = lambda x: x.end)
        return jobs

    def optimal_jobs(self, jobs):

        if (len(jobs) == 0):
            return

        jobs = self.order_by_finish(jobs)

        current_job = 0
        ids = []
        ids.append(jobs[current_job].id)

        i = 0

        while (i < len(jobs)):
            if jobs[i].start > jobs[current_job].end: 
                #does job start after this one is finished?
                current_job = i
                ids.append(jobs[current_job].id)
            i += 1
        return ids     

class Job:
    def __init__(self, start, end, id):
        self.start = start
        self.end = end
        self.id = id

if __name__ == "__main__":
    j1 = Job(0, 5, 1)
    j2 = Job(1, 2, 2)
    j3 = Job(0, 2, 3)
    j4 = Job(1, 3, 4)
    j5 = Job(2, 3, 5)
    j6 = Job(4, 5, 6)
    j7 = Job(4, 6, 7)
    j8 = Job(7, 9, 8)
    js = JobSelection()
    jobs = [j1, j2, j3, j4, j5, j6, j7, j8]
    print js.optimal_jobs(jobs)