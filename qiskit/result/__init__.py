# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2018.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
=========================================
Experiment Results (:mod:`qiskit.result`)
=========================================

.. currentmodule:: qiskit.result

.. autosummary::
   :toctree: ../stubs/

   Result
   ResultError
   Counts
   marginal_counts
   marginal_distribution

Distributions
=============

.. autosummary::
   :toctree: ../stubs/

   ProbDistribution
   QuasiDistribution

Mitigation
==========
.. autosummary::
   :toctree: ../stubs/

   BaseReadoutMitigator
   CorrelatedReadoutMitigator
   LocalReadoutMitigator

"""

from .result import Result
from .exceptions import ResultError
from .utils import marginal_counts
from .utils import marginal_distribution
from .counts import Counts

from .distributions.probability import ProbDistribution
from .distributions.quasi import QuasiDistribution
from .mitigation.base_readout_mitigator import BaseReadoutMitigator
from .mitigation.correlated_readout_mitigator import CorrelatedReadoutMitigator
from .mitigation.local_readout_mitigator import LocalReadoutMitigator
