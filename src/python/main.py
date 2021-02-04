#!/usr/bin/python

def a(j, k):
  """
  Add two values
  """
  s = j + k
  return s

def m(w):
  """
  Multiplies a character by itself 3 times
  >>> m("h")
  hhh
  """
  t = 3
  a = w * t
  return a

def main():
  """
  Main Function
  """
  v = int(input("Enter a number: "))
  assert type(v) is int
  print(a(v))

main()
