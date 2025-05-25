from dataclasses import dataclass
@dataclass
class DTO():
        name: str
        lat_name: str 
        plant_type: str 
        waterconsumption: str 
        prefered_location: str 
        location: list
        pruning_time: dict
        pruning_type: str 
        toxic_cat: str 
        toxic_human: str 
        comment: str 
        