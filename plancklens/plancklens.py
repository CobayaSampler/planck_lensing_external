from cobaya.likelihoods._base_classes import _cmblikes_prototype


class plancklens(_cmblikes_prototype):
    # You can either keep data separate and set install_options for where to download from, or
    # (if not too big) bundle the data in the package, so don't need separate install as here
    install_options = {}
