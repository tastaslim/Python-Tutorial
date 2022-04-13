- **DATABASE** is a server where you can read and write data. It is the most critical part of system, iff it goes down,
  your whole system will go down.
- A lot of people takes databases for granted that they always provide persistence , meaning data will be there even
  though your system crashes or there is some network issue, although this is often true but not always which leads us
  to 2 fundamental properties of storage.

1. **DISK** If database server writes to disk, data will be persistence even though our db server goes down. (Consider
   it as saving files in your hard drive.)
2. **MEMORY** In this case, once db server is down, or we restart server, data will be gone (Consider it as key-value
   hash table.)

Once question that you might be thinking about is why do we ever need to use memory? Because reading data from and
writing data to memory is way faster than disk.

Storage is very complicated, in this section we have just covered very basic part of it and will cover advanced topics
in next tutorial.
