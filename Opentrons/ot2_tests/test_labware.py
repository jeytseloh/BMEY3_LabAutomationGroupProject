from opentrons import protocol_api
import numpy as np
import opentrons.simulate
# Constants
CANDIDATE_TIPRACK_SLOTS = [ '9', '8', '11']
PIPETTE_MOUNT = 'right'
TUBE_RACK_TYPE = 'opentrons_15_tuberack_falcon_15ml_conical'
TUBE_RACK_POSITION = '3'
DESTINATION_PLATE_TYPE = 'corning_48_wellplate_1.6ml_flat'
TEMPDECK_SLOT = '4'
TEMP = 20
TOTAL_VOL = 15
PART_VOL = 1.5
MIX_SETTINGS = (1, 3)
tiprack_num = 1
tiprack_type = 'opentrons_96_tiprack_300ul'
TIP_RACK_POSITION = '1'
PLATE_TYPE = 'corning_96_wellplate_360ul_flat'
PLATE_POSITION = '6'
DESTINATION_SLOT = '7'


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


def run(protocol: protocol_api.ProtocolContext):
	tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', TIP_RACK_POSITION)
	reservoir = protocol.load_labware('nest_12_reservoir_15ml', 5)
	p300 = protocol.load_instrument('p300_multi_gen2', PIPETTE_MOUNT, tip_racks=[tiprack])
	slots = CANDIDATE_TIPRACK_SLOTS[:tiprack_num]
	tipracks = [protocol.load_labware(tiprack_type, slot)
                for slot in slots]
	plate = protocol.load_labware(PLATE_TYPE, PLATE_POSITION)
	tube_rack = protocol.load_labware(TUBE_RACK_TYPE, TUBE_RACK_POSITION)
	tempdeck = protocol.load_module('tempdeck', TEMPDECK_SLOT)
	destination_plate = protocol.load_labware(
        DESTINATION_PLATE_TYPE, DESTINATION_SLOT)
	tempdeck.set_temperature(TEMP)
	
	

	# distribute diluent
	p300.transfer(100, reservoir['A1'], plate.rows()[0])  

	# no loop, 8-channel pipette

	# save the destination row to a variable
	row = plate.rows()[0]

	# transfer solution to first well in column
	p300.transfer(100, reservoir['A2'], row[0], mix_after=(3, 50))

	# dilute the sample down the row
	p300.transfer(100, row[:11], row[1:], mix_after=(3, 50))

	# Needed to output steps in the protocol.
	for line in protocol.commands():
		print(line)

# How you run the simulation, for Jupyter Notebooks.
protocol = opentrons.simulate.get_protocol_api('2.12')
run(protocol)  # your protocol will now run