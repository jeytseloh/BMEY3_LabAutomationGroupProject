## Protocol Reference - https://github.com/Opentrons/opentrons/blob/edge/api/docs/v2/example_protocols/dilution_tutorial_multi.py 

'''
Navigate to the correct folder then type "opentrons_simulate goldengate_v0.py -e" to simulate this file.
The "-e" suffix gives an estimated duration for the protocol.
The "-o nothing" suffix will hide the output for if you just want to check the protocol runs.
'''
# Default import that is always needed.
from opentrons import protocol_api
import opentrons.execute


# Most Metadata is optional but you MUST include "apiLevel"
metadata = {
    'apiLevel': '2.12',
    'protocolName': 'Golden Gate OT API v1.1',
    'description': '''This protocol is the first draft of the Golden Gate assembly protocol given by 
    https://international.neb.com/protocols/2018/10/02/golden-gate-assembly-protocol-for-using-neb-golden-gate-assembly-mix-e1601
    v0.1 changed labware to custom labware (well plate and pcr plate)
    v0.2 changed incubation time to 1 min for dry runs
    v1.0 Optimising after first dry run: combine all H20 transfers for negative control, 
                                add p300 right pipette, and change single channel to 8 channel pipettes
    v1.1 Changed p300 multi to gen2 - could not attach gen1 to OT2''',
    'author': 'New API User'
    }

# This is where you put all your protocol instructions, it is generally defined as shown below.
# def run(protocol: protocol_api.ProtocolContext):
def run(protocol: protocol_api.ProtocolContext):
    #Set up labware and initial conditions
    tc_mod = protocol.load_module('thermocycler')
    tc_plate = tc_mod.load_labware('framestar_96_aluminumblock_200ul', label = 'Destination Plate')
    tiprack10 = protocol.load_labware('opentrons_96_tiprack_10ul', 1)
    tiprack300 = protocol.load_labware('opentrons_96_tiprack_300ul', 2)
    reagents = protocol.load_labware('masterblock_96_wellplate_2000ul', 4)
    p10 = protocol.load_instrument('p10_multi', 'left', tip_racks=[tiprack10])
    p300 = protocol.load_instrument('p300_multi_gen2', 'right', tip_racks=[tiprack300])
    
    #Transfer H2O - Assembly Reaction + Negative Control
    p300.transfer(28, reagents.wells_by_name()['A1'], tc_plate.wells_by_name()['A1']) # 1. Transfer 28 ul of nuclease-free H2O (assembly reaction).
    p300.transfer(30, reagents.wells_by_name()['A1'], tc_plate.wells_by_name()['A2']) # 2. Transfer 30 ul of nuclease-free H2O (negative control).
    #Transfer T4 DNA ligase buffer - Assembly Reaction + Negative Control
    p10.transfer(4, reagents.wells_by_name()['A2'], tc_plate.wells_by_name()['A1']) # 3. Transfer 4 ul of T4 DNA ligase buffer (assembly reaction).
    p10.transfer(4, reagents.wells_by_name()['A2'], tc_plate.wells_by_name()['A2']) # 4. Transfer 4 ul of T4 DNA ligase buffer (negative control).
    #Transfer Destination Plasmid - Assembly Reaction + Negative Control
    p10.transfer(2, reagents.wells_by_name()['A3'], tc_plate.wells_by_name()['A1']) # 5. Transfer 2 ul of destination plasmid (assembly reaction).
    p10.transfer(2, reagents.wells_by_name()['A3'], tc_plate.wells_by_name()['A2']) # 6. Transfer 2 ul of destination plasmid (negative control).
    #Transfer DNA Fragment 1 - Assembly Reaction + Negative Control 
    p10.transfer(2, reagents.wells_by_name()['A4'], tc_plate.wells_by_name()['A1']) # 7. Transfer 2 ul of DNA fragment 1 (assembly reaction).
    p10.transfer(2, reagents.wells_by_name()['A4'], tc_plate.wells_by_name()['A2']) # 8. Transfer 2 ul of DNA fragment 1 (negative control).
    #Transfer DNA Fragment 2 - Assembly Reaction + Negative Control 
    p10.transfer(2, reagents.wells_by_name()['A5'], tc_plate.wells_by_name()['A1']) # 9. Transfer 2 ul of DNA fragment 2 (assembly reaction).
    p10.transfer(2, reagents.wells_by_name()['A5'], tc_plate.wells_by_name()['A2']) # 10. Transfer 2 ul of DNA fragment 2 (negative control).
    #Transfer Golden Gate Enzyme Mix - Assembly Reaction 
    p10.transfer(2, reagents.wells_by_name()['A6'], tc_plate.wells_by_name()['A1']) # 11. Transfer 2 ul of Golden Gate enzyme mix (assembly reaction).
    
    #Mix
    p300.pick_up_tip(tiprack300.wells_by_name()['A3'])
    p300.mix(5, 20, tc_plate.wells_by_name()['A1']) # 12. Mix assembly reaction (volume 20 ul, 5 repetitions)
    p300.drop_tip()
    p300.pick_up_tip(tiprack300.wells_by_name()['A4'])
    p300.mix(5, 20, tc_plate.wells_by_name()['A2']) # 13. Mix negative control (volume 20 ul, 5 repetitions)
    p300.drop_tip()
    
    #Close thermocycler lid and incubate
    tc_mod.close_lid()
    # 14. Incubate at 37 degrees for 60 minutes
    tc_mod.set_lid_temperature(temperature=47)#10 degrees higher than inside
    tc_mod.set_block_temperature(temperature=37, hold_time_minutes=1, block_max_volume=40) 
    # 15. Incubate at 60 degrees for 5 minutes
    tc_mod.set_lid_temperature(temperature=70)#10 degrees higher than inside
    tc_mod.set_block_temperature(temperature=60, hold_time_minutes=1, block_max_volume=40) 


    
