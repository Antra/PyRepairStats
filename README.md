# PyRepairStats
Assignment from my Brother's maths/stats course on KU:

## Simulation task
In a workshop they replace spareparts on cars.
We assume that:
- the cars going to the workshop can always be repaired by replacing exactly one sparepart
- that there are only two possible spareparts to replace

There is a closeby stock of spareparts.
This sparepart stock contains precisely 10 parts of each type.
Nobody thinks about restocking, before they run out of spareparts.
When they run out of spareparts, they send the youngest apprentice to the remote stock to refill - he of course also needs to restock both types of parts.
He needs to fetch 11 of the type that is needed right now (1 for the repair, and 10 for the stock).
But how many does he need to fetch of the other?

Assume that the error rate is the same for both parts. What is the probability that he needs to fetch k = 0, 1, 2, ..., 10?
Assume that the error rate for one part is p=0.3 and for the other 1-p. What is the probability that he needs to fetch k = 0, 1, 2, ..., 10?