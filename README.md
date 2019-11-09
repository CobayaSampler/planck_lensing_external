# Example CMB external likelihood

** work under developement ***

This is an example likelihood package that can be externally installed and then referenced from Coabay .yaml files 
via the qualified module name. It just reproduces the Planck 2018 likelihoods already installed with Cobaya.

Requires latest external_modules banch (https://github.com/CobayaSampler/cobaya/pull/53) of Cobaya.

The likelihood classes can also be instantiated and called directly:

        from plancklens.plancklens import plancklens
        like = plancklens()
        print('chi2 = ',-2*like.log_likelihood(cl_dict, A_planck=1.0))

This example packages data internally. For larger data the data should probably be stored externally and installed separately.

