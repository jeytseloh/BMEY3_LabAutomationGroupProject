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
protocol.description = '''This protocol is a unit test designed to test thermocycler function and timing using the parameters used in the Gibson protocol, written in LabOP'''
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
spec_destination_plate = labop.ContainerSpec('destination_plate',
                                        name='Destination plate',
                                        queryString=REVERSE_LABWARE_MAP['biorad_96_wellplate_200ul_pcr'],
                                        # queryString='cont:BioRad96WellPCRPlate', # NEST 96 PCR
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
load = protocol.primitive_step('LoadContainerOnInstrument',
                               specification=spec_destination_plate,
                               instrument=thermocycler,
                               slots='A1:H12') # 96 wells

pcr = protocol.primitive_step('PCR',
                              denaturation_temp=sbol3.Measure(0, tyto.OM.degree_Celsius),
                              denaturation_time=sbol3.Measure(0, tyto.OM.minute),
                              annealing_temp=sbol3.Measure(0, tyto.OM.degree_Celsius),
                              annealing_time=sbol3.Measure(0, tyto.OM.second),
                              extension_temp=sbol3.Measure(0, tyto.OM.degree_Celsius),
                              extension_time=sbol3.Measure(0, tyto.OM.second),
                              cycles=1)
pcr.name = '1. Hold at 4 degrees Celsius'

pcr = protocol.primitive_step('PCR',
                              denaturation_temp=sbol3.Measure(50, tyto.OM.degree_Celsius),
                              denaturation_time=sbol3.Measure(300, tyto.OM.second),
                              annealing_temp=sbol3.Measure(0, tyto.OM.degree_Celsius),
                              annealing_time=sbol3.Measure(0, tyto.OM.second),
                              extension_temp=sbol3.Measure(0, tyto.OM.degree_Celsius),
                              extension_time=sbol3.Measure(0, tyto.OM.second),
                              cycles=1)
pcr.name = '11. Incubate at 50 degrees Celsius for 15 minutes'

filename = "ot2_tc_gibson_unit_test_labop"
agent = sbol3.Agent("ot2_machine", name="OT2 machine")
ee = ExecutionEngine(specializations=[OT2Specialization(filename)])
parameter_values = []
execution = ee.execute(protocol, agent, id="test_execution")