from pytracking.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.got10k_path = ''
    settings.lasot_path = ''
    settings.network_path = '/disk/xuxiang/FCOT/models/'    # Where tracking networks are stored.
    settings.nfs_path = ''
    settings.otb_path = ''
    settings.packed_results_path = '/disk/xuxiang/FCOT/pytracking/tracking_results/'
    settings.results_path = '/disk/xuxiang/FCOT/pytracking/tracking_results/'    # Where to store tracking results
    settings.trackingnet_path = ''
    settings.uav_path = ''
    settings.vot_path = '/nas/datasets/VOT/vot2018/'

    return settings

