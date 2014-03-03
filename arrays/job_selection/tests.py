import unittest
from job_selection import JobSelection
from job_selection import Job

class HighLowTest(unittest.TestCase):

    def setUp(self):
        self.js = JobSelection()

    def test_job_creation(self):
        j = Job(0, 2, 0)

    def test_order_by_finish(self):
        j1 = Job(0, 2, 0)
        j2 = Job(1, 3, 1)
        j3 = Job(3, 5, 2)
        ordered = self.js.order_by_finish([j1, j2, j3])

        self.assertIsInstance(ordered, type([]))
        self.assertEquals(ordered[0].id, j1.id)
        self.assertEquals(ordered[0], j1)
        self.assertIsInstance(ordered[0], Job)

    def test_optimal_jobs(self):
        j1 = Job(0, 2, 0)
        j2 = Job(1, 3, 1)
        j3 = Job(3, 5, 2)
        jobs = [j1, j2, j3]

        ids = self.js.optimal_jobs(jobs)
        self.assertEquals(ids, [0, 2])

        j1 = Job(0, 5, 1)
        j2 = Job(1, 2, 2)
        j3 = Job(0, 2, 3)
        j4 = Job(1, 3, 4)
        j5 = Job(2, 3, 5)
        j6 = Job(4, 5, 6)
        j7 = Job(4, 6, 7)
        j8 = Job(7, 9, 8)

        jobs = [j1, j2, j3, j4, j5, j6, j7, j8]
        ids = self.js.optimal_jobs(jobs)
        #any of the following paths are valid optimial paths
        self.assertIn(ids, [[2, 6, 8], [3, 6, 8], [2, 7, 8], [3, 7, 8]])





