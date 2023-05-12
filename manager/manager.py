import threading
from console import log, log_debug
from timepulse.timepulse import timepulse


class run_timepulse:
    _thread = None

    @staticmethod
    def start():
        log_debug("start_timepulse")
        run_timepulse._thread = threading.Thread(target=timepulse)
        run_timepulse._thread.start()
        log("start_timepulse: Started listening to TimePulse")

    @staticmethod
    def stop():
        log_debug("stop_timepulse")
        if run_timepulse._thread:
            run_timepulse._thread.join()
            run_timepulse._thread = None
            log("stop_timepulse: Stopped listening to TimePulse")

    @staticmethod
    def is_running():
        return run_timepulse._thread != None
