from parcels import rng as random
import math


__all__ = ['BrownianMotion2DFieldKh', 'SpatiallyVaryingDiffusion2D']


def BrownianMotion2DFieldKh(particle, fieldset, time, dt):
    # Kernel for simple Brownian particle diffusion in zonal and meridional direction.
    # Assumes that fieldset has fields Kh_zonal and Kh_meridional

    r = 1/3.
    kh_meridional = fieldset.Kh_meridional[time, particle.lon, particle.lat, particle.depth]
    particle.lat += random.uniform(-1., 1.)*math.sqrt(2*dt*kh_meridional/r)
    kh_zonal = fieldset.Kh_zonal[time, particle.lon, particle.lat, particle.depth]
    particle.lon += random.uniform(-1., 1.)*math.sqrt(2*dt*kh_zonal/r)


def SpatiallyVaryingDiffusion2D(particle, fieldset, time, dt):
    # Diffusion equations for particles in non-uniform diffusivity fields
    # from Ross &  Sharples 2004 and Spagnol et al. 2002

    r_var = 1/3.
    kh_meridional = fieldset.Kh_meridional[time, particle.lon, particle.lat, particle.depth]
    Ry = random.uniform(-1., 1.) * math.sqrt(2 * kh_meridional * dt / r_var)
    kh_zonal = fieldset.Kh_zonal[time, particle.lon, particle.lat, particle.depth]
    Rx = random.uniform(-1., 1.) * math.sqrt(2 * kh_zonal * dt / r_var)

    # Deterministic 'boost' out of areas of low diffusivity
    dKdx = fieldset.dKh_zonal_dx[time, particle.lon, particle.lat, particle.depth]
    dKdy = fieldset.dKh_meridional_dy[time, particle.lon, particle.lat, particle.depth]
    CorrectionX = dKdx * dt
    CorrectionY = dKdy * dt

    # diffuse particle
    particle.lon += Rx + CorrectionX
    particle.lat += Ry + CorrectionY
