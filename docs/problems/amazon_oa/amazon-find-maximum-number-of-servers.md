# [Get Max Servers](https://www.fastprep.io/problems/amazon-find-maximum-number-of-servers)

**Medium** | **NN minutes** | **Array, Sorting, Greedy**

$23

## Examples

### Example 1

**Input:** `powers = [4, 3, 5, 1, 2, 2, 1]`

**Output:** `5`

**Explanation:** Source update (July 2, 2026) ᕙ( •̀ ᗜ •́ )ᕗ : I found an official source image that includes the example illustration.Example source illustration
    
      

  

  
  
  
  
  

  4

      

  

  
  
  
  
  

  3

      

  

  
  
  
  
  

  5

      
        

  

  
  
  
  
  

  1


  

  
  
  
  
  

  2


  

  
  
  
  
  

  2


  

  
  
  
  
  

  1

      
    
    
      selected subsequence
      Highlighted values form [3, 1, 2, 2, 1].
    
  


Consider powers = [4, 3, 5, 1, 2, 2, 1].The subsequence [3, 1, 2, 2, 1] can be selected (5 servers) and rearranged to [2, 1, 1, 2, 3]. Checking circular adjacency: abs(2-1)=1, abs(1-1)=0, abs(1-2)=1, abs(2-3)=1, and (circular) abs(3-2)=1, all of which are <= 1.No valid candidate of size greater than 5 exists, so the maximum number of servers the client can buy is 5.

## Constraints

- `1 <= n <= 2 * 10^50 <= powers[i] <= 10^9`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
