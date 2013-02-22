import sherpa.astro.ui as ui
from spec import load_data, report_results

# Load data
x, y, y_err = load_data()
ui.load_arrays(1, x, y, y_err)

# Set up the model
ui.set_model(ui.powlaw1d.pl)
pl.gamma, pl.ampl = 2, 1e-12

# Perform fit
ui.fit() # Compute best-fit parameters
ui.covar() # Compute covariance matrix (i.e. errors)
#ui.conf() # Compute profile errors
#ui.show_all() # Print a very nice summary of your session to less

# Report results
fr = ui.get_fit_results()
cr = ui.get_covar_results()

package = 'sherpa'
gamma, norm = fr.parvals
chi2 = fr.statval
gamma_err, norm_err = cr.parmaxes
cov = cr.extra_output[1, 0]
corr = cov / (norm_err * gamma_err)
report_results(package, norm, norm_err, gamma, gamma_err,
               chi2, cov, corr)

