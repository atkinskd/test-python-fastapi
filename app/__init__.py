from asag_adp_logger.logger import PythonLogger

logger = PythonLogger("appsec-ken-test-api")

logger.debug("Loggers were reset", extra={"operationCode": "ALL_LOGGERS_SET"})
