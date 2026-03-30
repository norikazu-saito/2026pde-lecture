# Initial data
def initial(x):
  #return np.sin(2.0*np.pi*x)
  return np.exp(-100*(x-0.5)**2)
  #return np.maximum(0.0, 1.0-16.0*(x-0.5)**2)
  
# Hamiltonian
def Hamil(p):
  return 0.5*p*p

# Setting parameters
N = 401
T = 1.0
mu = 1.0
num = 40

# Computing the Hamilton-Jacobi equation
x, tn, sol = hamiltonjacobi_lf(Hamil, initial, N, T, mu, num)

# Displaying figures
plot_solution(x, sol)

# Displaying an animation
anim = plot_animation(x, tn, sol)
# Saving the results as hj.gif (make sure that Google Drive is mounted)
anim.save('/content/drive/MyDrive/Colab Notebooks/fig/hj.gif', writer='pillow')
rc('animation', html='jshtml')
plt.close()
anim
