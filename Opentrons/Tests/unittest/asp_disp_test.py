## Protocol Reference - https://github.com/Opentrons/opentrons/blob/edge/api/docs/v2/example_protocols/dilution_tutorial_multi.py 

'''
Navigate to the correct folder then type "opentrons_simulate asp_disp_test.py -e" to simulate this file.
The "-e" suffix gives an estimated duration for the protocol.
The "-o nothing" suffix will hide the output for if you just want to check the protocol runs.
'''
# Default import that is always needed.
from opentrons import protocol_api
import opentrons.execute

# Most Metadata is optional but you MUST include "apiLevel"
metadata = {
    'apiLevel': '2.0',
    'protocolName': 'Aspirating/Dispensing Unit Test v0',
    'description': '''This protocol is a unit test designed to validate accuracy in aspirating and dispensing 10ul ''',
    'author': 'New API User'
    }

# This is where you put all your protocol instructions, it is generally defined as shown below.
# def run(protocol: protocol_api.ProtocolContext):
def run(protocol: protocol_api.ProtocolContext):
    #Set up labware 
    tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', 1)
    well_plate = protocol.load_labware('nest_96_wellplate_2ml_deep', 4)
    p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack])
    

    #Pick up tip
    p20.pick_up_tip(tiprack.wells()[0], presses=0)
    #Aspirate from A1
    p20.aspirate(10, location = well_plate['A1'])
    #Dispense into B1
    p20.dispense(location = well_plate['B1'])
    #Drop tip
    p20.drop_tip()

#    #Create loop
#    for well in well_plate.columns_by_name():
#        #Pick up tip
#        p20.pick_up_tip(tiprack.wells()[1], presses=0)
#        #Aspirate from column 2
#        p20.aspirate(10, location = well['2'])
#        #Dispense into column 3
#        p20.dispense(location = well['3'])

#Code to run protocol
#protocol = opentrons.execute.get_protocol_api('2.13')
#run(protocol)  # your protocol will now run