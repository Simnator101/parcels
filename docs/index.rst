.. parcels documentation master file, created by
   sphinx-quickstart on Tue Oct 20 09:58:20 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Parcels
===================================

**Parcels** (**P**\ robably **A** **R**\ eally **C**\ omputationally **E**\ fficient **L**\ agrangian **S**\ imulator) is an experimental prototype code aimed at exploring novel approaches for Lagrangian tracking of virtual ocean particles in the petascale age. 

Its code is licensed under an `open source MIT license <https://github.com/OceanPARCELS/parcels/blob/master/LICENSE.md>`_ and can be downloaded from https://github.com/OceanPARCELS/parcels.

.. figure:: http://oceanparcels.org/animated-gifs/globcurrent_fullyseeded.gif
   :align: center
   
   *Animation of virtual particles carried by ocean surface flow in the* `Agulhas Current <https://en.wikipedia.org/wiki/Agulhas_Current>`_ *off South Africa. The particles are advected with* `Parcels <http://oceanparcels.org/>`_ *in data from the* `GlobCurrent Project <http://globcurrent.ifremer.fr/products-data/products-overview>`_. *See* `this tutorial <http://nbviewer.jupyter.org/github/OceanPARCELS/parcels/blob/master/examples/tutorial_Agulhasparticles.ipynb>`_ *for the Parcels code behind this animated gif.*

Postdoc and PhD positions available in Parcels development
===================================

Through the "Tracking Of Plastic In Our Seas", funded by the European Research Council, we are currently advertising two positions to further develop and work with Parcels. Application deadline for both positions is 14 April 2017.

We are looking for a postdoc with very strong programming skills to further develop the Parcels framework, and help apply it to the dispersion of plastic in the ocean. `See here for a more detailed description. <https://www.academictransfer.com/employer/UU/vacancy/38805/lang/en/>`_

We are looking for a PhD candidate to develop code and parameterisations to make the particles from the Parcels framework behave like plastic. `See here for a more detailed description. <https://www.academictransfer.com/employer/UU/vacancy/38804/lang/en/>`_ de

Parcels development status
===================================

Parcels is currently close to what we will release at version 0.9. 
This v0.9 will be a fully-functional, feature-complete code for offline 
Lagrangian ocean analysis. See below for a list of features, or keep an eye 
on the `Github Development Timeline page
<https://github.com/OceanPARCELS/parcels/projects/1>`_

**Currently implemented**

* Advection of particles in 2D using inbuilt kernels for Runge-Kutta4, Runge-Kutta45 and Euler Forward and in 3D using the inbuilt kernel for Runge-Kutta4_3D (see :mod:`parcels.kernels.advection`)
* Ability to define and execute custom kernels (see `this part of the Tutorial <http://nbviewer.jupyter.org/github/OceanPARCELS/parcels/blob/master/examples/PARCELStutorial.ipynb#Adding-a-custom-behaviour-kernel>`_)
* Ability to add custom Variables to Particles (see `this part of the Tutorial <http://nbviewer.jupyter.org/github/OceanPARCELS/parcels/blob/master/examples/PARCELStutorial.ipynb#A-second-example-kernel:-calculating-distance-travelled>`_)
* Ability to add and remove Particles (see :func:`parcels.particleset.ParticleSet.add` and :func:`parcels.particleset.ParticleSet.remove`)
* Ability to run in both Scipy and JIT (Just-In-Time compilation) mode. The former is easier to debug, but the latter can be a factor 1,000 faster (see the `JIT-vs-Scipy tutorial <http://nbviewer.jupyter.org/github/OceanPARCELS/parcels/blob/master/examples/tutorial_jit_vs_scipy.ipynb>`_)
* Ability to read in any type of hydrodynamic field in NetCDF format, as long as the grid is rectangular (i.e. grid axes are aligned with longitude and latitude; see :mod:`parcels.fieldset.FieldSet.from_netcdf` and `this part of the Tutorial <http://nbviewer.jupyter.org/github/OceanPARCELS/parcels/blob/master/examples/PARCELStutorial.ipynb#Reading-in-data-from-arbritrary-NetCDF-files>`_)
* Output particles in NetCDF format (see :mod:`parcels.particlefile`)
* Basic plotting of particles, both on the fly and from netcdf output files (see the `plotting tutorial <http://nbviewer.jupyter.org/github/OceanPARCELS/parcels/blob/master/examples/tutorial_plotting.ipynb>`_)

**Major developed goals beyond v0.9**

* Diffusion of particles using suite of inbuilt kernels
* Support for non-rectangular grids, including unstructured meshes
* Implementation of parallel execution using tiling of the domain
* Faster and more efficient code
* Advanced control of particles near land boundaries


Parcels Tutorials 
===================================

The best way to get started with Parcels is to have a look at the Jupyter notebooks below:

* `Parcels tutorial <http://nbviewer.jupyter.org/github/OceanPARCELS/parcels/blob/master/examples/PARCELStutorial.ipynb>`_ for a general introduction and overview into the main features of Parcels

* `Periodic boundaries tutorial <https://nbviewer.jupyter.org/github/OceanPARCELS/parcels/blob/master/examples/tutorial_periodic_boundaries.ipynb>`_ for a tutorial on how to implement periodic boundary conditions

* `FieldSet.advancetime() tutorial <https://nbviewer.jupyter.org/github/OceanPARCELS/parcels/blob/master/examples/tutorial_advancetime.ipynb>`_ for a tutorial on how to use Parcels with datasets that have a large number of time snapshots.

* `Delayed start of particles tutorial <http://nbviewer.jupyter.org/github/OceanPARCELS/parcels/blob/master/examples/tutorial_delaystart.ipynb>`_ for a tutorial on how to add particles to a ParticleSet during runtime, so that not all particles are released on the start of the run.

* `JIT-vs-Scipy tutorial <http://nbviewer.jupyter.org/github/OceanPARCELS/parcels/blob/master/examples/tutorial_jit_vs_scipy.ipynb>`_ for a tutorial showing how JIT  and Scipy mode compare.

* `Animated Gif tutorial <http://nbviewer.jupyter.org/github/OceanPARCELS/parcels/blob/master/examples/tutorial_Agulhasparticles.ipynb>`_ for a  tutorial on how to created the Agulhas region animated gif on the top of this page. This tutorial also features a brief explanation of how to handle `OutOfBounds` errors.

* `Plotting tutorial <http://nbviewer.jupyter.org/github/OceanPARCELS/parcels/blob/master/examples/tutorial_plotting.ipynb>`_ for further explanation on the plotting capabilities of Parcels

Installing Parcels
===================================

The latest version of Parcels, including tests and examples, 
can be obtained directly from github via::
    git clone https://github.com/OceanPARCELS/parcels.git
    cd parcels; pip install -r requirements.txt
    python scripts/pull_data.py
    export PYTHONPATH="$PYTHONPATH:$PWD"

In order for Parcels to work from any directory, add the following line to 
your ~/.bash_profile::
    export PYTHONPATH="$PYTHONPATH:$PWD"

Note that a functional NetCDF install is required.

Getting involved
===================================

Parcels development is supported by Imperial College London, with contributions 
from the people listed on the `Contributors page 
<https://github.com/OceanPARCELS/parcels/graphs/contributors>`_. 

If you want to help out with developing, testing or get involved in another way, 
please join the `mailing list 
<https://mailman.ic.ac.uk/mailman/listinfo/oceanparcels>`_.


Python design overview
===================================

.. figure:: ParcelsDesign.png
   :align: center
   
   *The figure above gives a brief overview of how the most important classes and methods in Parcels are related.*


See below for links to the full documentation of the python code for Parcels


Writing Parcels Kernels
===================================

One of the most powerful features of Parcels is the ability to write custom Kernels (see e.g. `this part of the Tutorial <http://nbviewer.jupyter.org/github/OceanPARCELS/parcels/blob/master/examples/PARCELStutorial.ipynb#Adding-a-custom-behaviour-kernel>`_). These Kernels are little snippets of code that get executed by Parcels, giving the ability to add 'behaviour' to particles. 

However, there are some key limitations to the Kernels that everyone who wants to write their own should be aware of:

* Every Kernel must be a function with the following (and only those) arguments: ``(particle, fieldset, time, dt)``

* In order to run successfully in JIT mode, Kernel definitions can only contain the following types of commands:

  * Basic arithmetical operators (``+``, ``-``, ``*``, ``/``) and assignments (``=``).

  * Basic logical operators (``<``, ``==``, ``>``, ``&``, ``|``)

  * ``if`` and ``while`` loops, as well as ``break`` statements. Note that ``for``-loops are not supported in JIT mode
    
  * Interpolation of a ``Field`` from the ``fieldset`` at a (time, lon, lat, depth) point, using using square brackets notation. For example, to interpolate the zonal velocity (`U`) field at the particle location, use the following statement::

      value = fieldset.U[time, particle.lon, particle.lat, particle.depth]

  * Functions from the ``maths`` standard library and from the custom ``random`` library at :mod:`parcels.rng`
  
  * ``print`` statements. Note however that in JIT mode these only work well for variables that are either floats or any of the inbuilt Particle properties

All other functions and methods are not supported yet in Parcels Kernels. If there is a functionality that can not be programmed with this limited set of commands, please create an `Issue ticket <https://github.com/OceanPARCELS/parcels/issues>`_.

Parcels documentation
===================================

See below for the technical documentation on the different Parcels modules

.. toctree::
   :maxdepth: 0

   parcels


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

