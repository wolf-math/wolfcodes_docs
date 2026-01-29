---
slug: diffie-hellman-key-exchange
title: "Diffie-Hellman Key Exchange"
authors: Aaron Wolf
sidebar_position: 1
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## History

The most advanced method of encryption during WWII (the enigma machine) was broken by a guy who built a computer (Alan Turing). 

In the decades following WWII the US was in a cold war with the USSR. Computers were being built in order to gain intelligence and monitor what the Soviets were doing. NORAD (part of the US and Canada's military complex) created the first networked computer system and they wanted secure communication so that no bad actors could eavesdrop on secret military communication.

## Diffie-hellman

In 1976 Whitfield Diffie and Martin Hellman developed a method of key exchange where two parties could share **public keys** for encryption and decryption but nobody else would be able to see any messages because each party would also have a **private keys**

The Diffie-Hellman key exchange was the first ever devised _asymmetric cipher_. This means that a secret message can be sent from one party to another without the need to share the keys.

:::note
The basics of this methodology are still used today in many forms of communication, including SSH. Never **EVER** share your private key with anybody!
:::

## How does it work conceptually?

Up until Diffie-Hellman all encryption was done with a _symmetric_ key exchange. This means that the sender and receiver had to share an agreed upon key before they can send messages to one another. But what if the 2 parties have never met? Or what if they're far away?

The solution is a public key exchange. This is called _asymmetric_ key exchange because each party has a different key. But how?

Each party has a private key and a public key. The private key is never shared. Both parties agree (publicly) on a prime modulus and a generator to the modulus. The prime modulus is just a large prime number and the generator is a number that when raised to the power off all numbers up to the prime number _p_ (1, 2, 3, ... , p-1 , p), the solution set will include all numbers up to _p_ (1, 2, 3, ... , p-1 , p). This allows for the same character to be encrypted to different values. 

It's confusing- I know.

But when the public keys are exchanged the individuals can calculate their private keys raised to the power of their partner's public key and everything unravels to decrypt itself!


## How does the math work?

The Diffie-Hellman key exchange algorithm is based on the difficulty of the discrete logarithm problem in modular arithmetic. The basic steps of the protocol involve:

1. Two parties agree on a large prime number _p_ and a base _g_, where _g_ is a primitive root modulo _p_. 

2. Each party selects a private key (a secret number), let's say _a_ and _b_, and  computes their respective public keys as $A = g^{a} mod(p)$ and $B = g^{b} mod(p)$.

3. They then exchange their public keys.

4. Each party raises the received public key to the power of their own private key to compute the shared secret: $s = B^{a} mod(p)$ and $s = A^{b} mod(p)$.

Due to the properties of modular exponentiation, both parties arrive at the same shared secret.

## Demonstration

This is a MarkDown version of a Jupyter Notebook that I created for this demonstration. Feel free to [clone the repository](https://github.com/wolf-math/encryption-demo) and play with the key exchange yourself.



### Helper functions

These are not the most performant functions but that's not their intention. They are here so that the user can gain an understanding of how the encryption takes place.

First we need a function that tells us if a number is prime or not. This is because our modulus must be a prime number


```python
# checks if number is prime or not

def is_prime(number):
    factors = []
    for i in range(2, int(number**0.5)+1):
        if (number/i)%1 == 0:
            factors.append(i)
            
    if len(factors) > 0:
        return False
    else:
        return True
```

Given a prime number $p$, the following function returns an array of all numbers that are **primitive roots** or **generators** of $p$. A primitive root is a number $a$ such that if you raise $a$ to all of the powers $(1, 2, 3, ... , p)$ the results will contain of the numbers $(1, 2, 3, ... , p)$, though not necessarily in order.


```python
# returns array of generators of a prime number

def calculate_generator(prime):
    if is_prime(prime) == False:
        return False

    generators = []
  
    for i in range(2, prime):
        results = []
        for j in range(2, prime):
            results.append(pow(i, j, prime))

        if len(set(results)) == len(results):
            generators.append(i)

    return generators
```

Given a private key (usually a random number), the public key is determined by the following arithmetic function. 

$$
public\_key = generator^{private\_key} (mod\ p)
$$


```python
# creates public key

def create_pub_key(generator, private_key, prime):
    # pow takes (base, exp, mod=None) 
    # is equivalent to base**exp % mod
    return pow(generator, private_key, prime)
```

_Encoding_ is **not** _encryption_. It simply converts the letter to its computer numerical value. Any computer can make this conversion, so it's not scrambled in any way. This function takes a string as an argument and returns an array of the encoded characters.


```python
# encode a string into an array of each character's numerical value

def encode_string(string):
    char_array = []
    for char in string:
        char_array.append(ord(char))
    return char_array
```

Decoding is the opposite of encoding. This function is the opposite of the previous one.


```python
# decode an array of numerical values to their corresponding character

def decode_string(arr):
    decoded_arr = []
    for i in arr:
        decoded_arr.append(chr(i))
    return "".join(decoded_arr)
```

Given a encoded array, a shared "super key", and a prime, we can encrypt the message. This is not technically part of the Diffie-Hellman process. We use the following mathematical function to encrypt each letter in the array, though others may be used.

$$
num + super\_key (mod\ p)
$$


```python
# encrypts message
 
def encrypt_message(super_key, message_array, prime):
    encrypted_array = []
    for num in message_array:
        encrypted_array.append(num + super_key % prime)
    return encrypted_array
```

Decrypting the message is the inverse function:

$$
num - super\_key (mod\ p)
$$


```python
# decrypts message

def decrypt_message(super_key, encrypted_array, prime):
    decrypted_message = []
    for num in encrypted_array:
        decrypted_message.append(num - super_key % prime)
    return decrypted_message
```

### Implementing Diffie-Hellman
Now that we have all of our helper functions we can implement Diffie-Hellman. Obviously, this would be done from two different machines if it was sent over the internet (i.e. SSH).

### Let's get 2 volunteers


```python
p1 = input("Person 1's name: ")
p2 = input("Person 2's name: ")
```

### Choose numbers

We need to do is choose a **publicly known prime number**, and a **generator** of that prime. In the video the prime was 17 and the generator was 3.


```python
prime = int(input("choose a shared prime number: "))

while is_prime(prime) == False:
    prime = int(input("that's not prime, try again: "))

gen = int(input(f"select a shared generator from the list {calculate_generator(prime)}: "))
```

Choose a **private key** then autogenerate the **public key**

$$
public\_key = g^{private\_key} (mod\ p)
$$


```python
p1private_key = int(input(f"{p1} select a private key: "))
p1public_key = create_pub_key(gen, p1private_key, prime)
print(f"{p1}'s public key: {p1public_key}")

p2private_key = int(input(f"{p2} select a private key: "))
p2public_key = create_pub_key(gen, p2private_key, prime)
print(f"{p2}'s public key: {p2public_key}")
```

### Review so far:

#### Numbers that are known to everyone


```python
print(f"prime number {prime}")
print(f"generator of {prime}: {gen}")
print(f"{p1}'s public key {p1public_key}")
print(f"{p2}'s public key {p2public_key}")
```

#### Numbers only known to their owners


```python
print(f"{p1}'s private key {p1private_key}")
print(f"{p2}'s private key {p2private_key}")
```

### The `super` key

The super key is the super-secret key that both parties calculate on their own but with different numbers. They should be equal otherwise this won't work. In the video the super key was 10


```python
super_key = pow(p2public_key, p1private_key, prime)
super_key2 = pow(p1public_key, p2private_key, prime)

if super_key != super_key2:
    print("Oops, something went wrong...")
    
print(f"super key: {super_key}")
```


```python
print(super_key)
```

### Sending a message

#### Step 1: Encode the message into the computer numeric values


```python
message = input(f"{p1}, what message do you want to send to {p2}? ")
message_array = encode_string(message)
print(message_array)
```

#### Step 2: Encrypt message


```python
encrypted = encrypt_message(super_key, message_array, prime)
print(encrypted)
```

#### Step 3: Decrypt message


```python
decrypted = decrypt_message(super_key2, encrypted, prime)
print(decode_string(decrypted))
```

## Next step

We learn how RSA encryption works!!!
