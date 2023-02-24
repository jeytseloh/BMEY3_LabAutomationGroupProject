from opentrons import protocol_api
import opentrons.simulate

metadata = {
    'apiLevel': '2.12',
    'protocolName': 'Golden Gate Assembly',
    'author': 'sk',
    'description': 'A script to automate the Golden Gate assembly protocol using the OpenTrons API v2',
    'scheduling': 'continuous'
}

def run(protocol: protocol_api.ProtocolContext):
    # Define the required labware and pipettes
    source_plate = protocol.load_labware("corning_96_wellplate_360ul_flat", "1")
    destination_plate = protocol.load_labware("corning_96_wellplate_360ul_flat", "2")
    tiprack = protocol.load_labware("opentrons_96_tiprack_300ul", "3")
    pipette = protocol.load_instrument("p300_multi_gen2", "left", tip_racks=[tiprack])

    # Define the wells containing the DNA fragments to be ligated
    fragment_1_well = source_plate.wells()[0]
    fragment_2_well = source_plate.wells()[1]

    # Define the destination well where the ligated DNA fragments will be collected
    destination_well = destination_plate.wells()[0]

    # Transfer the DNA fragments to the destination well
    pipette.transfer(5, fragment_1_well, destination_well, new_tip='always')
    pipette.transfer(5, fragment_2_well, destination_well, new_tip='always')

    # Add the ligation buffer and incubate the reaction mixture
    pipette.transfer(10, source_plate.wells()[2], destination_well, new_tip='always')
    protocol.delay(minutes=30)

    # Add the ligase enzyme and incubate the reaction mixture
    pipette.transfer(2, source_plate.wells()[3], destination_well, new_tip='always')
    protocol.delay(hours=2)

    # End the protocol
    protocol.comment("Golden Gate assembly complete!")




