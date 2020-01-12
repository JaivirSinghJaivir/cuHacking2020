import json
from datetime import datetime


with open('dataset.json') as f:
    t_events = json.load(f)



class List_Pick:
    def __init__(self):
        pass


    def data_inf(self,data_name,data_type): # data name is the name of the subject (eg. Rob)
        data = {}                           # data type is the type of the subject (eg. guest-id)
        data["data_list"] = []
        for event_num in t_events.keys():
            if t_events[event_num][data_type] == data_name:
                data["data_list"].append(t_events[event_num])
        return data


    def data_sets(self,data_names,data_types): # data name set (eg. Rob, access point, 110, user connected
        data = {}                              # data type set (eg. device, device-id, event, guest-id
        data["data_set"] = []
        for name_num in data_names.keys():
            for type_num in data_types.keys():
                for event_num in t_events.keys():
                    if t_events[event_num][data_types[type_num]] == data_names[name_num]:
                        data["data_set"].append(t_events[event_num])
        return data
