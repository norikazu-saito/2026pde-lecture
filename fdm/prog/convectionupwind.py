# Upwind difference scheme for the linear concevtion equation
def linear_convection_upwind(c, initial, N, T, mu, num):
  L = 1.0
  h = L/N
  tau = mu*h/np.abs(c)
  nmax = int(T/tau)
  step = int(max(1, nmax/num))
  lam = tau/h
  theta = 1 if c >= 0 else 0

  xgrid = np.linspace(0.0, L, N)
  xtmp = np.copy(xgrid[0:N-1])
  tgrid = np.array([0.0])
  u = initial(xtmp)
  sol = np.copy(np.append(u,u[0]))

  for n in range(nmax):
    p = 1.0 - theta*c*lam + (1.0 - theta)*c*lam
    q = theta*c*lam
    r = (1.0 - theta)*c*lam
    u = p*u + q*np.roll(u, 1) - r*np.roll(u, -1)
    tnow = (n+1)*tau
    if (n+1)%step==0:
      sol=np.vstack((sol,np.append(u,u[0])))
      tgrid=np.append(tgrid, tnow)

  return xgrid, tgrid, sol
