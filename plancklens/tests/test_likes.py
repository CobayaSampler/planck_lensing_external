import unittest

camb_params = {
    "ombh2": 0.022274,
    "omch2": 0.11913,
    "cosmomc_theta": 0.01040867,
    "As": 0.2132755716e-8,
    "ns": 0.96597,
    "tau": 0.0639}


class LikeTest(unittest.TestCase):

    def test_indep(self):
        from plancklens.cmbmarged import cmbmarged
        import camb
        lmax = 2500
        pars = camb.set_params(lens_potential_accuracy=1, **camb_params, lmax=lmax)
        results = camb.get_results(pars)
        cls = results.get_total_cls(lmax, CMB_unit='muK')
        cl_dict = {p: cls[:, i] for i, p in enumerate(['tt', 'ee', 'bb', 'te'])}
        cl_dict['pp'] = results.get_lens_potential_cls(lmax)[:, 0]
        like = cmbmarged()
        self.assertAlmostEqual(-2 * like.log_likelihood(cl_dict), 8.76, 1)

        from plancklens.plancklens import plancklens
        like = plancklens()
        self.assertAlmostEqual(-2 * like.log_likelihood(cl_dict, A_planck=1.0), 8.734, 1)

        # aggressive likelihood
        like = cmbmarged({'dataset_file': 'data_2018/smicadx12_Dec5_ftl_mv2_ndclpp_p_teb_agr2_CMBmarged.dataset'})
        self.assertAlmostEqual(-2 * like.log_likelihood(cl_dict), 13.5, 1)

    def test_cobaya(self):
        from cobaya.model import get_model

        info = {'likelihood': {'plancklens.plancklens': None},
                'theory': {'camb': {"extra_args": {"lens_potential_accuracy": 1}}},
                'params': camb_params}
        model = get_model(info)
        chi2 = -2 * model.loglikes({'A_planck': 1.0})[0]
        self.assertAlmostEqual(chi2[0], 8.734, 1)

        info = {'likelihood': {'plancklens.cmbmarged': None},
                'theory': {'camb': {"extra_args": {"lens_potential_accuracy": 1}}},
                'params': camb_params}
        model = get_model(info)
        chi2 = -2 * model.loglikes({})[0]
        self.assertAlmostEqual(chi2[0], 8.765, 1)
