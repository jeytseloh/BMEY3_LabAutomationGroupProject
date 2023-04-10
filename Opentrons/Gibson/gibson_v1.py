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
    'protocolName': 'Gibson OT API v1.1',
    'description': '''This protocol is the first draft of the Gibson assembly protocol as given by: 
                        https://international.neb.com/protocols/2012/12/11/gibson-assembly-protocol-e5510
                         v0.1 changed labware to custom labware (well plate and pcr plate) 
                         v0.2 Changed to new tip=always for transfers excluding first transfer
                         v1.0 Optimising after first dry run: combine all H20 transfers for negative control, 
                                add p300 right pipette, and change single channel to 8 channel pipettes, 
                                changed incubation time to 1 min for dry runs
                        v1.1 Changed p300 multi to gen2 - could not attach gen1 to OT2 ''',
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
    tc_mod.set_block_temperature(temperature=4, block_max_volume=40) # 1. Hold at 4 (ice)

    #Transfer H2O - Assembly Reaction + Negative Control
    p300.transfer(16, reagents.wells_by_name()['A2'], tc_plate.wells_by_name()['A1']) # 2. Add 16 ul deionized H2O for assembly reaction
    p300.transfer(36, reagents.wells_by_name()['A2'], tc_plate.wells_by_name()['A2']) # 3. Add 36 ul deionized H2O for negative control
    #Transfer Gibson Master Mix - Assembly Reaction
    p300.transfer(20, reagents.wells_by_name()['A1'], tc_plate.wells_by_name()['A1']) # 4. Add 20 ul Gibson Assembly Master Mix for assembly reaction
    #Transfer DNA Fragment 1 - Assembly Reaction + Negative Control 
    p10.transfer(2, reagents.wells_by_name()['A3'], tc_plate.wells_by_name()['A1']) # 5. Add 2 ul DNA fragment 1 for assembly reaction
    p10.transfer(2, reagents.wells_by_name()['A3'], tc_plate.wells_by_name()['A2']) # 6. Add 2 ul DNA fragment 1 for negative control
    #Transfer DNA Fragment 2 - Assembly Reaction + Negative Control 
    p10.transfer(2, reagents.wells_by_name()['A4'], tc_plate.wells_by_name()['A1']) # 7. Add 2 ul DNA fragment 2 for assembly reaction
    p10.transfer(2, reagents.wells_by_name()['A4'], tc_plate.wells_by_name()['A2']) # 8. Add 2 ul DNA fragment 2 for negative control
    #Mix
    p300.pick_up_tip(tiprack300.wells_by_name()['A4'])
    p300.mix(5,20, tc_plate.wells_by_name()['A1']) # 9. Mix assembly reaction (volume 20 ul, 5 repetitions)
    p300.drop_tip()
    p300.pick_up_tip(tiprack300.wells_by_name()['A5'])
    p300.mix(5,20, tc_plate.wells_by_name()['A2']) # 10. Mix negative control (volume 20 ul, 5 repetitions)
    p300.drop_tip()
    #Close thermocycler lid and incubate
    tc_mod.close_lid()
    tc_mod.set_lid_temperature(temperature=60)#10 degrees higher than inside 
    tc_mod.set_block_temperature(temperature=50, hold_time_minutes=15, block_max_volume=40)  # 11. Incubate at 50 C for 15 minutes



#Code to run protocol
#protocol = opentrons.execute.get_protocol_api('2.13')
#run(protocol)  # your protocol will now run