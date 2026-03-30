# Lax--Friedrics scheme for the nonlinear conservation law
def conservationlaw_lf(flux, initial, N, T, mu, num):
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
  smin, smax, abs_df = find_maximum(flux, u)

  # t-grids
  tau = mu*h/abs_df
  lam = tau/h
  nmax = int(T/tau)
  step = int(max(1, nmax/num))

  # iteration
  const = 0.5/lam
  n = 0
  tnow = n*tau
  for n in range(nmax):
    uflux = 0.5*(flux(u) + flux(np.roll(u,1))) - const * (u - np.roll(u,1))
    u = u - lam*(np.roll(uflux,-1) - uflux)
    tnow = (n+1)*tau
    if (n+1)%step==0:
      sol=np.vstack((sol,np.append(u,u[0])))
      tgrid=np.append(tgrid, tnow)

  return xgrid, tgrid, sol
