#!/usr/bin/env python3
#------------------------------------------------------------------------
# Image Processing Application: ipapp.py
#------------------------------------------------------------------------
import argparse
import logging

import ipcat

logger = logging.getLogger(__name__)

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--batch-mode', dest='batchMode',
                        action='store_true', default=False,
                        help='Run in batch mode (no GUI)')
    return parser.parse_args()

def run(args):
    app = ipcat.App(useGUI=not args.batchMode)

    if args.batchMode:
        logger.info('Running in batch mode')
        test = ipcat.BatchTest1('test1', app)
        test.run()
    else:
        app.mainloop()
    
if __name__ == '__main__':
    args = parseArgs()
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)8s %(name)-20s: %(message)s')
    run(args)
    
