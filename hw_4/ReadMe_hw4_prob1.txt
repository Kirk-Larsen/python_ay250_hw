In this notebook, we compare execution times (and rates) for a 
Monte Carlo simulation approximating the value of pi. We compare
a simple serial implementation against an implementation using
concurrent.futures and an implementation using dask. In this simulation,
points are randomly dropped in the quadrant [0,1]x[0,1] and checked to see
if the point lies within part of a circle inscribed in the quadrant. We use
10 - 10,000,000 points (in steps of 10^n), recording execution time and point
rate. This is done for a single run over the range 10 - 10,000,000 and also
for 10 runs over the range 10 - 10,000,000 in order to extract means and
standard deviations. 

Processor: MacBook 2.6 GHz Intel Core i5, 2 "cores"

We observe that for a number of points dropped between 10 - 10^4, the serial implementation is actually faster than both of the parallelized implementations. 
This is because setting up the environment for a parallel calculation has a cost, 
and this cost is not amortized until a large enough number of points is reached. 
The parallelism only pays off when the problem reaches a large enough size. This
is also why the parallel point rates lag behind the serial point rate (which
remains approximately constant) before overtaking the serial point rate. Once 
the problem is large enough (10^5 - 10^7 points), the parallel implementations 
overtake the serial implementation in execution time and point rate. The parallel 
execution times (and rates) in this region are roughly half of the serial execution 
times, which we expect, since we've divided the work in half among two processes in 
the parallel schemes.