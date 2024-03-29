#!/usr/bin/env python2
from __future__ import print_function, with_statement, division, generators
import socket, json, struct
import threading
import sys, os, re, argparse, copy, time, datetime
import errno
from traceback import print_exc

from headers import *
from param_utils import *

class ConnectorThread(threading.Thread):
    def __init__(self, meta, meta_rlock, db, db_rlock, server_ip, server_port):
        super(self.__class__, self).__init__()
        
        self.meta = meta
        self.meta_rlock = meta_rlock
        self.db = db
        self.db_rlock = db_rlock
        self.server_ip = server_ip
        self.server_port = server_port

    def run(self):

        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("server_ip: {server_ip} [{server_port_type}],\nserver_port: {server_port} [{server_port_type}]".format(
            server_ip=self.server_ip,
            server_ip_type=type(self.server_ip),
            server_port=self.server_port,
            server_port_type=type(self.server_port),
            ))
        conn = None
        for i in range(10):
            try:
                conn = socket.create_connection((self.server_ip, self.server_port), timeout=20)
                break
            except EnvironmentError, err:
                if err.errno == 61:
                    print(">>>> Connection refused.")
                    time.sleep(1)

                else:
                    print("EXCEPTION: errno: {errno}".format(errno=err.errno))
                    print_exc()
                    sys.exit(-1)

        if conn:
            state = EmissionThread_state_INIT
             
            #while True:
            for i in range(10):
                if state == EmissionThread_state_INIT:
                    print("would be emitting stuff !")
                    time.sleep(0.01)

        else:
            print("WE FAILED") 


if __name__ == '__main__':

    db = {}
    db_rlock = threading.RLock()
    meta = {
        "server_queries":{
            "pull_part_param",
            "pull_full_param",   
        },
        "exceptions-log": open("./exceptions.log", "a"),
    }

    meta_rlock = threading.RLock()

    acceptor_thread = AcceptorThread(meta, meta_rlock, db, db_rlock)
    acceptor_thread.start()

    connector_thread = ConnectorThread(meta, meta_rlock, db, db_rlock, IP, PORT)
    connector_thread.start()

    acceptor_thread.join()
    connector_thread.join()
    