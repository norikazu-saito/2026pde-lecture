# Lax--Friedrics scheme for the Hamilton--Jacobi equation
def hamiltonjacobi_lf(Hamil, initial, N, T, mu, num):
  # x-grids
  L = 1.0
  h = L/N
  xgrid = np.linspace(0.0, L, N)
  xtmp = xgrid[:-1].copy()

  # initial setteings
  tgrid = np.array([0.0])
  u = initial(xtmp)
  sol = np.copy(np.append(u,u[0]))

  # CFL condition
  uu = initial(xgrid)
  du = (uu[1:] - uu[:-1])/h
  pmax, abs_dH = find_maximum_dH(Hamil, du)

  # t-grids
  tau = mu*h/abs_dH
  lam = tau/h
  nmax = int(T/tau)
  step = int(max(1, nmax/num))

  # iteration
  tnow = 0.0
  for n in range(nmax):
    u = 0.5*(np.roll(u,1) + np.roll(u,-1)) - tau*Hamil(0.5*(np.roll(u,-1)-np.roll(u,1))/h)
    tnow = (n+1)*tau
    if (n+1)%step==0:
      sol=np.vstack((sol,np.append(u,u[0])))
      tgrid=np.append(tgrid, tnow)

  return xgrid, tgrid, sol
