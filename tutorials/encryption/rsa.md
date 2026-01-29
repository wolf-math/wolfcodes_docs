---
slug: rsa
title: "RSA Encryption"
authors: Aaron Wolf
sidebar_position: 2
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## History and overview

RSA was invented by NORAD in the early 1970's but was deemed top secret. A few years later in 1977, Ron **R**ivest, Adi **S**hamir and Leonard **A**dleman independantly invented the exact same process for encryption and called it RSA. RSA is the most used software in the world to date and every internet user has used RSA at some point whether they knew it or not. 

<!-- truncate -->

It shares many mathematical similarities with Diffie-Hellman encryption, but it's conceptually a little different. Instead of thinking about public and private keys, RSA can be thought of as sending an unlocked padlock. It would be like someone who wants to receive a message sending an **unlocked** padlock to the sender who then locks his message and sends it back for decryption.

The problem RSA solves compared to Diffie-Hellman is that of key storage. When using Diffie-Hellman every key needs to be saved separately. This can be unwieldy for a large organizaion like a bank with many customers- the bank would need a different key for each customer. The solution to this is RSA! The bank can send the same lock, that they alone have keys for, out to many customers who can send encrypted messages back.

## Common uses of RSA encryption

Some common uses of RSA encryption are:

- **The Signal protocol**: An open source protocol for sending secure messages. Used by programs like Signal and WhatsApp. Though the signal protocol also uses a special version of Diffie-Hellman on top of RSA.
- **HTTPS**: The encrypted connection between a computer and a server from the World Wide Web uses SSL or TLS which is based on RSA.
- **VPN**: Like HTTPS, connecting to a VPN uses the SSL or TLS protocols.
- **Encrypted file systems**: Many files and file systems are encrypted using RSA.

## RSA encryption process

The entire process is based on Euler's theorem: $m^{φ(n)} \equiv 1 \mod n$, where $φ(n)$ is the product of two large prime numbers.

### Key generation
1. **Select two prime numbers**: Choose two large prime numbers, `p` and `q`.
2. **Compute the modulus `n`**: Calculate `n = p * q`. The value of `n` is used as the modulus for both the public and private keys.
3. **Calculate the totient (phi $φ$)**: Compute Euler's totient function, `φ(n) = (p-1) * (q-1)`.
4. **Choose the public exponent `e`**: Select an integer `e` such that `1 < e < φ(n)` and `e` is coprime with `φ(n)`. Often, `e = 65537`.
5. **Determine the private exponent `d`**: Calculate `d` as the _modular multiplicative_ inverse of `e` modulo `φ(n)`.

### Encryption process
1. **Public key**: The public key consists of the modulus `n` and the public exponent `e`.
2. **Encrypting a message**: Convert the message into an integer `m` (e.g., via ASCII). Then, compute the ciphertext `c` using $c ≡ m^e (mod n)$.

### Decryption process
1. **Private key**: The private key is made of the modulus `n` and the private exponent `d`.
2. **Decrypting a message**: Decrypt the message by computing $m ≡ c^{d} (mod \ n)$ using the private key.

### Security
- RSA's security relies on the difficulty of factoring the product of two large prime numbers.
- The security improves with larger key sizes but at the cost of slower encryption and decryption.

## Let's get coding: helper functions

These functions are meant for demonstration, not performance. This is just to show how the process of RSA, but this would never be used in production. In modern applications this process is completely automated. 

```python
# finds factors and determines if prime.

def factors(number):
    number = int(number)
    factors = set()

    # check for divisibility by 2 first to handle even numbers quickly
    if number % 2 == 0:
        factors.update({2, number // 2})

    # check for odd divisors only, up to the square root of the number
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            factors.update({i, number // i})

    # add 1 and the number itself to the factors
    factors.update({1, number})

    # a prime number has exactly two factors: 1 and itself
    return {'factors': factors, 'is_prime': len(factors) == 2}

    
    
# determines greatest common divisor of 2 numbers

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a



# encode a string into an array of each character's numerical value

def encode_string(string):
    char_array = []
    for char in string:
        char_array.append(ord(char))
    return char_array



# decode an array of numerical values to their corresponding character

def decode_string(arr):
    decoded_arr = []
    for i in arr:
        decoded_arr.append(chr(i))
    return "".join(decoded_arr)



# Calculate if numbers are co-prime (they have no common factors except 1)

def are_coprime(number1, number2):
    number1_factors = factors(number1)['factors']
    number2_factors = factors(number2)['factors']
    
    common_factors = number1_factors.intersection(number2_factors)
    
    # if the intersection of common factors is only 1 return True
    return common_factors == {1}

```

## Encryption functions

### Selecting the public key

$e$ should be an integer that is not only greater than 1 but also less than $φ(n)$, where $n = pq$ (the product of two distinct prime numbers $p$ and $q$).

$e$ and $φ(n)$ should be coprime, meaning they should have no common factors other than 1. This ensures that $e$ has a multiplicative inverse $mod φ(n)$.

The private exponent `d` is the modular multiplicative inverse of `e modulo ϕ(n)`. 
This means `d` is the number that satisfies the equation 
$d × e ≡ 1 \ modϕ(n)$.


```python
# calulate phi (φ) - the totient

def calculate_phi(p, q):
    if factors(p)['is_prime'] and factors(q)['is_prime']:
        return (p - 1) * (q - 1)
    
    raise ValueError('Not prime numbers')



# calculate e - the public exponent

def find_suitable_e(totient):
    # Start with 65537 - A common value for `e` in RSA
    e = 65537

    # Check if e is less than totient and coprime with the totient
    # If not, decrement by 2 (to keep e as an odd number) and check again
    while e >= totient or not are_coprime(e, totient):
        e -= 2
        if e <= 2:
            raise ValueError("Could not find an appropriate 'e' value.")

    return e


# encrypts each letter of the message with the exponent and modulus
def encrypt(message, e, n):
    if isinstance(message, list):
        encrypted_list = []
        for i in message:
            encrypted_list.append(pow(i, e, n))
        return encrypted_list
    else:
        return []
    
    
    
# decrypts each letter of the message given d - the private key - and n - the modulus

def decrypt(message, d, n):
    decrypted = []
    for i in message:
        decrypted.append(pow(i, d, n))
        
    return decrypted

    
    
# calculate d: the private key
def calculate_d(phi_n, e):
    return pow(e, -1, phi_n)

```

## Watch RSA in action

```python
# alice picks 2 prime numbers of similar size to compute `n`

while True:
    p1 = int(input('Pick your first prime: '))
    p2 = int(input('Pick your second prime: '))
    
    p1_is_prime = factors(p1)['is_prime']
    p2_is_prime = factors(p2)['is_prime']
    
    if p1_is_prime and p2_is_prime:
        print(f"\nAlice's primes are {p1} and {p2}")
        break
    elif not p1_is_prime and not p2_is_prime:
        print(f'{p1} and {p2} are both not prime')
    elif not p1_is_prime:
        print(f'{p1} is not prime.')
    elif not p2_is_prime:
        print(f'{p2} is not prime.')
        
        

# calculate n as the product of p1 and p2

n = p1 * p2

print(f"Alice's n value is {p1} x {p2} = {n}")



# calculate the totient - φ(n)

totient = calculate_phi(p1, p2)

print(f'φ(n) = ({p1} - 1) x ({p2} - 1) = {totient}')



# calculate exponent e, such that it is odd and coprime with φ(n)

e = exponent(totient)

print(f'The exponent value is {e}')



# calculate the private key `d`. Alice keeps this as her secret key.

d = calculate_d(totient, e)
print(f"Alice's private decryption key is {d}")
```


## Alice sends `n` and `e`. Bob uses these numbers to encrypt

Alice sends to Bob her values for `n` and `e`. This is like sending an open lock that Bob will use to lock up his message. He does this by calculating $m^{e} mod(n)$. Where `m` is the numerical value of his message.


```python
# Bob's message to Alice
message = input('Type a message to send: ')

encoded_message = encode_string(message)
print(f'Encoded but not encrypted message is:\n{encoded_message}\n')

encrypted_message = encrypt(encoded_message, e, n)
print(f'Encoded and encrypted message is:\n {encrypted_message}')
```

## Send the encrypted message

`encrypted_message` can now be sent from Bob to Alice without an eavesdropper (Eve) making any sense of the message. In practice this only works when large values of `p` and `q` are used, otherwise computers can still quite easily brute force the encryption.

## Alice uses her private key `d` to decrypt the message

Since `d` is the multiplicative inverse of `e` in respect to `φ(n)`, decrypting the message is easy. Each letter is decrypted with the function $i^{d} mod (n)$, where `i` is the encrypted numerical value of the letter, `d` is our private key, and `n` is the product of our two primes.

```python
# Alice decrypts the message using `d`

decrypted_message = decrypt(encrypted_message, d, n)

print(f"The decrypted encoded message is the same as above\n{encoded_message} = {decrypted_message}\n")


decoded_message = decode_string(decrypted_message)
print(f"The plain text value is: {decoded_message}")
```
