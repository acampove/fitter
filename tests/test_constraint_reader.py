'''
Module with functions needed to test ConstraintReader class
'''

import pytest
from dmu.logging.log_store    import LogStore
from fitter.constraint_reader import ConstraintReader

log=LogStore.add_logger('fitter:test_constraint_reader')
# --------------------------------------------------------------
class Data:
    '''
    Data class
    '''
    l_sig_par = [
        'ar_dscb_Signal_002_1_reso_flt',
        'mu_Signal_000_scale_flt',
        'mu_Signal_001_scale_flt',
        'mu_Signal_002_scale_flt',
        'nl_dscb_Signal_001_1_reso_flt',
        'nr_dscb_Signal_002_1_reso_flt',
        'sg_Signal_000_reso_flt',
        'sg_Signal_001_reso_flt',
        'sg_Signal_002_reso_flt',
    ]

    l_brem_frac = [
        'frac_brem_000',
        'frac_brem_001',
        'frac_brem_002',
    ]

    l_prec_par  = [
        'sBd_Kstee_eq_btosllball05_DPC',
        'sBu_Kstee_Kpi0_eq_btosllball05_DPC',
        'sBs_phiee_eq_Ball_DPC',
    ]

    l_invalid = [
        'ap_hypexp',
        'bt_hypexp',
        'mu_hypexp',
        'ncmb',
        'nsig',
    ]
# --------------------------------------------------------------
def _print_constraints(d_cns : dict[str, tuple[float,float]]) -> None:
    for name, (value, error) in d_cns.items():
        log.info(f'{name:<40}{value:<20.3f}{error:<20.3f}')
# --------------------------------------------------------------
def test_signal():
    '''
    Tests getting constraints for signal parameters
    '''
    q2bin     = 'central'
    l_sig_par = Data.l_sig_par + Data.l_brem_frac

    obj     = ConstraintReader(parameters = l_sig_par, q2bin=q2bin)
    d_cns   = obj.get_constraints()
    _print_constraints(d_cns)

    assert len(d_cns) > 0
# --------------------------------------------------------------
@pytest.mark.parametrize('q2bin', ['low', 'central', 'high'])
def test_prec(q2bin : str):
    '''
    Tests getting constraints for prec parameters
    '''
    obj     = ConstraintReader(parameters = Data.l_prec_par, q2bin=q2bin)
    d_cns   = obj.get_constraints()
    _print_constraints(d_cns)

    assert len(d_cns) > 0
# --------------------------------------------------------------
def test_all():
    '''
    Tests getting constraints all model parameters
    '''
    q2bin = 'central'
    l_par = Data.l_sig_par + Data.l_brem_frac + Data.l_prec_par

    obj   = ConstraintReader(parameters = l_par, q2bin=q2bin)
    d_cns = obj.get_constraints()
    _print_constraints(d_cns)

    assert len(d_cns) > 0
# --------------------------------------------------------------
