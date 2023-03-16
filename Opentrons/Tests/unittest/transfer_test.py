
'''
Navigate to the correct folder then type "opentrons_simulate transfer_test.py -e" to simulate this file.
The "-e" suffix gives an estimated duration for the protocol.
The "-o nothing" suffix will hide the output for if you just want to check the protocol runs.
'''
# Default import that is always needed.
from opentrons import protocol_api
import opentrons.execute

# Most Metadata is optional but you MUST include "apiLevel"
metadata = {
    'apiLevel': '2.0',
    'protocolName': 'Transfer Unit Test v0.2',
    'description': '''This protocol is a unit test designed to validate accuracy in transferring 10ul
                       v0.1 Changed tiprack to 10ul
                        v0.2 changed labware to custom labware (well plate and pcr plate) ''',
    'author': 'New API User'
    }

# This is where you put all your protocol instructions, it is generally defined as shown below.
# def run(protocol: protocol_api.ProtocolContext):
def run(protocol: protocol_api.ProtocolContext):
    #Set up labware 
    tiprack = protocol.load_labware('opentrons_96_tiprack_10ul', 1)
    well_plate = protocol.load_labware('masterblock_96_wellplate_2000ul', 4)
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack])

    #Transfer 10ul from one well to another (1-1)
    p20.transfer(10, well_plate.wells_by_name()['A1'], well_plate.wells_by_name()['A2']) 
    #Transfer 10ul from one well to multiple wells (1 - many)
    p20.transfer(10, well_plate.wells_by_name()['A1'], well_plate.columns_by_name()['2']) 