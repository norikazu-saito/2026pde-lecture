# Initial data
def initial1(x):
  return 0.2*np.sin(2*np.pi*x) + 1.2

# Flux function
def flux1(s):
  return 0.5*s*s

# Setting parameters
N = 201
T = 2
mu = 1
num = 40

# Computing the nonlinear conservation law
x, tn, sol = conservationlaw_lf(flux1, initial1, N, T, mu, num)

# Displaying figures
plot_solution(x, sol)

# Displaying an animation
anim = plot_animation(x, tn, sol)
# Saving the results as ncl.gif (make sure that Google Drive is mounted)
anim.save('/content/drive/MyDrive/Colab Notebooks/fig/ncl.gif', writer='pillow')
rc('animation', html='jshtml')
plt.close()
anim
