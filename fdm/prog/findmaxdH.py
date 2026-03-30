def find_maximum_dH(HH, dinit):
  p1 = np.max(np.abs(dinit))
  Np = 1000
  xp = np.linspace(-p1, p1, Np)
  yp = HH(xp)
  dHp = (yp[1:] - yp[:-1])*Np/(2*p1)
  return p1, np.max(np.abs(dHp))
