"""Module to log changes in the register and database."""
import logging

MODULE_LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class RegisterLogger(logging.LoggerAdapter):
    """Logger adapter to add module name to log messages, 
    for changes in registr and databse.
    """

    def __init__(self, logger, extra):
        """Initialize the logger adapter."""
        super(RegisterLogger, self).__init__(logger, extra)

    def process(self, msg, kwargs):
        """Add module name to log messages."""
        return f'{self.extra["module"]} - {msg}', kwargs

    def export_log(self, filename):
        """Export log to a file."""
        with open(filename, 'w') as file:
            for record in self.logger.handlers[0].buffer:
                file.write(f'{record}\n')
