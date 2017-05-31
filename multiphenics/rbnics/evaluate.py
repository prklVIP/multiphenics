# Copyright (C) 2015-2017 by the RBniCS authors
# Copyright (C) 2016-2017 by the multiphenics authors
#
# This file is part of the RBniCS interface to multiphenics.
#
# RBniCS and multiphenics are free software: you can redistribute them and/or modify
# them under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# RBniCS and multiphenics are distributed in the hope that they will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with RBniCS and multiphenics. If not, see <http://www.gnu.org/licenses/>.
#

from multiphenics.rbnics.matrix import Matrix
from multiphenics.rbnics.vector import Vector
from multiphenics.rbnics.function import Function
from multiphenics.rbnics.functions_list import FunctionsList
from multiphenics.rbnics.tensors_list import TensorsList
from multiphenics.rbnics.parametrized_tensor_factory import ParametrizedTensorFactory
from multiphenics.rbnics.parametrized_expression_factory import ParametrizedExpressionFactory
from multiphenics.rbnics.reduced_mesh import ReducedMesh
from multiphenics.rbnics.reduced_vertices import ReducedVertices
from rbnics.utils.decorators import backend_for, tuple_of

# Evaluate a parametrized expression, possibly at a specific location
#@backend_for("multiphenics", inputs=((Matrix.Type(), Vector.Type(), Function.Type(), TensorsList, FunctionsList, ParametrizedTensorFactory, ParametrizedExpressionFactory), (ReducedMesh, ReducedVertices, None)))
def evaluate(expression_, at=None):
    pass # TODO
    
