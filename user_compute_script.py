""" Extremely simple launch script. Should be improved. """
#!/usr/bin/env python2

PORT = 6000

from __future__ import print_function, with_statement, division, generators
import os, sys, re, threading, socket, argparse, time
import subprocess as sp
import postgres

def getTOD():
    return time.strftime("%H:%M:%S", time.gmtime())


def entete():
    return "PBS_NODENUM#%s - %s" % (getTOD(), s.environ["PBS_NODENUM"],)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sql_server_ip', nargs=1, type=str)
    parser.add_argument('--sql_server_port', nargs=1, type=str)
    parser.add_argument('--job_id', nargs=1, type=int)
    args = parser.parse_args()


    postgres.save_proc_entry(args.job_id, os.environ["PBS_NODENUM"], PORT)
    


if __name__ == '__main__':
    main()
