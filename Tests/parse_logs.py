import json

testname = 'gibson_v1'

path_to_file = 'BMEY3_LabAutomationGroupProject\Tests\gibson\ot2v1\SD20181230A10_Gibson OT API v1.1_2023-03-20T11_04_56.348Z.json'

with open(path_to_file, 'r') as f:
  data = json.load(f)
  #print(data.keys())
  #print(data["commands"])


commands = data['commands']

save_output = testname + '_runlogs.txt'

command_map = {
    'pickUpTip': "Picking up tip from ",
    'aspirate' : "Aspirating",
    'dispense' : "Dispensing",
    'dropTip' : "Dropping tip into ",
    #'framestar_96_aluminumblock_200ul' : "Framestar 96 Aluminum Block 200 Â\u00b5L on Thermocycler Module GEN1",
    'framestar_96_aluminumblock_200ul' : "Destination Plate on Thermocycler Module GEN1",
    'opentrons_96_tiprack_10ul' : "Opentrons 96 Tip Rack 10 Â\u00b5L",
    'opentrons_96_tiprack_300ul' : "Opentrons 96 Tip Rack 300 Â\u00b5L",
    'masterblock_96_wellplate_2000ul' : "Masterblock 96 Well Plate 2000 Â\u00b5L",
    'fixedTrash' : 'Opentrons Fixed Trash',
    'opentrons_96_tiprack_20ul' : "Opentrons 96 Tip Rack 20 Â\u00b5L",
    "opentrons_1_trash_1100ml_fixed" : 'Opentrons Fixed Trash',
    'nest_96_wellplate_200ul_flat' : 'NEST 96 Well Plate 200 Â\u00b5L Flat'


}


with open(save_output, 'w') as f: #opens file to write logs to
#    
    for step in commands:


        if "volume" in step["params"]: #filters aspirate and dispense commands
            
            if step["commandType"] == 'aspirate':
                direction = ' from '
                speed = '150'
            elif step["commandType"] == 'dispense':
                direction = ' into '
                speed = '300'
            for i in range(0,len(data["labware"])):
                if step["params"]["labwareId"] == data["labware"][i]["id"]:
                    labware = command_map[data["labware"][i]["loadName"]]
                   
                    try:
                        lab_slot = data["labware"][i]["location"]["slotName"] 
                    except:
                        lab_slot = data["modules"][0]["location"]["slotName"]
            log = command_map[step["commandType"]] + " "+str(step["params"]["volume"]) + '.0 uL' + direction + step["params"]["wellName"] +" of "+ labware + " on " + lab_slot +  " at " + str(step["params"]["flowRate"]) + '.0 uL/sec'
            f.write(str(log))
            f.write('\n')


        elif step["commandType"] in command_map.keys():
            for i in range(0,len(data["labware"])):
                
                if step["params"]["labwareId"] == data["labware"][i]["id"]:
                    labware = command_map[data["labware"][i]["loadName"]]
                    try:
                        lab_slot = data["labware"][i]["location"]["slotName"] 
                    except:
                        lab_slot = data["modules"][0]["location"]["slotName"]
            log = command_map[step["commandType"]] + step["params"]["wellName"] + " of " +labware+ " on " + lab_slot
            f.write(str(log))
            f.write('\n')
        elif "legacyCommandText" in step["params"]:
            f.write(step["params"]["legacyCommandText"])
            f.write('\n')


