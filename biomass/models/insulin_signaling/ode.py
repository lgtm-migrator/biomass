from .name2idx import C, V
from .reaction_network import ReactionNetwork


class DifferentialEquation(ReactionNetwork):
    def __init__(self, perturbation):
        super(DifferentialEquation, self).__init__()
        self.perturbation = perturbation

    def diffeq(self, t, y, *x):

        v = self.flux(t, y, x)

        if self.perturbation:
            for i, dv in self.perturbation.items():
                v[i] = v[i] * dv

        dydt = [0] * V.NUM

        dydt[V.IRcom] = v[1] - v[2] - v[6] + v[7]
        dydt[V.p1IRcom] = v[2] - v[3] - v[4] + v[5]
        dydt[V.p2IRcom] = v[6] - v[7] - v[8] - v[9]
        dydt[V.p1p2IRcom] = v[4] - v[5] + v[9] - v[10]
        dydt[V.pAKT] = v[11] - v[12]
        dydt[V.pmTOR] = v[13] - v[14]
        dydt[V.pX] = v[17] - v[18]
        dydt[V.pS6K] = v[15] - v[16]
        dydt[V.pGSK3B] = v[19] - v[20]
        dydt[V.pFoxO1] = v[21] - v[22]
        dydt[V.G6Pase] = v[23] - v[24]

        return dydt


def param_values():
    x = [0] * C.NUM

    x[C.k1_synthesis] = 0.04780
    x[C.k1_InsIRcom] = 7.78161
    x[C.k2_InsIRcom] = 1.61148
    x[C.k1_p1IRcomDeg] = 0.00792
    x[C.k1_p1IRcomPhos] = 0.00004
    x[C.k1_p1p2IRcomdePhos] = 0.28443
    x[C.k1_IRcomPhos] = 9.93311
    x[C.k1_p2IRcomdePhos] = 0.00001
    x[C.k1_p2IRcomDeg] = 0.00001
    x[C.k1_Insp2IRcom] = 0.36303
    x[C.k2_Insp2IRcom] = 0.40813
    x[C.k1_p1p2IRcomDeg] = 0.09490
    x[C.k1_AKTPhos] = 0.00920
    x[C.k1_pAKTdePhos] = 7.70619
    x[C.k1_mTORPhos] = 0.41968
    x[C.k1_pmTORdePhos] = 0.12433
    x[C.k1_S6KPhos] = 0.00752
    x[C.k1_pS6KdePhos] = 1.95498
    x[C.k1_XPhos] = 0.00105
    x[C.k1_pXdePhos] = 0.00146
    x[C.k1_GSK3BPhos] = 2.97538
    x[C.k1_pGSK3BdePhos] = 0.92460
    x[C.k1_FoxO1Phos] = 4.59698
    x[C.k1_pFoxO1dePhos] = 0.15172
    x[C.k1_G6PaseSynthesis] = 4.86146
    x[C.k1_G6PaseDeg] = 0.05496

    return x


def initial_values():
    y0 = [0] * V.NUM

    y0[V.pro_IRcom] = 46.22225
    y0[V.IRcom] = 46.22225
    y0[V.p1IRcom] = 0
    y0[V.p2IRcom] = 0
    y0[V.p1p2IRcom] = 0
    y0[V.iAKT] = 4.33812
    y0[V.pAKT] = 0
    y0[V.imTOR] = 0.09592
    y0[V.pmTOR] = 0
    y0[V.iX] = 14.99133
    y0[V.pX] = 0
    y0[V.iS6K] = 2.77699
    y0[V.pS6K] = 0
    y0[V.iGSK3B] = 10.56415
    y0[V.pGSK3B] = 0
    y0[V.iFoxO1] = 0.43571
    y0[V.pFoxO1] = 0
    y0[V.G6Pase] = 38.54029

    return y0
