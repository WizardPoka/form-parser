# notifier.py

from utils import ExecutableUtil


class Notifier(ExecutableUtil):
    """
    DOCUMENTME
    """
    def __init__(self, cfg):
        self.server = cfg 
        
    def execute(self, *args):
        """
        DOCUMENTME
        """
        self.notify(*args)
        
    def notify(self, mail, lst):
        """
        DOCUMENTME
        """
        # TODO: ImplementMe
        raise NotImplementedError('Implement notify in %s.' % (self.__class__.__name__))
