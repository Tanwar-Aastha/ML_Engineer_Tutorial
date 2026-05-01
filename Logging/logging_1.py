import logging

# setting up basic configurations of logging message
logging.basicConfig(
    filename="app.log",   # setting the file name where the logs will be kept
    level=logging.ERROR,  # type of message we want to log
    format="%(asctime)s - %(levelname)s - %(message)s"   # format of the log
)

logging.error("This is an error Message")
logging.info("This is a info msg")
logging.debug("Debugging the message")


