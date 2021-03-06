#!/usr/bin/env python

"""Implementation and improvement of the paper:
Unsupervised learning and segmentation of complex activities from video.
"""

__author__ = 'Anna Kukleva'
__date__ = 'June 2019'

import sys
import os
sys.path.append(os.path.abspath('.').split('data_utils')[0])

from ute.utils.arg_pars import opt
from data_utils.dummy_utils.update_argpars import update

from ute.ute_pipeline import temp_embed, all_actions


if __name__ == '__main__':

    # set root
    opt.dataset_root = '/sequoia/data1/akukleva/projects/unsup_temp_embed/dummy_data'

    # set activity name
    opt.subaction = 'coffee'
    # set feature extension and dimensionality
    opt.ext = 'txt'
    opt.feature_dim = 64

    # model name can be 'mlp' or 'nothing' for no embedding (just raw features)
    opt.model_name = 'mlp'

    # resume training
    opt.resume = False
    # load an already trained model (stored in the models directory in dataset_root)
    opt.load_model = False

    opt.lr = 1e-3
    opt.epochs = 10

    # dimensionality of your embedding
    opt.embed_dim = 20

    # use background noise (e.g. for YTI)
    opt.bg = False

    # update log name and absolute paths
    update()

    # run temporal embedding
    if opt.subaction == 'all':
        actions = ['coffee']
        all_actions(actions)
    else:
        temp_embed()


