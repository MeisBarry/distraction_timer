import os
import platform
import subprocess
import time

from src.Utility import print_flush


class Timer(object):
    def __init__(self, mins, beeps=2, freq=3000):
        """ A nicey nice pomodoro timer class

        Arguments:
            mins (int): Number of minutes to run the timer for
            beeps (int): Number of beeps for the ending alarm
            freq (int): The frequency of the beep sound's sine wave

        Properties:
            platform (str): The current OS (e.g. Windows, etc.)
            start (float): Starting time from time.time()
            time_remaining (float): Time remaining in the timer
            time_remaining_clean (str): A pretty-printed representation of the time remaining
            done (bool): Timer complete status

            REFRESH_INTERVAL = Not sure, Barry included it
            POWERSHELL_LOC = The location of the PowerShell executable

        """

        self.mins = mins
        self.beeps = beeps
        self.freq = freq

        self.platform = platform.system()

        self.start = 0.0
        self.done = False

        self.REFRESH_INTERVAL = 0.2
        self.POWERSHELL_LOC = "C:/WINDOWS/system32/WindowsPowerShell/v1.0/powershell.exe"

    @property
    def time_remaining(self):
        """ The time remaining; returns 0 if timer 'runs out' """
        tr = self.start + (self.mins * 60) - time.time()
        if tr <= 0:
            return 0
        return tr

    @property
    def time_remaining_clean(self):
        """ A pretty-printed representation of the time remaining """
        return time.strftime('%M:%S', time.gmtime(self.time_remaining))

    def done_beeps_linux(self):
        """ Beeps for open-source """
        for i in range(self.beeps):
            os.system('play \
                        --no-show-progress \
                        --null \
                        --channels 1 \
                        synth 0.1 \
                        sine {base_freq} \
                        vol 0.3'.format(base_freq=self.freq))
            time.sleep(0.1)

    def done_beeps_windows(self):
        """ Beeps for virus-riddled nonsense """
        for i in range(self.beeps):
            subprocess.call([
                self.POWERSHELL_LOC,
                '[console]::beep({ps_freq}, {ps_time})'.format(
                    ps_freq=self.freq,
                    ps_time='100'
                )
            ])
            time.sleep(0.1)

    def run(self):
        """ Actually start the timer """
        self.start = time.time()
        while self.time_remaining:
            print_flush(self.time_remaining_clean)
            time.sleep(self.REFRESH_INTERVAL)
        print()  # puts your prompt on a new line
        self.done = True

    def finish(self):
        """ Called at the end of the timer; checks for `done` status """
        if self.done:
            if self.platform == 'Windows':
                self.done_beeps_windows()
            else:
                self.done_beeps_linux()
        else:
            out_str = 'Your timer is not yet finished, {time_remain} remaining'
            print(out_str.format(time_remain=self.time_remaining_clean))

    def begin(self):
        self.run()
        self.finish()
