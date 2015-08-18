from threading import Thread
import rospy

class EventMonitor(Thread):
    
    def __init__(self, target, args=(), kwargs={}):
        Thread.__init__(self, target=target, args=args, kwargs=kwargs)
        self._return = None

    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args, **self._Thread__kwargs)

    def join(self, timeout=None):
        Thread.join(self, timeout=timeout)
        return self._return

    def get_result(self):
        return self._return

    def terminate(self):
        if self.is_alive():
            Thread._Thread__stop(self)