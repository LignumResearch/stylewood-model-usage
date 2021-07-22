# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# This work is licensed under the Creative Commons Attribution-NonCommercial
# 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to
# Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

"""Main entry point for training StyleGAN and ProGAN networks."""

import copy
import dnnlib
from dnnlib import EasyDict

import config
from metrics import metric_base

#----------------------------------------------------------------------------
# Official training configs for StyleGAN, targeted mainly for FFHQ.

if 1:
    desc          = 'sgan'                                                                 # Description string included in result subdir name.
    train         = EasyDict(run_func_name='training.training_loop.training_loop')         # Options for training loop.
    G             = EasyDict(func_name='training.networks_stylegan.G_style')               # Options for generator network.
    D             = EasyDict(func_name='training.networks_stylegan.D_basic')               # Options for discriminator network.
    G_opt         = EasyDict(beta1=0.0, beta2=0.99, epsilon=1e-8)                          # Options for generator optimizer.
    D_opt         = EasyDict(beta1=0.0, beta2=0.99, epsilon=1e-8)                          # Options for discriminator optimizer.
    G_loss        = EasyDict(func_name='training.loss.G_logistic_nonsaturating')           # Options for generator loss.
    D_loss        = EasyDict(func_name='training.loss.D_logistic_simplegp', r1_gamma=10.0) # Options for discriminator loss.
    dataset       = EasyDict()                                                             # Options for load_dataset().
    sched         = EasyDict()                                                             # Options for TrainingSchedule.
    grid          = EasyDict(size='4k', layout='random')                                   # Options for setup_snapshot_image_grid().
    metrics       = [metric_base.fid50k]                                                   # Options for MetricGroup.
    submit_config = dnnlib.SubmitConfig()                                                  # Options for dnnlib.submit_run().
    tf_config     = {'rnd.np_random_seed': 1000}                                           # Options for tflib.init_tf().

    # Dataset.
    desc += '-dataset';            dataset = EasyDict(tfrecord_dir='YOUR PATH HERE', resolution = 512); train.mirror_augment = True

    # Number of GPUs.
    #desc += '-1gpu'; submit_config.num_gpus = 1; sched.minibatch_base = 4; sched.minibatch_dict = {4: 128, 8: 128, 16: 128, 32: 64, 64: 32, 128: 16, 256: 8, 512: 4}
    #desc += '-2gpu'; submit_config.num_gpus = 2; sched.minibatch_base = 8; sched.minibatch_dict = {4: 256, 8: 256, 16: 128, 32: 64, 64: 32, 128: 16, 256: 8}
    desc += '-4gpu'; submit_config.num_gpus = 4; sched.minibatch_base = 32; sched.minibatch_dict = {4: 256, 8: 256, 16: 256, 32: 256, 64: 64, 128: 32, 256: 16, 512: 4}
    #desc += '-8gpu'; submit_config.num_gpus = 8; sched.minibatch_base = 32; sched.minibatch_dict = {4: 512, 8: 256, 16: 128, 32: 64, 64: 32}

    # Default options.
    train.total_kimg = 40000
    sched.lod_initial_resolution = 8
    sched.G_lrate_dict = {128: 0.0015, 256: 0.002, 512: 0.003, 1024: 0.003}
    sched.D_lrate_dict = EasyDict(sched.G_lrate_dict)

    # WGAN-GP loss
    #desc += '-wgangp'; G_loss = EasyDict(func_name='training.loss.G_wgan'); D_loss = EasyDict(func_name='training.loss.D_wgan_gp'); sched.G_lrate_dict = {k: min(v, 0.002) for k, v in sched.G_lrate_dict.items()}; sched.D_lrate_dict = EasyDict(sched.G_lrate_dict)

    # Table 1.
    #desc += '-tuned-baseline'; G.use_styles = False; G.use_pixel_norm = True; G.use_instance_norm = False; G.mapping_layers = 0; G.truncation_psi = None; G.const_input_layer = False; G.style_mixing_prob = 0.0; G.use_noise = False
    #desc += '-add-mapping-and-styles'; G.const_input_layer = False; G.style_mixing_prob = 0.0; G.use_noise = False
    #desc += '-remove-traditional-input'; G.style_mixing_prob = 0.0; G.use_noise = False
    #desc += '-add-noise-inputs'; G.style_mixing_prob = 0.0
    #desc += '-mixing-regularization' # default

    # Table 2.
    #desc += '-mix0'; G.style_mixing_prob = 0.0
    #desc += '-mix50'; G.style_mixing_prob = 0.5
    #desc += '-mix90'; G.style_mixing_prob = 0.9 # default
    #desc += '-mix100'; G.style_mixing_prob = 1.0

    # Table 4.
    #desc += '-traditional-0'; G.use_styles = False; G.use_pixel_norm = True; G.use_instance_norm = False; G.mapping_layers = 0; G.truncation_psi = None; G.const_input_layer = False; G.style_mixing_prob = 0.0; G.use_noise = False
    #desc += '-traditional-8'; G.use_styles = False; G.use_pixel_norm = True; G.use_instance_norm = False; G.mapping_layers = 8; G.truncation_psi = None; G.const_input_layer = False; G.style_mixing_prob = 0.0; G.use_noise = False
    #desc += '-stylebased-0'; G.mapping_layers = 0
    #desc += '-stylebased-1'; G.mapping_layers = 1
    #desc += '-stylebased-2'; G.mapping_layers = 2
    #desc += '-stylebased-8'; G.mapping_layers = 8 # default


def main():
    kwargs = EasyDict(train)
    kwargs.update(G_args=G, D_args=D, G_opt_args=G_opt, D_opt_args=D_opt, G_loss_args=G_loss, D_loss_args=D_loss)
    kwargs.update(dataset_args=dataset, sched_args=sched, grid_args=grid, metric_arg_list=metrics, tf_config=tf_config)
    kwargs.submit_config = copy.deepcopy(submit_config)
    kwargs.submit_config.run_dir_root = dnnlib.submission.submit.get_template_from_path(config.result_dir)
    kwargs.submit_config.run_dir_ignore += config.run_dir_ignore
    kwargs.submit_config.run_desc = desc
    dnnlib.submit_run(**kwargs)

#----------------------------------------------------------------------------

if __name__ == "__main__":
    main()

#----------------------------------------------------------------------------
