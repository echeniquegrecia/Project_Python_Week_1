#!/usr/bin/env python3
import os
import subprocess
from api import format_response, parse_php_response, Addon

class Execute_Addon(Addon):

    def execute(self, duplex):
        if (".php" in duplex.request.uri):
            env = dict()
            root = os.path.dirname(os.path.abspath('myApache')) 
            env['SCRIPT_FILENAME'] = root + "/www" + duplex.request.uri
            conn = duplex.socket

            with subprocess.Popen('php-cgi', env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as process:
                stdout, stderr = process.communicate()
                response = parse_php_response(stdout)
                response = format_response(response)
                duplex.response = response.encode()