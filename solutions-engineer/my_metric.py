from checks import AgentCheck
from random import *
class MyMetricRando(AgentCheck):
    def check(self, instance):
        self.gauge('my.metric', randint(1, 1000))
