from datetime import datetime


def log_event(event, logfile_name="test.log"):
    with open(logfile_name, mode="a") as file:
        file.write(f"{datetime.now()}: {event}\n")

log_event("Program started")
log_event("We're watching the program run.", "other.log")
log_event("Program finished")