#include <bits/stdc++.h>
using namespace std;

// returns gcd of and b
int gcd(int a, int h) 
{
  int temp;
  while (1) {
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
  double q = 7;

  // part 1 of public key
  double n = p * q;

  // finding part 2 of public key
  double encrypt = 2;
  double phi = (p - 1) * (q - 1);
  while (encrypt < phi) {
    // encrypt must be co-prime to phi and smaller than phi
    if (gcd(encrypt, phi) == 1)
      break;
    else
      encrypt++;
  }
  // private key
  // choosing decrypt such that is satisfies
  // decrypt*encrypt = 1 + k * totient
  int k = 2; // a constant value 
  double decrypt = (1 + (k * phi)) / encrypt;

  // message to be encrypted
  double msg = 12;
  printf("message data = %lf", msg);

  // encryption c = (msg ^ encrypt) % n
  double c = pow(msg, encrypt);
  c = fmod(c, n);
  printf("\nencrypted data = %lf", c);

  // decryption m = (c ^ d) % n
  double m = pow(c, decrypt);
  m = fmod(m, n);
  printf("\noriginal message sent = %lf", m);

  return 0;
}
