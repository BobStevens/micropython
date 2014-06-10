#!/usr/bin/python
"""
An plot of acceleromenter data
args: see usage()
"""
__author__ = """Bob Stevens - https://github.com/BobStevens"""

import getopt
import os
import sys

try:
  import matplotlib
  # use Agg to bypass X display requirement
  # matplotlib.use('Agg')
  import pylab as plt 
except:
  raise ImportError,"matplotlib.pyplot or pylab can not be imported."
try:
  import Numeric as N
except:
  try:
    import numpy as N
  except:
    raise ImportError,"numpy and/or Numeric can not be imported."

def usage():
  usage ="""Usage:
plotdata.py [options ...] file
-h, --help             help
-v, --verbose          verbose
log file must be formatted as: time,x,y,z
  """
  print usage

# DPI used both for plot figure and exported png
PLOT_DPI=100

def main(argv=None):
  if argv is None:
    argv = sys.argv
  try:
    opts, args = getopt.getopt(argv[1:], "hv", ["help", "verbose"])
  except getopt.GetoptError, err:
    # print help information and exit:
    print str(err) # will print something like "option -a not recognized"
    usage()
    return 2
  verbose = False
  inputfile = None
  if args > []:
    inputfile = args[-1]
  for o, a in opts:
    if o in("-v", '--verbose'):
      verbose = True
    elif o in ("-h", "--help"):
      usage() 
      return 2
    else:
      assert False, "unhandled option"

  # inputfile required
  if inputfile == None: 
    usage()
    return 2
    
  # load data from file, use source filename for png filename
  fileName, fileExtension = os.path.splitext(inputfile)
  if verbose: print("loading data from " + inputfile)
  # generate plot data from txt file
  data = N.genfromtxt(inputfile, delimiter=',', names=['time','x', 'y', 'z'])
  if verbose: print(data)
  # reduce margins
  pars = matplotlib.figure.SubplotParams(top=0.9,right=0.95,bottom=0.1,left=0.05)
  fig = plt.figure(figsize=(16, 8), dpi=PLOT_DPI, subplotpars=pars )
  # add the plot
  ax1 = fig.add_subplot(111, axisbg='w')
  ax1.set_title("Accelerometer")    
  ax1.set_xlabel('time')
  ax1.set_ylabel('value')
  ax1.plot(data['time'], data['x'], marker="", color='b', label='x')
  ax1.plot(data['time'], data['y'], marker="", color='r', label='y')
  ax1.plot(data['time'], data['z'], marker="", color='g', label='z')
  # add legend
  leg = ax1.legend()
  # save as png
  plt.savefig(fileName + '.png', dpi=PLOT_DPI) 
  plt.show()
  
if __name__ == "__main__":
  sys.exit(main())
    
