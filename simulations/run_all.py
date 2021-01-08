import denest
import glob
from pathlib import Path

# Each contains 'parameter_tree.yml'
# After run, raw data and recorder metadata is saved in `<simulation_dir>/data`
# Comment out lines if you don't want to run all
SIMULATION_DIRS = [
    # Reference simulations
    *glob.glob('./fig0_wake_mode_spontaneous/'),
    *glob.glob('./fig0_wake_mode_stimuli/'),
    *glob.glob('./fig0_sleep_mode/'),
    *glob.glob('./fig2_wake_mode_stimuli_highdef/'),
    *glob.glob('./SM_fig2_sleep_mode_highdef/'),
    # Parameter exploration
    *glob.glob('./fig5_modulation_gaba_b1a/*'),
    *glob.glob('./fig6_modulation_gKL_gAMPA/*'),
    *glob.glob('./SM_fig5_modulation_gNaP_gKNa/g_KNa/*'),
    *glob.glob('./SM_fig5_modulation_gNaP_gKNa/g_NaP/*'),
    # local AMPA
    *glob.glob('./fig8_local_AMPA/from_sleep/*'),
    *glob.glob('./fig8_local_AMPA/from_wake_g_KL=1.0/*'),
    *glob.glob('./fig8_local_AMPA/from_wake_g_KL=1.05/*'),
    *glob.glob('./fig8_local_AMPA/from_wake_g_KL=1.1/*'),
    *glob.glob('./fig8_local_AMPA/from_wake_g_KL=1.15/*'),
    *glob.glob('./fig8_local_AMPA/from_wake_g_KL=1.2/*'),
    # stimulation
    *glob.glob('./fig9_stimulation/from_sleep_MCs/*'),
    *glob.glob('./fig9_stimulation/from_sleep_all_units/*'),
    *glob.glob('./fig9_stimulation/from_wake_MCs/*'),
    *glob.glob('./fig9_stimulation/from_wake_all_units/*'),
    # SM: Sleep mode without MaCs
    *glob.glob('./SM_fig3_sleep_noMC/'),
]

N_JOBS = 1  # Install joblib if >1. Be careful with memory


def run_dir(simulation_dir):
    assert (Path(simulation_dir)/'parameter_tree.yml').exists()
    sim_params = denest.ParamsTree.read(
        Path(simulation_dir)/'parameter_tree.yml'
    )
    sim = denest.Simulation(sim_params)
    sim.run()


def run_all(simulation_dirs, n_jobs=1):

    print(f"Running N={len(simulation_dirs)} simulations")

    if N_JOBS == 1:
        for sim_dir in simulation_dirs:
            run_dir(sim_dir)

    else:
        from joblib import Parallel, delayed
        Parallel(n_jobs=n_jobs)(
            delayed(run_dir)(sim_dir) for sim_dir in simulation_dirs
        )

if __name__ == "__main__":
    run_all(SIMULATION_DIRS, n_jobs=N_JOBS)
