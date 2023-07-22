from os import listdir
from os.path import isfile, join
import re
import json
from Log import get_logger
from logging import CRITICAL
import argparse


# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Safe Snapraid. Safely test if everything what has been deleted also has been deleted')

# Add arguments to the parser
parser.add_argument('-d', '--diff', default=None, help='Check snapraid')
parser.add_argument('--json', default=None, help='Return JSON')
parser.add_argument('--test', action=argparse.BooleanOptionalAction, default=False, help='Return Test scripts in test directory')
parser.add_argument('-e', '--only-exit', action=argparse.BooleanOptionalAction, default=False, help='Return Test scripts in test directory')


args = parser.parse_args()

# Get snapraid diff

class SafeSnapraid:

    def __init__(self) -> None:
        self.log = get_logger('DEBUG')

    def run(self, txt):
        """Run for live"""
        # Prepare json Obj
        json_obj = {
            'safe': [],
            'unsafe': []
        }

        fls = re.findall(r'remove\s(.*)', txt)

        for fl in fls:
            # Check if exists in 
            mtc = re.findall(fr'copy\s({fl})', txt)
            if mtc:
                self.log.debug(f'\t{fl} exists in copy regex')
                json_obj['safe'].append(fl)
            else:
                self.log.warning(f'{fl} is removed but not copied!')
                json_obj['unsafe'].append(fl)

        return json_obj
        # self.log.debug(json.dumps(json_obj, indent=4))
    
    def run_tests(self):
        """Run all tests in the tests directory"""

        # If testing then run over all the tests
        mypath = ['.', 'tests']
        files = [join(*mypath, f) for f in listdir(join(*mypath)) if isfile(join(*mypath, f))]

        for f in files:
            self.log.info(f'Running test for [{f}]')
            with open(f) as f:
                self.run(f.read())

snap = SafeSnapraid()

# Run tests
if args.test == True:
    snap.run_tests()

# Run live
elif args.diff != None:
    if args.only_exit == True:
        snap.log.setLevel(CRITICAL)
    snap.log.info('Running SafeSnapraid')
    result = snap.run(args.diff)

    if len(result['unsafe']) > 0:
        exit(-1)
    else:
        exit(0)

else:
    parser.print_help()