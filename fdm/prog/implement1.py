def initial1(x):
  return np.sin(4*np.pi*x)

def initial2(x):
  return  np.maximum(0.0, np.minimum(2.0*x-0.5, 1.5-2.0*x))

# Setting parameters
c = -1.0
N = 51
T = 1.0
mu = 1
num = 40

# Computing the linear convection equation
x, tn, sol = linear_convection_central(c, initial1, N, T, mu, num)
#x, tn, sol = linear_convection_upwind(c, initial1, N, T, mu, num)
#x, tn, sol = linear_convection_lf(c, initial1, N, T, mu, num)

# Displaying figures
plot_solution(x, sol)

# Displaying an animation
anim = plot_animation(x, tn, sol)
# Saving the results as convect.gif (make sure that Google Drive is mounted)
anim.save('/content/drive/MyDrive/Colab Notebooks/fig/convect.gif', writer='pillow')
rc('animation', html='jshtml')
plt.close()
anim
