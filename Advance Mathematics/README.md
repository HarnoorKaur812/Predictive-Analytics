The estimation technique used is histogram-based non-linear least squares estimation. First, the probability density function of the transformed random variable 𝑧.    z is approximated using a normalized histogram. A Gaussian-type parametric model is then assumed for the distribution of 𝑧. The unknown parameters of this model are estimated by minimizing the squared error between the empirical PDF values and the theoretical model values. This optimization is performed using SciPy’s curve_fit.

Result:
c= 0.02680311584081422, 
λ= 0.002057693030878697, 
μ= 19.629308102018342
