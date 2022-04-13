- **DATABASE** is a server where you can read and write data. It is the most critical part of system, iff it goes down,
  your whole system will go down.
- A lot of people takes databases for granted that they always provide persistence , meaning data will be there even
  though your system crashes or there is some network issue, although this is often true but not always which leads us
  to 2 fundamental properties of storage.

1. **DISK :** If database server writes to disk, data will be persistent even though our DB server goes down. (Consider
   it as saving files in your hard drive.)
2. **MEMORY :** In this case, once DB server is down, or we restart server, data will be gone (Consider it as key-value
   pair hash table.)

One question that you might ask is, hey Taslim why do we ever need to use memory as once server is down/restarted data
will be gone. Answer is simple,read and write operation in memory is way faster than disk. We want to make our system as
efficient, fast as possible and at the same time persistent even though server goes down. That is where lots of
techniques come into picture which we will discuss later in this series.

Storage is very complicated, in this section we have just covered very basic part of it and will cover advanced topics
in coming tutorials.
