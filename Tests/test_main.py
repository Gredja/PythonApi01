import unittest
import multiprocessing

if __name__ == '__main__':
    # Number of parallel processes
    num_processes = 4

    # Create a process pool
    pool = multiprocessing.Pool(processes=num_processes)

    # Run tests in parallel
    pool.ma()

    # Close the pool
    pool.close()
    pool.join()

    unittest.main()
