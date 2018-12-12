import difflib
import webbrowser
import os
from time import sleep


class Debug:

    @staticmethod
    def compare(expected, actual, show=True):
        report = 'debug_report.html'
        diff = difflib.HtmlDiff().make_file(expected.splitlines(), actual.splitlines())
        with open(report, 'w') as f:
            f.write(diff)
        url = report
        if show:
            webbrowser.open_new(url)
        sleep(1)
        os.remove(report)
