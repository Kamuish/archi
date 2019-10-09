.. _optimization:

The Optimization routine 
========================
The optimization process is one of the most important factors for achieving low noise on
the extracted light curves, since it allows us to tweak the mask size. The process is quite
simple, since it consists in running the algorithm with different masks sizes, and searching
the one that minimizes the CDPP. 

To speed up this process, it was implemented in a concurrent way, allowing to have
multiple factors being tested at once. If the CDPP is deemed invalid, i.e. if the mask went outside of the image region, then
we attribute an arbitrarily high noise level, such as 2e7, so it’s certain that any valid values
will have a far lower noise and thus a valid mask is chosen.


If any star has a mask size that lies within a tolerance range of
the maximum value, the search for the optimal size shall continue, now with a lower limit
of the previous maximum value and an upper limit of two times the previous maximum.
This repetition has a user-defined maximum number, but we found that limiting it to 5
times is enough to find the best sizes for all the stars, when considering background grids
smaller or equal to 1800 points. 

The design of the shape mask does not allow for partial increases
in the size. However, that’s not the case for the circle mask, whose radius can be increased
in fractions. So, for this mask, after finding the optimal value, a second optimization step
is launched, now searching the values within 1 unit from the optimal one, in steps of 0.1
units. We have found that gains from using smaller steps were not enough to justify the
increase in the computational cost.


