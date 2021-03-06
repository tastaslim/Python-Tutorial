## Protocols ##

[Protocols](https://www.cloudflare.com/en-in/learning/network-layer/what-is-a-protocol/)

[HTTP status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

# What is a network protocol? #

In networking, a protocol is a set of rules for formatting and processing data. Network protocols are like a common
language for computers. The computers within a network may use vastly different software and hardware; however, the use
of protocols enables them to communicate with each other regardless.

Standardized protocols are like a common language that computers can use, similar to how two people from different parts
of the world may not understand each other's native languages, but they can communicate using a shared third language.
If one computer uses the Internet Protocol (IP) and a second computer does as well, they will be able to communicate —
just as the United Nations relies on its 6 official languages to communicate amongst representatives from all over the
globe. But if one computer uses IP and the other does not know this protocol, they will be unable to communicate.

On the Internet, there are different protocols for different types of processes. Protocols are often discussed in terms
of which OSI model layer they belong to.

---

We will discuss **IP**, **TCP** and **HTTP** in this tutorial.

1. **IP(Internet Protocol) :** Modern internet works on this Protocol, data transfer happens over this protocol. Data
   chunk is send in the form of IP packets which has 2 parts (Header(between 20-60 byte), data).

- **Header:** It contains metadata about IP packet(Like Source IP address, Destination Ip address, Total length of IP
  packet, Version(IPv4/IPv6), TTL (Time to leave) etc.) so that we can transfer data from source to destination.
- **data:** Actual data chunk which needs to be transferred.

Header | Data
_______|____________________________________________________  ==> IP Packet (2^16 byte max)

But problem is that IP packets are limited in size (MAX: 2^16 bytes ~=~ 0.065 mb), meaning our data is not going to fit
in a single packet (Say you are sending an email with some attachment), hence we use multiple IP packets. But how do we
guarantee that some packets are not lost, or they are received in the same order as sent. (Because you want your data to
be structured. Imagine you are watching YouTube video and after 8:30 min, you receive content of 12:30 min, that would
be horrible, so serialization of data is important). To solve this problem, we have **TCP(Transmission Control
Protocol)**

2. **TCP(Transmission Control Protocol) :** It is built on top of IP. It makes sure IP packets are sent in ordered,
   structured way, if any packet is lost, we will have information of that, and we can resend it. All of these
   operations happens in an error free way.

Header | TCP Header | Data
_______|____________|_________________________________________  ===> IP Packet(2^16 byte Max)

**TCP Header :** It contains information about ordering of packets. So what happens is before sending data to any
destination machine, source machine first establishes a TCP connection  (for a TTL period) with the destination (==>This
is called handshake). Once the connection is established, data can be transferred.

- Sender or receiver can close or time out the connection based on requirements.
- Although TCP is a powerful wrapper on top of IP and solves most of the problems, but It really lacks the more robust
  kind of framework which Software engineers can use to define meaningful and easy to use communication channel between
  client and server to transfer data. That is where **HTTP** comes into picture. Because with TCP all you are sending is
  arbitrary data and their order.

3. **HTTP(Hyper Text Transfer Protocol) :** It is a layer on top of TCP which introduces a higher level abstraction over
   TCP called request-response paradigm. With HTTP now we don't need to care about IP packets, TCP blah blah blah, we
   are just concerned about request and response using few predefined HTTP methods. You just provide route, method name,
   required headers and request body required to ask information from server.

```javascript
const httpRequest = {
    Headers: {
        host: 'localhost:5050',
        'user-agent': 'curl/7.79.1',
        accept: '*/*',
        'content-type': 'application/json',
        'content-length': '17'
    },
    Method: POST,
    body: {
        id: 1
    }
}

// Use this:  curl --header {content-type: application/json} http://localhost:5050/hello --data '{ "id": 1, "name": "Taslim", "age": 22, "address": "NPP" }'
const httpResponse = "Depends: In which format you are sending data and what content"
// For example: above request will give below response (See practice/server.js file)
const httpResponseExample = {
    body: {
        "id": 1,
        "name": "Taslim",
        "age": 22,
        "address": "NPP"
    },
    message: "Success fetched data for userId : 1"
}
```

- As a software developer, you will mostly be concerned about HTTP, you will be working with it only.

---
For more info on IP header: [IP header](https://www.guru99.com/ip-header.html)

## Port ## 

- HTTP works on port **80** by default.
- HTTPS works on port **443** by default.
- SSH works on port **22** by default.
- Port numbers **21** and **20** are used for FTP. Port 21 is used to establish the connection between the 2 computers (
  or hosts) and port 20 to transfer data (via the Data channel).

## HTTP Methods ## 

- GET : It is used to typically retrieve data from a server. (Status code : 200)
- POST : It is used to typically send data to a server. (Status code : 201 generally)
- PATCH : It is used to typically update data on a server.(Status code : 202,204 generally)
- PUT : It is used to typically replace data on a server. Status code : 202,204 generally)
- DELETE : It is used to typically delete data from a server. (Status code : 204 generally)

## HTTP Headers ##

- Content-Type : It is used to specify the type of data being sent to the server.
- Accept : It is used to specify the type of data being sent to the server.
- Custom headers
- cache-control : It is used to specify the caching policy of the server.
- content-length : It is used to specify the length of the data being sent to the server.
- content-encoding : It is used to specify the encoding of the data being sent to the server.

## Netcat ## 

Netcat (or nc) is a command-line utility that reads and writes data across network connections, using the TCP or UDP
protocols. It is one of the most powerful tools in the network and system administrators arsenal, and it as considered
as a Swiss army knife of networking tools.

Netcat is cross-platform, and it is available for Linux, macOS, Windows, and BSD. You can use Netcat to debug and
monitor network connections, scan for open ports, transfer data, as a proxy, and more.

**Note** One cool thing which you can do is, open two terminal windows and run

1. **nc -l 8081** in one window
2. **nc 127.0.0.1 8081** in other window

[Netcat Tutorial](https://linuxize.com/post/netcat-nc-command-with-examples/)

Now anything which you type in 2nd window will be visible in 1st window (Meaning we are transferring data over TCP/UDP
network protocol on port 8081)