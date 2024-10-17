import pytest
import _pytest
import sys
import io
from pprint import pprint

def pytest_terminal_summary(terminalreporter, exitstatus, config):    
    total_tests = len(set([report.location[2] for report in terminalreporter.stats.get('')]))
    total_passed = len(terminalreporter.stats.get('passed', 0))    
    with open('pytest_stdout.log','w') as f:
        f.write(f'Score: {(total_passed/total_tests)*100}%\n')
        terminalreporter.writer = terminalreporter._tw = _pytest.config.create_terminal_writer(config, f)        
        terminalreporter.short_test_summary()
        terminalreporter.summary_stats()        

    terminalreporter.writer = terminalreporter._tw = _pytest.config.create_terminal_writer(config, sys.stdout)       
