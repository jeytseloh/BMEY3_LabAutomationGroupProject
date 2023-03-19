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
from labop_convert.opentrons.opentrons_specialization import OT2Specialization
from labop_convert.markdown.markdown_specialization import MarkdownSpecialization

#############################################
# set up the document
print('Setting up document')
doc = sbol3.Document()
sbol3.set_namespace('https://bbn.com/scratch/')

#############################################
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

protocol = labop.Protocol('gibson_assembly_v2_0')
protocol.name = "LabOP Opentrons Gibson Assembly Protocol"
doc.add(protocol)

# create the materials to be provisioned
CONT_NS = rdfl.Namespace('https://sift.net/container-ontology/container-ontology#')
OM_NS = rdfl.Namespace('http://www.ontology-of-units-of-measure.org/resource/om-2/')

PREFIX_MAP = json.dumps({"cont": CONT_NS, "om": OM_NS})

# Define labware
# spec_tiprack = labop.ContainerSpec('tiprack',
#                                    queryString='cont:Opentrons96TipRack10uL', # didn't have 20uL tiprack
#                                    prefixMap=PREFIX_MAP)
# tiprack = protocol.primitive_step('EmptyContainer',
#                                   specification=spec_tiprack)

# print(tiprack.input_pin('specification').value.get_value())
# print(spec_tiprack)

spec_reagent_plate = labop.ContainerSpec('reagent_plate',
                                    name='Well plate for reagents',
                                    queryString='cont:NEST96WellPlate', # same as NEST 96 deep well plate?
                                    prefixMap=PREFIX_MAP)
reagent_plate = protocol.primitive_step('EmptyContainer',
                                        specification=spec_reagent_plate)
load_reagent_plate = protocol.primitive_step('LoadRackOnInstrument',
                                             rack=spec_reagent_plate,
                                             coordinates='4')

print(reagent_plate.output_pin('samples'))
