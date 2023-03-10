
'''
Navigate to the correct folder then type "opentrons_simulate tc_test.py -e" to simulate this file.
The "-e" suffix gives an estimated duration for the protocol.
The "-o nothing" suffix will hide the output for if you just want to check the protocol runs.
'''
# Default import that is always needed.
from opentrons import protocol_api
import opentrons.execute

# Most Metadata is optional but you MUST include "apiLevel"
metadata = {
    'apiLevel': '2.0',
    'protocolName': 'Transfer Unit Test v0',
    'description': '''This protocol is a unit test designed to validate accuracy in transferring 10ul ''',
    'author': 'New API User'
    }

# This is where you put all your protocol instructions, it is generally defined as shown below.
# def run(protocol: protocol_api.ProtocolContext):
def run(protocol: protocol_api.ProtocolContext):
    #Set up labware 
    tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', 1)
    well_plate = protocol.load_labware('nest_96_wellplate_2ml_deep', 4)
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack])
    tc_mod = protocol.load_module('thermocycler')
    print(tc_mod.block_temperature_status)
    tc_mod.set_block_temperature(temperature=4, block_max_volume=40)
    print(tc_mod.block_temperature_status)
    tc_mod.set_block_temperature(temperature=50, block_max_volume=40) # check when time starts
    print(tc_mod.block_temperature_status)
