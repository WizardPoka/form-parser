# validdator.py

from utils import ExecutableUtil


class Validator(ExecutableUtil):
    """
    DOCUMENTME
    """
    def execute(self, *args):
        """
        DOCUMENTME
        """
        self.validate(*args)
    
    def validate(self, word):
        """
        DOCUMENTME
        """
        # TODO: ImplementMe
        raise NotImplementedError('Implement validate in %s.' % (self.__class__.__name__))
