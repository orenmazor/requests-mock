# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


class MockException(BaseException):
    """Base Exception for library"""


class NoMockAddress(MockException):
    """The requested URL was not mocked"""

    def __init__(self, request):
        self.request = request

    def __str__(self):
        return "No mock address: %s %s" % (self.request.method,
                                           self.request.url)


class UncalledMockedAddressException(MockException):
    """The requested url was mocked but never called!"""

    def __init__(self, matcher):
        self.matcher = matcher

    def __str__(self):
        return "Mocked address %s %s but never called" % (self.matcher._method,
                                                          self.matcher._url)


class InvalidRequest(MockException):
    """This call cannot be made under a mocked environment"""
