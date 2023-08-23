# What Is SSH: Understanding Encryption, Ports and Connection #

- SSH, or **Secure Shell** Protocol, is a remote administration protocol that allows users to access, control, and
  modify their remote servers over the internet.

- SSH service was created as a secure replacement for the unencrypted Telnet and uses cryptographic techniques to ensure
  that all communication to and from the remote server happens in an encrypted manner. It provides a mechanism for
  authenticating a remote user, transferring inputs from the client to the host, and relaying the output back to the
  client.
- The SSH command consists of below distinct parts:
    1. user:Account which you want to access
    2. host: computer/server which you want to access (Provide IP Address or Domain name)
    3. Private key if password authentication is not enabled
  ```bash
  ssh {user}@{host} # given that password policy is enabled
  ssh -i your_private-key.pem {user}@{host} # If password policy is not enabled then key is required
  ```

## Understanding Different Encryption Techniques ##

- The significant advantage offered by SSH over telnet is the use of encryption to ensure a secure transfer of
  information between the host and the client. There are three different encryption technologies used by SSH:
    1. Symmetrical encryption
    2. Asymmetrical encryption
    3. Hashing

---

## Symmetrical Encryption ##

- Symmetric encryption is a form of encryption where a secret key is used for both encryption and decryption of a
  message by both the client and the host. Effectively, anyone possessing the key can decrypt the message being
  transferred.
- Symmetrical encryption is often called **shared key** or **shared secret** encryption. There is usually only one key
  that is used, or sometimes a pair of keys, where one key can easily be calculated using the other key.
- Symmetric keys are used to encrypt the entire communication during an SSH session. Both the client and the server
  derive the secret key using an agreed method, and the resultant key is never disclosed to any third party.
- Symmetric key is created using **key exchange algorithm** such as **AES (Advanced Encryption Standard)**, **CAST128**,
  **Blowfish**.

## Asymmetrical Encryption ##

- Unlike symmetrical encryption, asymmetrical encryption uses two separate keys for encryption and decryption. These two
  keys are known as the public key and the private key. Together, both these keys form a public-private key pair.
- A public key can be used by any individual to encrypt a message and can only be decrypted by the recipient who
  possesses their particular private key, and vice versa. These consist of extensive and seemingly random combinations
  of numbers and symbols, however, both public and private keys are paired using complex mathematical algorithms(**RSA
  Algorithm**).
- Note that both encryption and decryption mechanisms are automatic processes – you don’t need to do anything manually.

### Symmetrical Encryption Pros and Cons  ###

**Pros**

- Fast
- Efficient for large Data

**Cons**

- Hard to share the key(as key is same both client and server side and while sharing any hacker can still the key
  information and access your data).

### ASymmetrical Encryption Pros and Cons  ###

**Pros**

- Efficient for small Data
- **Security**: Without both keys, a hacker can only access useless data.
- **Transparency**: Public keys can be openly distributed, as losing them will not devolve into a security risk.

**Cons**

- **Speed** : Systems need time for decryption. Users sending plenty of bulk files will have a long wait.
- **Vulnerabilities**: Lose a private key, and anyone who finds it can read all messages, even if they're private. A
  lost key can result in a man-in-the-middle attack too.
- **Loss**: If you lose your private key, you won't be able to decrypt messages sent to you.
- **Long-term sustainability**: In the future, quantum computing will break most asymmetric and symmetric approaches.

---

If you see, the problem with symmetrical encryption is the threat to expose the key to some malicious user while sharing
the key info with server but at the same time it is fast and efficient for large data.
In real world, we use combination of best of both encryption algorithms.

---

- We use **ASymmetrical Encryption** to initiate the communication b/w two parties and once communication is initiated
  successfully, we start using **Symmetric Encryption** for data transfer.
- **ASymmetrical Encryption** is used during the key exchange algorithm of symmetric encryption. Before initiating a
  secured connection, both parties generate temporary public-private key pairs and share their respective private keys
  to produce the shared secret key.

# Hashing #

One-way hashing is another form of cryptography used in Secure Shell Connections. One-way-hash functions differ from the
above two forms of encryption in the sense that they are never meant to be decrypted. They generate a unique value of a
fixed length for each input that shows no clear trend which can be exploited. This makes them practically impossible to
reverse.

- It is easy to generate a cryptographic hash from a given input, but impossible to generate the input from the hash.
  This means that if a client holds the correct input, they can generate the cryptographic hash and compare its value to
  verify whether they possess the correct input.
- SSH uses hashes to verify the authenticity of messages. This is done using HMACs, or Hash-based Message Authentication
  Codes. This ensures that the command received is not tampered with in any way.
- While the symmetrical encryption algorithm is being selected, a suitable message authentication algorithm is also
  selected. This works in a similar way to how the cipher is selected, as explained in the symmetric encryption section.
- Each message that is transmitted must contain a MAC, which is calculated using the symmetric key, packet sequence
  number, and the message contents. It is sent outside the symmetrically encrypted data as the concluding section of the
  communication packet.

## How Does SSH Work With These Encryption Techniques ##

- The way SSH works is by making use of a client-server model to allow for authentication of two remote systems and
  encryption of the data that passes between them.
- The client must begin the SSH connection by initiating the TCP handshake with the server, ensuring a secured symmetric
  connection, verifying whether the identity displayed by the server match previous records (typically recorded in an
  RSA key store file), and presenting the required user credentials to authenticate the connection.
- SSH operates on TCP port 22 by default (though SSH port can be changed if needed). The host (server) listens on port
  22 (or any other SSH assigned port) for incoming connections. It organizes the secure connection by authenticating the
  client and opening the correct shell environment if the verification is successful.

## Session Encryption Negotiation ##

- When a client tries to connect to the server via TCP, the server presents the encryption protocols and respective
  versions that it supports. If the client has a similar matching pair of a protocol and version, an agreement is
  reached and the connection is started with the accepted protocol. The server also uses an asymmetric public key which
  the client can use to verify the authenticity of the host.
- Once this is established, the two parties use what is known as a **Diffie-Hellman Key Exchange Algorithm** to create a
  symmetrical key. This algorithm allows both the client and the server to arrive at a shared encryption key which will
  be used henceforth to encrypt the entire communication session.

#### Here is how the algorithm works at a very basic level: ####

- Both the client and the server agree on a very large prime number, which of course does not have any factor in common.
  This prime number value is also known as the seed value.
- Next, the two parties agree on a common encryption mechanism to generate another set of values by manipulating the
  seed values in a specific algorithmic manner. These mechanisms, also known as encryption generators, perform large
  operations on the seed. An example of such a generator is **AES (Advanced Encryption Standard)**.
- Both the parties independently generate another prime number. This is used as a secret private key for the
  interaction.
- This newly generated private key, with the shared number and encryption algorithm (e.g. AES), is used to compute a
  public key which is distributed to the other computer.
- The parties then use their personal private key, the other machine’s shared public key and the original prime number
  to create a final shared key. This key is independently computed by both computers but will create the same encryption
  key on both sides.
- Now that both sides have a shared key, they can symmetrically encrypt the entire SSH session. The same key can be used
  to encrypt and decrypt messages (read: section on symmetrical encryption).

Now that the secured symmetrically encrypted session has been established, the user must be authenticated.

## Authenticating the User ##

- The final stage before the user is granted SSH access to the server is authenticating his/her credentials. For this,
  most SSH users use a password. The user is asked to enter the username, followed by the password.
- These credentials securely pass through the symmetrically encrypted tunnel, so there is no chance of them being
  captured by a third party.
- **Although passwords are encrypted, it is still not recommended to use passwords for secure connections. This is
  because many bots can simply brute force easy or default passwords and gain secure shell access to your account.
  Instead, the recommended alternative is SSH Key Pairs**.
- These are a set of asymmetric keys used to authenticate the user without the need of inputting any password.

---

If you’re wondering how long it takes for a computer to calculate a hash and authenticate a user, well, it happens in
less than a second. In fact, the maximum amount of time is spent in transferring data across the Internet