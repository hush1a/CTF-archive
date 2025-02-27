### Simple Math \- 100 pts
**Reverse Engineering**   
Description:  
"Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation."

`Author: Haalloobim`

I viewed the code and it is a bytecode disassembly,  
Another file was the **output.txt** file, which contains numbers.  

Using AI,I was able to see the constructed python code that resembles the original decompiled one.  
I also inserted the numbers from the text files to the ‘flags’ array.

```python
def conv(s, l=(5,)):
    """Splits a string into chunks of length l."""
    return (s[i : i + l[0]] for i in range(0, len(s), l[0]))


# INSERT THE FLAG LIST FROM OUTPUT.TXT
flags = [
        927365724618649,
        855544946535839,
        1075456339888851,
        1051300489856216,
        854566738228717,
        862564607600557,
        1107196607637040,
        835104762026329,
        1108826984434051,
        843310935687105,
    ]


# list of numerical values
N = [
    412881107802, 397653008560, 378475773842, 412107467700, 410815948500,
    424198405792, 379554633200, 404975010927, 419449858501, 383875726561
]


# Reverse the list
NR = list(reversed(N))


# Ensure flag length is a multiple of 5
assert len(flags) % 5 == 0


# Process flag characters
for i, j, k in zip(conv(flags), N, NR):
    x = int.from_bytes(i.encode(), 'big')  # Convert chunk to integer
    y = (x + j) * 1337 ^ k - 871366131    # Apply transformation
    flags.append(y)


print(flags)
```

The code reads a flag from a file, processes it using a transformation involving numerical operations, and prints the final transformed values.  
Below i made a script that reconstructs the flag by reversing the techniques,

1. Reverse subtraction  
2. Reverse XOR  
3. Reverse multiplication and addition


```python
Then it is converted back to string, and the flag chunks are combined together to make the flag.

def decrypt_flag(flags, N):
    NR = list(reversed(N))  # Reversed list of N values
    original_flag = []


    for y, j, k in zip(flags, N, NR):
        y_prime = y + 871366131  # Reverse subtraction
        y_double_prime = y_prime ^ k  # Reverse XOR
        x = y_double_prime // 1337 - j  # Reverse multiplication and addition
        original_flag.append(x.to_bytes(5, 'big').decode())  # Convert back to string
   
    return ''.join(original_flag)  # Combine flag chunks


original_flag = decrypt_flag(flags, N)
print("Recovered Flag:", original_flag)
```
When the program is ran, the flag will be printed:

Flag: `ARA6{8yT3_c0d3_W1Th_51MPl3_m4th_15_345Y____R19ht?}`
