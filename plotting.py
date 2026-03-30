# Plotting figures. Overlaying multiple graphs in a single figure
def plot_solution(xgrid, uvect):
  # Setting parameters related to plotting
  umax = np.max(sol)
  umin = np.min(sol)
  ulength = umax - umin
  umax += 0.05 * ulength
  umin -= 0.05 * ulength
  # t = 0
  plt.plot(xgrid,uvect[0,:],color='#ff8c00')
  # t > 0
  for n in range(1,uvect.shape[0]):
    plt.plot(xgrid,uvect[n,:],color='#00bfff')

  plt.xlabel('x')
  plt.ylabel('u')
  plt.ylim(umin, umax)
  plt.grid('on')
  plt.show()
