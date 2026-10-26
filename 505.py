import sys


def solve():
  out = []
  for line in sys.stdin:
    line = line.strip()
    if not line:
      continue
    m = [[int(x) for x in r.split()] for r in line.split(",")]
    n, s = len(m), sum(m[0])
    ok = (
        all(len(r) == n for r in m)
        and all(sum(r) == s for r in m)
        and all(sum(m[r][c] for r in range(n)) == s for c in range(n))
        and sum(m[i][i] for i in range(n)) == s
        and sum(m[i][n - 1 - i] for i in range(n)) == s
    )
    out.append(str(ok))
  print("\n".join(out))


if __name__ == "__main__":
  solve()

