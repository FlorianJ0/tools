from scipy import optimize
import configparser
import re

# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def f(x):  # The rosenbrock function
    print
    .5 * (1 - x[0]) ** 2 + (x[1] - x[0] ** 2) ** 2
    return .5 * (1 - x[0]) ** 2 + (x[1] - x[0] ** 2) ** 2


# print optimize.minimize(f, [5,5], method="L-BFGS-B")
def add_section_header(properties_file, header_name):
    # configparser.ConfigParser requires at least one section header in a properties file.
    # Our properties file doesn't have one, so add a header to it on the fly.
    yield '[{}]\n'.format(header_name)
    for line in properties_file:
        yield line


infile = '/home/florian/lumpedflow/trunk/Models/LiverProject/ClosedLoop/PatientModel/RightLeftLiv/headers/ConfFile/Patient_CMAR.h'

file = open(infile)

with open(infile, 'rw') as f:
    read_data = f.read()

newstring = re.sub('(Ea_RA_val)', r'tutu', read_data)

with open(infile+'.test', 'w') as f:
    f.write(newstring)
# config = configparser.ConfigParser()
# config.optionxform = str
# config = configparser.RawConfigParser()
#
# config.read_file(file)

'''
config = configparser.ConfigParser(comment_prefixes=('#', ';' ,'/','*'), inline_comment_prefixes=('#', ';','/','*'))
config = configparser.RawConfigParser()
config.optionxform = str
config.read_file(infile)
# print config.sections()
# config.get(config.sections()[0], 'Ea_RA')
'''