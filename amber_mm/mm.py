#AMBER95
""" Python Program for AMBER95 framework """
import sys

from mmlib import fileio
from mmlib import molecule

if __name__ == '__main__':
    
  input_file_name = fileio.ValidateInput(__file__, sys.argv)

  molecule = molecule.Molecule(input_file_name)

  molecule.GetEnergy('nokinetic')

  molecule.PrintData()
