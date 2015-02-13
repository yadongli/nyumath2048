import numpy as np

class Swap(object) :
    def __init__(self, maturity, coupon, freq) :
        '''
        Args:
            freq: frequency of payments, 2 for semi-annual
        '''
        self.maturity = maturity
        self.coupon = coupon
        self.freq = freq
        
    def __str__(self) :
        return 'Swap: maturity %g, coupon %g, freq %g' % (self. maturity, self.coupon, self.freq)
 
def priceSwap(swap, discf) :
    '''
    compute par spreads and PV01 of a receiver IR swaps:
    Args:
        swap: a swap of type Swap
        discf: a function that computes discount curve, i.e., b(t)
    Returns:
        pv: the PV of the swap
    '''
    ts = np.arange(1./swap.freq, swap.maturity + 1e-6, 1./swap.freq) # why +1e-6?
    disc = discf(ts)
    pv01 = np.sum(disc)/swap.freq
    par = (1.-disc[-1])/pv01
    return (swap.coupon - par)*pv01

def swapParSpread(m, discf, freq) :
    '''
    compute par spreads and PV01 of IR swaps:
    Args:
        m: maturity
        discf: a function that computes discount curve, i.e., b(t)
        freq: coupon freq
    Returns:
        par: par spread
    '''
    ts = np.arange(1./freq, m + 1e-6, 1./freq) # why +1e-6?
    disc = discf(ts)
    pv01 = np.sum(disc)/freq
    return (1.-disc[-1])/pv01
