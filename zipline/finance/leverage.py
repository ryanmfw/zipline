#
# Copyright 2013 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from functools import partial
import abc

def leverage_stub(leverage, portfolio, order):
    return leverage.validate(order, portfolio)

def leverage_partial(leverage, portfolio):
    return partial(leverage_stub, leverage, portfolio)

class LeverageModel(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def validate(self, order, portfolio):
        pass


class NullLeverage(object):
    def validate(self, order, portfolio):
        return True
