import numpy as np
import sherpa.astro.ui as ui
from bb import BoxBOD, report_results

# Load data
ui.load_arrays(1, BoxBOD.x, BoxBOD.y, np.ones_like(BoxBOD.x))
# @todo: It is possible to give no staterror, but I'm not sure
# what Sherpa does then. fr.statval is no longer the correct chi2.

# Set up the model and load it as a Sherpa model
def boxbod_func(pars, x):
    b1, b2 = pars
    return BoxBOD.model(x, b1, b2)

ui.load_user_model(boxbod_func, "boxbod")
ui.add_user_pars("boxbod", ["b1", "b2"])
bb = boxbod
ui.set_model(bb)
bb.b1, bb.b2 = BoxBOD.p0[0], BoxBOD.p0[1]

# Perform fit
ui.set_stat('chi2datavar')
#ui.set_method('levmar') #  ['levmar', 'moncar', 'neldermead', 'simplex']
ui.set_method_opt('xtol', 1e-10)
ui.fit() # Compute best-fit parameters
ui.set_covar_opt('eps', 1e-5) # @todo: Why does this parameter have no effect
ui.covariance() # Compute covariance matrix (i.e. errors)
#ui.conf() # Compute profile errors
#ui.show_all() # Print a very nice summary of your session to less

# Report results
fr = ui.get_fit_results()
cr = ui.get_covar_results()

# Report results (we have to apply the s factor ourselves)
popt = np.array(fr.parvals)
chi2 = fr.statval
s_factor = np.sqrt(chi2 / fr.dof)
perr = s_factor * np.array(cr.parmaxes)
report_results('sherpa', popt, perr, chi2)

