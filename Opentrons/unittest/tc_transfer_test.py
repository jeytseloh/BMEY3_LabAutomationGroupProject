
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
    'apiLevel': '2.12',
    'protocolName': 'Thermocycler Transfer Unit Test v0.3',
    'description': '''This protocol is a unit test designed to test transfers to PCR plates in the thermocycler   
                    v0.1 Changed tiprack to 10ul
                    v0.2 changed labware to custom labware (well plate and pcr plate)
                    v.03 transfer from reagents to pcr plate in tc''',
    'author': 'New API User'
    }

# This is where you put all your protocol instructions, it is generally defined as shown below.
# def run(protocol: protocol_api.ProtocolContext):
def run(protocol: protocol_api.ProtocolContext):
    #Set up labware 
    tiprack = protocol.load_labware('opentrons_96_tiprack_10ul', 1)
    reagents = protocol.load_labware('masterblock_96_wellplate_2000ul', 4)
    tc_mod = protocol.load_module('thermocycler')
    tc_plate = tc_mod.load_labware('framestar_96_aluminumblock_200ul', label = 'Destination Plate')
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack])
    
    #print(tc_mod.block_temperature_status)
    #tc_mod.set_block_temperature(temperature=4, hold_time_minutes=1, block_max_volume=40)
    #print(tc_mod.block_temperature_status)
    #tc_mod.set_block_temperature(temperature=50, hold_time_minutes=1, block_max_volume=40) # check when time starts
    #print(tc_mod.block_temperature_status)
    p20.transfer(10, reagents.wells_by_name()['A2'], tc_plate.columns_by_name()['1'],new_tip='always')
    p20.transfer(10, reagents.wells_by_name()['A2'], tc_plate.columns_by_name()['2'], new_tip='always')
