## Protocol Reference - https://github.com/Opentrons/opentrons/blob/edge/api/docs/v2/example_protocols/dilution_tutorial_multi.py 

'''
Navigate to the correct folder then type "opentrons_simulate gibson_v1.py -e" to simulate this file.
The "-e" suffix gives an estimated duration for the protocol.
The "-o nothing" suffix will hide the output for if you just want to check the protocol runs.
'''
# Default import that is always needed.
from opentrons import protocol_api
import opentrons.execute

# Most Metadata is optional but you MUST include "apiLevel"
metadata = {
    'apiLevel': '2.12',
    'protocolName': 'Gibson OT API v1.0',
    'description': '''This protocol is the first draft of the Gibson assembly protocol as given by: 
                        https://international.neb.com/protocols/2012/12/11/gibson-assembly-protocol-e5510
                         v0.1 changed labware to custom labware (well plate and pcr plate) 
                         v0.2 Changed to new tip=always for transfers excluding first transfer
                         v1.0 Optimising after first dry run: combine all H20 transfers for negative control, 
                                add p300 right pipette, and change single channel to 8 channel pipettes''',
    'author': 'New API User'
    }

# This is where you put all your protocol instructions, it is generally defined as shown below.
# def run(protocol: protocol_api.ProtocolContext):
def run(protocol: protocol_api.ProtocolContext):
    #Set up labware and initial conditions
    tc_mod = protocol.load_module('thermocycler')
    tc_mod.set_block_temperature(temperature=4, block_max_volume=40)
    tc_plate = tc_mod.load_labware('framestar_96_aluminumblock_200ul', label = 'Destination Plate')
    tiprack10 = protocol.load_labware('opentrons_96_tiprack_10ul', 1)
    tiprack300 = protocol.load_labware('opentrons_96_tiprack_300ul', 2)
    reagents = protocol.load_labware('masterblock_96_wellplate_2000ul', 4)
    p10 = protocol.load_instrument('p10_multi', 'left', tip_racks=[tiprack10])
    p300 = protocol.load_instrument('p300_multi', 'right', tip_racks=[tiprack300])
    
    #Transfer H2O - Assembly Reaction + Negative Control
    p300.transfer(16, reagents.columns_by_name()['2'], tc_plate.columns_by_name()['1'])
    p300.transfer(36, reagents.columns_by_name()['2'], tc_plate.columns_by_name()['2'])
    #Transfer Gibson Master Mix - Assembly Reaction
    p300.transfer(20, reagents.columns_by_name()['1'], tc_plate.columns_by_name()['1'])
    #Transfer DNA Fragment 1 - Assembly Reaction + Negative Control 
    p10.transfer(2, reagents.columns_by_name()['3'], tc_plate.columns_by_name()['1'])
    p10.transfer(2, reagents.columns_by_name()['3'], tc_plate.columns_by_name()['2'])
    #Transfer DNA Fragment 2 - Assembly Reaction + Negative Control 
    p10.transfer(2, reagents.columns_by_name()['4'], tc_plate.columns_by_name()['1'], mix_after=(5, 20))
    p10.transfer(2, reagents.columns_by_name()['4'], tc_plate.columns_by_name()['2'], mix_after=(5, 20))
    #Close thermocycler lid and incubate
    tc_mod.close_lid()
    tc_mod.set_lid_temperature(temperature=60)#10 degrees higher than inside 
    #Do we need to set lid temp or is this insignificant?
    tc_mod.set_block_temperature(temperature=50, hold_time_minutes=15, block_max_volume=40) # check when time starts

    # Do we need to specify new tip etc?


#Code to run protocol
#protocol = opentrons.execute.get_protocol_api('2.13')
#run(protocol)  # your protocol will now run