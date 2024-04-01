MAX = 100_007
MOD = 1_000_000_007

def is_good(n):
  if n == 1:
    return True

  binary_decimals = [i for i in range(2, MAX) if all(digit <= str(1) for digit in str(i))]  # Efficiently generate binary decimals
  for divisor in binary_decimals:
    if n % divisor == 0 and is_good(n // divisor):
      return True
  return False

def solve():
  n = int(input())
  print("YES" if is_good(n) else "NO")

if __name__ == "__main__":
  t = int(input())
  for _ in range(t):
    solve()