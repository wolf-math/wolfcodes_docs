---
slug: hashes
title: "Hashes"
authors: Aaron Wolf
sidebar_position: 3
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## Introduction

Hashing is a one way function that's used in encryption scenarios where the goal is secure storage, data integrity, and verification. The original use that led to the creation of hashing functions was digital signatures. It's basically a function that creates a summary of the whole, but the whole cannot be extrapolated from the hash. 

Any website you've logged into with a password should be storing your password as a hash, meaning the maintainers of the website couldn't extrapolate your password even if they wanted to. It's just saved as a hash which is represented by a random string. When you log into the website your password is sent securely (over `HTTPS`) from your computer to the server where it is hashed and compared against the server's hash of the password. If they match, you get authenticated, if not, try again.

Hashing can also work to verify data. If you've ever downloaded a Linux `.iso` and the instructions tell you to run `sha256sum <linux_distro_of_your_choice>.iso`, the output will be a hash and it should match what the Linux website says, otherwise someone may have tampered with it or it could be corrupt. 

You can clone my [encryption demo repo](https://github.com/wolf-math/encryption-demo) and run the code from this article on your own machine.

## Hashing algorithms

There are many different hashing algorithms but most of them follow the same basic process. It is a mathematical function that takes a particular input (a password for instance) and converts it through some mathematical means into a digest, also sometimes referred to as tags or just hashes. 

There are a few commonalities that good hashing algorithms share:

1. **It's deterministic**: This means that an input will always result in the same output.
2. **Fixed length**: The input can be as large as the user wants, however, the output will always be a fixed length. For instance `sah256sum` always produces a hash that is 256 bits. 
3. **It's fast**, but also not too fast: It needs to be fast for performance, but if it's too fast that indicates that it's not performing enough computation to create a _good_ hash.
4. **The avalanche principal**: If even a single bit of data has changed, no matter where in the file, the resulting hash will be drastically different.
5. **Collision resistant**: Two inputs never create the same output. While there are an incredible number of possible hashes out there, there are still only a finite number of them. Therefore in the natural course of using a hash function it's possible that two files can create the same hash. However the function should be collision resistant enough that intentionally creating two files that generate the same hash is unlikely and virtually impossible. If this was possible, forging documents would be easy. Due to their extensive use and known collision resistance issues, there are a few hashing algorithms that are considered broken including SHA1 and MD5.

## SHA-1 in action

SHA stands for **S**ecure **H**ash **A**lgorithm, even though, ironically, it's no longer secure. However, it takes any size input and returns a 160-bit (20-byte) fixed-length hash value.

1. **Padding the message:**
The input message is padded so that its total length (in bits) is congruent to 448 mod 512.
Padding starts with a single 1 bit, followed by enough 0 bits to reach that length, and finally appends a 64-bit representation of the original message length.
2. **Initialization:**
SHA-1 begins with five 32-bit initial hash values (denoted H₀ through H₄).
3. **Message schedule preparation:**
Each 512-bit block of the padded message is divided into sixteen 32-bit words (W[0] through W[15]).
4. **Word expansion:**
These sixteen words are expanded into eighty 32-bit words (W[0] through W[79]) using bitwise operations (XORs and circular left shifts).
5. **Main loop (80 rounds):**
The algorithm runs 80 iterations per block, applying a compression function that mixes the data with nonlinear functions (AND, OR, XOR), constants, and circular shifts.
6. **Hash value update:**
After processing each block, the five working variables are added to the existing hash values. For the first block, the initial values are used; for subsequent blocks, the updated values from the previous block are carried forward.
7. **Final digest:**
When all blocks are processed, the five 32-bit words are concatenated to form the 160-bit hash — the final SHA-1 digest.

## Python for SHA-1

Let's write some Python to create a SHA-1 hash. **Note** that as stated above SHA-1 is no longer considered safe. **Don't use it in production!!!** 

Using the hashlib library, it's easy to generate a hash from a number of different algorithms. Feel free to try them all. Creating a hash function is beyond the scope of this write up.


```python
import hashlib

def sha1_hash(input_string):
    # Create a SHA-1 hash object
    hash_object = hashlib.sha1()

    hash_object.update(input_string.encode())

    # Get the hexadecimal representation of the hash
    hex_digest = hash_object.hexdigest()

    return hex_digest

```


```python
input_string = input('Enter a string to hash: ')
result = sha1_hash(input_string)

print(f"The SHA-1 hash of '{input_string}' is: {result}")

```