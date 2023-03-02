## Protocol Reference - https://github.com/Opentrons/opentrons/blob/edge/api/docs/v2/example_protocols/dilution_tutorial_multi.py 

'''
Navigate to the correct folder then type "opentrons_simulate goldengate_v0.py -e" to simulate this file.
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
    tc_plate = tc_mod.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', label = 'Destination Plate')
    tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', 1)
    reagents = protocol.load_labware('nest_96_wellplate_2ml_deep', 4)
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack])
    
    #Transfer H2O - Assembly Reaction + Negative Control
    p20.transfer(28, reagents.wells_by_name()['A1'], tc_plate.columns_by_name()['1'])
    p20.transfer(16, reagents.wells_by_name()['A1'], tc_plate.columns_by_name()['2'])
    #Transfer T4 DNA ligase buffer - Assembly Reaction + Negative Control
    p20.transfer(4, reagents.wells_by_name()['A2'], tc_plate.columns_by_name()['1'])
    p20.transfer(4, reagents.wells_by_name()['A2'], tc_plate.columns_by_name()['2'])
    #Transfer Destination Plasmid - Assembly Reaction + Negative Control
    p20.transfer(2, reagents.wells_by_name()['A3'], tc_plate.columns_by_name()['1'])
    p20.transfer(2, reagents.wells_by_name()['A3'], tc_plate.columns_by_name()['2'])
    #Transfer DNA Fragment 1 - Assembly Reaction + Negative Control 
    p20.transfer(2, reagents.wells_by_name()['A4'], tc_plate.columns_by_name()['1'])
    p20.transfer(2, reagents.wells_by_name()['A4'], tc_plate.columns_by_name()['2'])
    #Transfer DNA Fragment 2 - Assembly Reaction + Negative Control 
    p20.transfer(2, reagents.wells_by_name()['A5'], tc_plate.columns_by_name()['1'])
    p20.transfer(2, reagents.wells_by_name()['A5'], tc_plate.columns_by_name()['2'])
    #Transfer Golden Gate Enzyme Mix - Assembly Reaction 
    p20.transfer(2, reagents.wells_by_name()['A6'], tc_plate.columns_by_name()['1'], mix_after=(5, 20)) 
    #Transfer H2O -  Negative Control 
    p20.transfer(2, reagents.wells_by_name()['A1'], tc_plate.columns_by_name()['2'], mix_after=(5, 20))  
    # Define TC profile
    profile = [
    {'temperature': 37, 'hold_time_seconds': 3600},
    {'temperature': 60, 'hold_time_seconds': 300}]
    
    #Close thermocycler lid and incubate
    tc_mod.close_lid()
    #Incubate at 37 degrees for 60 minutes
    tc_mod.set_lid_temperature(temperature=47)#10 degrees higher than inside
    tc_mod.set_block_temperature(temperature=37, hold_time_minutes=60, block_max_volume=40) # check when time starts

    #Incubate at 60 degrees for 5 minutes
    tc_mod.set_lid_temperature(temperature=70)#10 degrees higher than inside
    tc_mod.set_block_temperature(temperature=60, hold_time_minutes=5, block_max_volume=40) # check when time starts


    #Do we need to specify lid temp separately here?/ Do we even need to set lid temp?
    #tc_mod.execute_profile(steps=profile, repetitions=1, block_max_volume=40)

    # Do we need to specify new tip etc?

