from lettuce import *
from os import chdir
from os import getcwd
from os import mkdir
from shutil import rmtree
from subprocess import check_call

@before.each_scenario
def set_up(scenario):
    world.testDir = '/tmp/_test_repo'
    world.execDir = getcwd()

@before.each_scenario
def initialize_repository(scenario):
    mkdir(world.testDir) 
    chdir(world.testDir)
    check_call(['hg', 'init'])

@after.each_scenario
def clean_up(scenario):
    chdir(world.execDir)
    rmtree(world.testDir)

    world.spew('testDir')
    world.spew('execDir')

