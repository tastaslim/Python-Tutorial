**Throughput** is amount of task a machine can perform in a given amount of time(Or number of bits transferred per
second/ number of HTTP calls per day).

- Measured in gbps, kbps, mbps etc.

---
Suppose an assembly line is manufacturing cars. Let’s consider the factory is able to produce around 100 cars per day.
So the Throughput of the line is Throughput ~ 100 cars/day.

## Misconceptions with Latency ##

Latency is defined as the time interval between making a request and beginning to see a result. It is measured in the
unit of time. Latency is always misunderstood with Throughput, and it is taken for granted that High throughput systems
should have low latency. However, this may not always be true. Consider the data processing in association with disks,
which tend to have large Throughput but fail to provide low latency.

Similarly, in networked connections, the latency increases with Throughput. With the increase in Throughput, more and
more packets will be there on a wire and contribute to increased latency. It is also possible to have systems with Low
Throughput and Low Latency also. Hence, the combination of Latency and Throughput is best chosen by considering the
system and business requirements.

---

Throughput depends on hardware which we are using, network traffic, accessibility etc. We can increase the number of
servers when there are too many requests to increase the throughput and properly manage the request so that no server is
over/under utilized.