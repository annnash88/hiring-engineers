from checks import AgentCheck
from random import *
class MyMetricRando(AgentCheck):
    def check(self, instance):
        self.gauge('my_metric', randint(1, 1000))
