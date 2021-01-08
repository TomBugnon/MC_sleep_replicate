## Parameter files for all the simulations described in :

"Sleep and wake in a model of the thalamocortical system with Martinotti cells", Tom Bugnon, William G. P. Mayner, Chiara Cirelli and Giulio Tononi

### Running the simulation

1. Install NEST v2.20

2. Make the updated ht_neuron model available to NEST by installing the extension module at `../extension_modules`

2. Install the `MC_sleep` branch of deNEST with `pip install git+https://github.com/tombugnon/denest.git@MC_sleep`

3. From this directory, run all the simulations with `python run_all.py`. Comment out the relevant lines in `run_all.py` to run only a subset of simulations . Output raw data and recorder metadata will be saved in the `data` subdirectory for each individual simulation.
