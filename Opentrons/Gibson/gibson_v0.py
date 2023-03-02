## Protocol Reference - https://github.com/Opentrons/opentrons/blob/edge/api/docs/v2/example_protocols/dilution_tutorial_multi.py 

'''
Navigate to the correct folder then type "opentrons_simulate gibson_v0.py -e" to simulate this file.
The "-e" suffix gives an estimated duration for the protocol.
The "-o nothing" suffix will hide the output for if you just want to check the protocol runs.
'''
# Default import that is always needed.
from opentrons import protocol_api

# Most Metadata is optional but you MUST include "apiLevel"
metadata = {
    'apiLevel': '2.12',
    'protocolName': 'Serial Dilution Tutorial',
    'description': '''This protocol is the outcome of following the
                   Python Protocol API Tutorial located at
                   https://docs.opentrons.com/v2/tutorial.html. It takes a
                   solution and progressively dilutes it by transferring it
                   stepwise across a plate.''',
    'author': 'New API User'
    }

# This is where you put all your protocol instructions, it is generally defined as shown below.
# def run(protocol: protocol_api.ProtocolContext):
def run(protocol: protocol_api.ProtocolContext):
    #Set up labware and initial conditions
    tc_mod = protocol.load_module('thermocycler')
    tc_mod.set_block_temperature(temperature=4, block_max_volume=40)
    tc_plate = tc_mod.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', label = 'Destination Plate')
    tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', 1)
    reagents = protocol.load_labware('nest_96_wellplate_2ml_deep', 4)
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack])
    
    #Transfer H2O - Assembly Reaction + Negative Control
    p20.transfer(16, reagents.wells_by_name()['A2'], tc_plate.columns_by_name()['1'])
    p20.transfer(16, reagents.wells_by_name()['A2'], tc_plate.columns_by_name()['2'])
    #Transfer Gibson Master Mix - Assembly Reaction
    p20.transfer(20, reagents.wells_by_name()['A1'], tc_plate.columns_by_name()['1'])
    #Transfer H2O - Negative Control
    p20.transfer(20, reagents.wells_by_name()['A2'], tc_plate.columns_by_name()['2'])
    #Transfer DNA Fragment 1 - Assembly Reaction + Negative Control 
    p20.transfer(2, reagents.wells_by_name()['A3'], tc_plate.columns_by_name()['1'])
    p20.transfer(2, reagents.wells_by_name()['A3'], tc_plate.columns_by_name()['2'])
    #Transfer DNA Fragment 2 - Assembly Reaction + Negative Control 
    p20.transfer(2, reagents.wells_by_name()['A4'], tc_plate.columns_by_name()['1'], mix_after=(5, 20))
    p20.transfer(2, reagents.wells_by_name()['A4'], tc_plate.columns_by_name()['2'], mix_after=(5, 20))
    #Close thermocycler lid and incubate
    tc_mod.close_lid()
    tc_mod.set_lid_temperature(temperature=60)#10 degrees higher than inside 
    #Do we need to set lid temp or is this insignificant?
    tc_mod.set_block_temperature(temperature=50, hold_time_minutes=15, block_max_volume=40) # check when time starts

    # Do we need to specify new tip etc?

