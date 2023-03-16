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

protocol = labop.Protocol('asp_disp_unit_test_labop_v0')
protocol.name = "Aspirating/Dispensing Unit Test Using LabOP v0"
protocol.description = "This protocol is a unit test designed to validate accuracy in aspirating and dispensing 10ul, written in LabOP"
doc.add(protocol)

# create the materials to be provisioned
CONT_NS = rdfl.Namespace('https://sift.net/container-ontology/container-ontology#')
OM_NS = rdfl.Namespace('http://www.ontology-of-units-of-measure.org/resource/om-2/')

PREFIX_MAP = json.dumps({"cont": CONT_NS, "om": OM_NS})

# Define reagents & tip
dh2o = sbol3.Component('dH2O', 'https://pubchem.ncbi.nlm.nih.gov/substance/24901740')
dh2o.name = 'Water, sterile-filtered, BioReagent, suitable for cell culture'
doc.add(dh2o)

p20 = sbol3.Agent('p20_single_gen2',
                  name='P20 Single GEN2')
doc.add(p20)
load = protocol.primitive_step('ConfigureRobot',
                               instrument=p20,
                               mount='left')

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

# Set up target samples
plate = protocol.primitive_step('EmptyContainer',
                                specification=spec_well_plate)
source_well = protocol.primitive_step('PlateCoordinates',
                                      source=plate.output_pin('samples'),
                                      coordinates='A1')
destination_well = protocol.primitive_step('PlateCoordinates',
                                           source=plate.output_pin('samples'),
                                           coordinates='B1')

# Pick up tip - no corresponding primitive in OT2Specialization
# Aspirate from A1 - no corresponding primitive in OT2Specialization
# Dispense into B1
dispense = protocol.primitive_step('Dispense',
                                   source=source_well.output_pin('samples'),
                                   destination=destination_well.output_pin('samples'),
                                   amount=sbol3.Measure(10, tyto.OM.microliter))
# Drop tip - no corresponding primitive in OT2Specialization


filename = "ot2_asp_disp_unit_test_labop"
agent = sbol3.Agent("ot2_machine", name="OT2 machine")
ee = ExecutionEngine(specializations=[OT2Specialization(filename)])
parameter_values = []
execution = ee.execute(protocol, agent, id="test_execution")
