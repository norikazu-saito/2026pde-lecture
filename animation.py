# Creating animations
# Using the IPython.display module
def plot_animation(xgrid, tgrid, uvect):
  # Configuring plotting-related parameters
  umax = np.max(sol)
  umin = np.min(sol)
  xmax = np.max(xgrid)
  xmin = np.min(xgrid)
  ulength = umax - umin
  utop = umax + 0.1*ulength
  umax += 0.05*ulength
  umin -= 0.05*ulength
  xmid = (xmax+xmin)/2
  xlength = xmax - xmin
  xmax += 0.05*xlength
  xmin -= 0.05*xlength

  # Creating fig and ax objects
  fig, ax = plt.subplots()
  ims = []

  # t = 0
  n = 0
  im, = ax.plot(xgrid, uvect[n, :], color='#ff8c00')
  title = ax.text(xmid, utop, f'time={tgrid[n]:.4f}', ha='center', va='center', fontsize=15)
  ims.append([im, title])

  # t > 0
  for n in range(1, uvect.shape[0]):
    im, = ax.plot(xgrid, uvect[n, :], color='#00bfff')
    title = ax.text(xmid, utop, f'time={tgrid[n]:.4f}', ha='center', va='center', fontsize=15)
    ims.append([im, title])

  # Setting labels for each axis
  ax.set_xlabel(r"$x$", fontsize=15)
  ax.set_ylabel(r"$u$", fontsize=15)
  # Setting the range of the graph
  ax.set_xlim([xmin, xmax])
  ax.set_ylim([umin, umax])
  ax.grid(True)

  # Creating an animation by passing the fig object and ims to ArtistAnimation
  return animation.ArtistAnimation(fig, ims)
