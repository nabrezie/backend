"""Module to log changes in the register and database."""


class RegisterLogger:
    """Logger adapter to add module name to log messages,
    for changes in registr and databse.
    """

    def process(self, msg, kwargs):
        """Add module name to log messages."""
        return f'{self.extra["module"]} - {msg}', kwargs

    def export_log(self, filename):
        """Export log to a file."""
