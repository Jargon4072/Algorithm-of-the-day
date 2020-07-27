# Problems:
## Total 7 problems to be done in 120 mins.

### Q1: given a list l=[1,2,3,'a',None,(),[]], What will be the output of len(l)?

### Q2: What will be output of the following program?

```
ANIMAL = 'Tiger'

module Foo
    ANIMAL = 'Python'
    class Bar
        def value1
            print ANIMAL, " "
        end
    end
end
class Foo::Bar
    def value2
        print ANIMAL, " "
    end
end

Foo::Bar.new.value1
Foo::Bar.new.value2

```

### Q3: A quality agent is responsible for inspecting samples of the finished products in the production line. Each sample contains defective and non defective products represented by 1 and 0 respectively. After placing the product samples sequentially in a two-dimensional square matrix of product samples, determine the size of the largest square area of defective products

Example:
```

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 2
```

### Q4: Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
```

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.
```

##### Example 1:

Input: n = 1

Output: 5

Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

##### Example 2:

Input: n = 2

Output: 10

Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".


### Q5: Given a range [L, R] and an integer N, we need to find two integers in this range such that their XOR is maximum among all possible choices of two integers and is not more than N. More Formally, given [L, R], find S =max (A ^ B) where L <= A, B and S<=N.

##### Example 1:

Input:
8 20 15

Output:

15

### Q6: given a list, reverse it without using any inbuilt libraries. Use indexing and traversing method.

### Q7: Multiple choice output problem related to reversing a list.

