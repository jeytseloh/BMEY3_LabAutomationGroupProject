import json

testname = 'goldengate_v0'

path_to_file = 'C:/Users/sonya/Documents/y3_proj/BMEY3_LabAutomationGroupProject/Tests/goldengate/SD20181230A10_Golden Gate OT API v0.2_2023-03-16T11_41_13.232Z.json'

with open(path_to_file, 'r') as f:
  data = json.load(f)
  #print(data.keys())
  #print(data["commands"])


commands = data['commands']
#
save_output = testname + '_runlogs.txt'

command_map = {
    'pickUpTip': "Picking up tip from ",
    'aspirate' : "Aspirating",
    'dispense' : "Dispensing",
    'dropTip' : "Dropping tip into ",
    'labware-0' : "Destination Plate on Thermocycler Module GEN1",
    'labware-1' : "Opentrons 96 Tip Rack 10 µL",
    #'labware-2' : "Opentrons 96 Tip Rack 300 µL on 2",
    'labware-2' : "Masterblock 96 Well Plate 2000 µL",
    'fixedTrash' : 'Opentrons Fixed Trash on 12'


}

ignore_command = ["loadLabware", "loadModule", "loadPipette", "thermocycler/openLid", "home", 'moveTo']
#print(command_map["pickUpTip"])

with open(save_output, 'w') as f:
#    
    for step in commands:
        print(step["commandType"])

        if "volume" in step["params"]:
            if step["commandType"] == 'aspirate':
                direction = ' from '
            elif step["commandType"] == 'dispense':
                direction = ' into '
            log = command_map[step["commandType"]] + " "+str(step["params"]["volume"]) + 'uL' + direction + step["params"]["wellName"] +" of "+ command_map[step["params"]["labwareId"]] +  " at " + str(step["params"]["flowRate"]) + 'uL/sec'
            f.write(str(log))
            f.write('\n')
        elif step["commandType"] in command_map.keys():
            log = command_map[step["commandType"]] + step["params"]["wellName"] + " of " +command_map[step["params"]["labwareId"]]
            f.write(str(log))
            f.write('\n')
        elif "legacyCommandText" in step["params"]:
            f.write(step["params"]["legacyCommandText"])
            f.write('\n')


