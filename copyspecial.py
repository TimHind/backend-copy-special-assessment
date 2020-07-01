#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "???"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    special_list = []
    for path in os.listdir(dirname):
        # if "__" in path:
        match = re.search(r'__(\w+)__', path)
        if match: 
            special_list.append(os.path.abspath(os.path.join(dirname, path)))
    return special_list
# print(get_special_paths(os.getcwd()))

def copy_to(path_list, dest_dir):
    """Copying special files"""
    os.makedirs(dest_dir)
    for path in path_list:
        shutil.copy(path, dest_dir)

    


def zip_to(path_list, dest_zip):
    """Zip up special file paths to new zip file"""
    cmd = ['zip', '-j', dest_zip]
    cmd.extend(path_list)
    #print("Command I'm going to do")
    #print(' '.join(cmd))
    #try:
    subprocess.check_output(cmd)
    # except subprocess.CalledProcessError() as e:
        #print(e.output)
        #raise
        



def main(raw_args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('dir', help='directory stuff')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    args = parser.parse_args(raw_args)
    path_list = get_special_paths(args.dir)
    # print(path_list)
    if not args:
        parser.print_usage()
        return
    if not args.dir:
        parser.print_usage()
        return
    if args.todir:
        copy_to(path_list, args.todir)
    elif args.tozip:
        zip_to(path_list, args.tozip)
    else:
        print("\n".join(path_list))
    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
