"""Module to log changes in the register and database."""
import logging

MODULE_Logger = logging.getLogger(__name__)
MODULE_Logger.setLevel(logging.DEBUG)


class RegisterLogger(logging.LoggerAdapter):
    """Logger adapter to add module name to log messages,
    for changes in registr and databse.
    """

    def __init__(self, module):
        """Initialize logger."""
        self.extra = {'module': module}
        super().__init__(MODULE_Logger, self.extra)

    def process(self, msg, kwargs):
        """Add module name to log messages."""
        return f'{self.extra["module"]} - {msg}', kwargs

    def export_log(self, filename):
        """Export log to a file."""
        with open(filename, 'w') as file:
            for record in self.logger.handlers[0].buffer:
                file.write(f'{record.levelname} - {record.msg}\n')
        self.logger.handlers[0].buffer = []
