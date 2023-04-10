from opentrons import protocol_api

metadata = {'apiLevel': '2.11',
            'description': 'None',
            'protocolName': 'LabOP Opentrons Golden Gate Assembly Protocol'} 

def run(protocol: protocol_api.ProtocolContext):
    p10_multi = protocol.load_instrument('p10_multi', 'left')
    p300_multi = protocol.load_instrument('p300_multi', 'right')
    thermocycler_module = protocol.load_module('thermocycler module', '7')
    thermocycler_module.open_lid()
    labware1 = protocol.load_labware('opentrons_96_tiprack_10ul', '1')
    p10_multi.tip_racks.append(labware1)
    labware2 = protocol.load_labware('opentrons_96_tiprack_300ul', '2')
    p300_multi.tip_racks.append(labware2)
    labware4 = protocol.load_labware('masterblock_96_wellplate_2000ul', '4')
    labware7 = thermocycler_module.load_labware('framestar_96_aluminumblock_200ul')
    p300_multi.transfer(28.0, labware4['A1'], labware7['A1'])  # 1. Transfer 28 ul of nuclease-free H2O (assembly reaction).
    p300_multi.transfer(28.0, labware4['A1'], labware7['A2'])  # 2. Transfer 30 ul of nuclease-free H2O (negative control).
    p10_multi.transfer(4.0, labware4['A2'], labware7['A1'])  # 3. Transfer 4 ul of T4 DNA ligase buffer (assembly reaction).
    p10_multi.transfer(4.0, labware4['A2'], labware7['A2'])  # 4. Transfer 4 ul of T4 DNA ligase buffer (negative control).
    p10_multi.transfer(2.0, labware4['A3'], labware7['A1'])  # 5. Transfer 2 ul of destination plasmid (assembly reaction).
    p10_multi.transfer(2.0, labware4['A3'], labware7['A2'])  # 6. Transfer 2 ul of destination plasmid (negative control).
    p10_multi.transfer(2.0, labware4['A4'], labware7['A1'])  # 7. Transfer 2 ul of DNA fragment 1 (assembly reaction).
    p10_multi.transfer(2.0, labware4['A4'], labware7['A2'])  # 8. Transfer 2 ul of DNA fragment 1 (negative control).
    p10_multi.transfer(2.0, labware4['A5'], labware7['A1'])  # 9. Transfer 2 ul of DNA fragment 2 (assembly reaction).
    p10_multi.transfer(2.0, labware4['A5'], labware7['A2'])  # 10. Transfer 2 ul of DNA fragment 2 (negative control).
    p10_multi.transfer(2.0, labware4['A6'], labware7['A1'])  # 11. Transfer 2 ul of Golden Gate enzyme mix (assembly reaction).
    
    p300_multi.pick_up_tip(labware2.wells_by_name()['A3'])
    p300_multi.mix(5, 20.0, labware7['A1'])    # 12. Mix assembly reaction (volume 20 ul, 5 repetitions)
    p300_multi.drop_tip()
    p300_multi.pick_up_tip(labware2.wells_by_name()['A4'])
    p300_multi.mix(5, 20.0, labware7['A2'])    # 13. Mix negative control (volume 20 ul, 5 repetitions)
    p300_multi.drop_tip()
    
    # 14. Incubate at 37 degrees for 60 minutes
    thermocycler_module.close_lid()
    thermocycler_module.set_lid_temperature(temperature=47.0)
    thermocycler_module.set_block_temperature(temperature=37.0, hold_time_minutes=60.0)
    # 15. Incubate at 60 degrees for 5 minutes
    thermocycler_module.close_lid()
    thermocycler_module.set_lid_temperature(temperature=70.0)
    thermocycler_module.set_block_temperature(temperature=60.0, hold_time_minutes=5.0)
