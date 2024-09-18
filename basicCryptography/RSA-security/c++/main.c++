#include <bits/stdc++.h>
using namespace std;

// returns gcd of and b 
int gcd(int a, int h)
{
  int temp; 
  while(1) {
    temp = a % h; 
    if (temp == 0)
      return h; 
    a = h; 
    h = temp;
  }
}

// code to demonstrate RSA algorithm 
int main() 
{
  // two random prime numbers 
  double p = 3; 
  double q = 77; 

  // part 1 of public key 
  double n = p * q; 

  // finding other part of public key
  double encrypt = 2; 
  double phi = (p-1) * (q-1)
    while (encrypt < phi) {
      // encrypt must be co-prime to phi and smaller than phi 
      if (gcd(e, phi) == 1)
        break; 
      else 
        e++; 
    }
}
