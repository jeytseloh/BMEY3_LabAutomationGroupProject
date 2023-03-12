from logging import Logger
import os
import logging
import sbol3
import labop
import tyto
import uml
import json
import rdflib as rdfl
from typing import Dict, Tuple
from sbol3 import Document

from labop.execution_engine import ExecutionEngine
from labop_convert.opentrons.opentrons_specialization import OT2Specialization, REVERSE_LABWARE_MAP
from labop_convert.markdown.markdown_specialization import MarkdownSpecialization

from IPython.display import Image

# Import the primitive libraries
print('Importing libraries')
labop.import_library('liquid_handling')
print('... Imported liquid handling')
labop.import_library('plate_handling')
print('... Imported plate handling')
labop.import_library('spectrophotometry')
print('... Imported spectrophotometry')
labop.import_library('sample_arrays')
print('... Imported sample arrays')
labop.import_library('pcr')
print('... Imported pcr')

# set up the document
print('Setting up document')
doc = sbol3.Document()
sbol3.set_namespace('https://unittest.com/')

protocol = labop.Protocol('tc_gib_unit_test_labop_v0')
protocol.name = "Thermocycler Gibson Unit Test Using LabOP v0"
protocol.description = '''This protocol is a unit test designed to test thermocycler function and 
                        timing using the parameters used in the Gibson protocol, written in LabOP'''
doc.add(protocol)

# create the materials to be provisioned
CONT_NS = rdfl.Namespace('https://sift.net/container-ontology/container-ontology#')
OM_NS = rdfl.Namespace('http://www.ontology-of-units-of-measure.org/resource/om-2/')

PREFIX_MAP = json.dumps({"cont": CONT_NS, "om": OM_NS})

# Define tip & thermocycler
p20 = sbol3.Agent('p20_single_gen2',
                  name='P20 Single GEN2')
thermocycler = sbol3.Agent('thermocycler_module',
                           name='Thermocycler Module')
doc.add(p20)
doc.add(thermocycler)
load = protocol.primitive_step('ConfigureRobot',
                               instrument=p20,
                               mount='left')
load = protocol.primitive_step('ConfigureRobot',
                               instrument=thermocycler,
                               mount='7')

# Define labware
spec_tiprack = labop.ContainerSpec('tiprack',
                                   name='tiprack',
                                   queryString=REVERSE_LABWARE_MAP['opentrons_96_tiprack_10ul'],
                                #    queryString='cont:Opentrons96TipRack10uL',
                                   prefixMap=PREFIX_MAP)
spec_well_plate = labop.ContainerSpec('reagent_plate',
                                      name='Well plate for reagents',
                                      queryString=REVERSE_LABWARE_MAP['nest_96_wellplate_200ul_flat'],
                                    #   queryString='cont:NEST96WellPlate',
                                      prefixMap=PREFIX_MAP)
doc.add(spec_tiprack)
doc.add(spec_well_plate)

# Load OT2 robot with labware
load = protocol.primitive_step('LoadRackOnInstrument',
                                  rack=spec_tiprack,
                                  coordinates='1')
load = protocol.primitive_step('LoadRackOnInstrument',
                                          rack=spec_well_plate,
                                          coordinates='4')

# not sure what the equivalent of block_temperature_status is in labop