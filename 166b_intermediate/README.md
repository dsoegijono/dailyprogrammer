### [[6/14/2014] Challenge #166b [Intermediate] Prime Factor Trees](http://www.reddit.com/r/dailyprogrammer/comments/284uhh/6142014_challenge_166b_intermediate_prime_factor/)

Given a number, generate its factor tree. A prime factor tree is a tree that has a number's factor as its branches. Continue to "draw" these branches (divisions) until prime numbers are found (therefore can't be branched).

Example:

    60

60 can be divided by 4 to get 15, for example, therefore they can be used as branches:

       60
        |
     4--+--15

Then, do the same for each of those numbers, too:

        60
         |
      4--+--15
      |      |
    2-+-2  3-+-5
      
Once a prime number (such as the bottom row) is created, you can't factor any further, so you stop.

#### Challenge

##### Challenge Input

    1767150

##### Sample Challenge Output

There are a lot of different ways to display a factor tree for some numbers. Here are some examples.

               1767150          
                |               
       1309-----+-----1350      
         |             |        
      77-+--17    45---+---30   
      |            |        |   
     7+-11       9-+--5   6-+--5
                 |        |     
                3+-3     2+-3 
                
               1767150          
                   |            
           1350----+-----1309   
            |              |    
       45---+---30      77-+--17
       |         |      |       
     5-+-9     6-+--5  7+-11    
         |     |                
        3+-3  2+-3
        
#### Notes

If you're having trouble with the tree printing logic, that's fine - you can skip that if you want. Print it a different way that's easier to format.

### My Output
      2-x-3   3-x-3   5-x-5   7-x-11   17 
        6--x--9      25--x--77      17  
          54---x---1925         17   
            103950----x----17    
              1767150     

My first try was to just find the prime factors of the number. Once I got that, I built the tree upside down, multiplying the prime factors back to the original number. This isn't a solution to the challenge yet, and I'm still trying to figure that out.
