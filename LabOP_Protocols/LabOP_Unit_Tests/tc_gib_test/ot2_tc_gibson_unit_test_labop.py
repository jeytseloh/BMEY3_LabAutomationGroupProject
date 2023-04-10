from opentrons import protocol_api

metadata = {'apiLevel': '2.11',
            'description': 'This protocol is a unit test designed to test thermocycler function and timing using the parameters used in the Gibson protocol, written in LabOP',
            'protocolName': 'Thermocycler Gibson Unit Test Using LabOP v0'} 

def run(protocol: protocol_api.ProtocolContext):
    p20_single_gen2 = protocol.load_instrument('p20_single_gen2', 'left')
    thermocycler_module = protocol.load_module('thermocycler module', '7')
    thermocycler_module.open_lid()
    labware1 = protocol.load_labware('opentrons_96_tiprack_10ul', '1')
    p20_single_gen2.tip_racks.append(labware1)
    labware4 = protocol.load_labware('nest_96_wellplate_200ul_flat', '4')
    thermocycler_module.close_lid()
    profile = [{'temperature': 0.0, 'hold_time_seconds': 0.0}, {'temperature': 0.0, 'hold_time_seconds': 0.0}, {'temperature': 0.0, 'hold_time_seconds': 0.0}]
    thermocycler_module.execute_profile(steps=profile, repetitions=1)
    thermocycler_module.set_block_temperature(4)
    thermocycler_module.close_lid()
    profile = [{'temperature': 50.0, 'hold_time_seconds': 300.0}, {'temperature': 0.0, 'hold_time_seconds': 0.0}, {'temperature': 0.0, 'hold_time_seconds': 0.0}]
    thermocycler_module.execute_profile(steps=profile, repetitions=1)
    thermocycler_module.set_block_temperature(4)
