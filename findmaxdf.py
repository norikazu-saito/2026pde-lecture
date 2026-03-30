def find_maximum(ff, init):
  s0 = np.min(init)
  s1 = np.max(init)
  Ns = 1000
  xs = np.linspace(s0, s1, Ns)
  ys = ff(xs)
  dfs = (ys[1:] - ys[:-1])*Ns/(s1-s0)
  return s0, s1, np.max(np.abs(dfs))
