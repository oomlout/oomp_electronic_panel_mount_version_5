
import copy
import itertools

from requests import options

from oomp_populate_helper import build_oomp_id, write_extras


def main(**kwargs):
    
    options = []
    
    

    if True:
        option = {}
        option["type_level_1"] = "motor_controller"
        option["type_level_2"] = "stepper"
        option["type_level_3"] = "single_axis"
        option["supplier_part_number_aliexpress"] = "1005010508840160"
        option["supplier_link_aliexpress"] = "https://www.aliexpress.com/item/1005010508840160.html"
        option["width_mm"] = 86
        option["width_cutout_mm"] = 81.6
        option["height_mm"] = 45        
        option["height_cutout_mm"] = 40.6        
        option["depth_mm"] = 28
        option["depth_cutout_mm"] = 3
        option["manufacturer"] = "aliexpress"
        option["manufacturer_part_number"] = "xy_smh"
        
        options.append(copy.deepcopy(option))
        
    
    #load from working_manual.yaml
    if False:
        with open("working_manual.yaml", 'r', encoding='utf-8') as file:
            import yaml
            data = yaml.safe_load(file)
            options_yaml = data.get("options", [])
            for option_yaml in options_yaml:
                options.append(option_yaml)

    
    ###### populate taxonomy details and oobb details
    if True:
        for option in options:       
            option["taxonomy_1"] = f"electronic"  
            option["taxonomy_2"] = f"panel_mount"              
            count = 3
            if True:
                value_name = "type_level_1"
                value = option.get(value_name, None)
                if value is not None:
                    option[f"taxonomy_{count}"] = f"{value}"
                    count += 1
            if True:
                value_name = "type_level_2"
                value = option.get(value_name, None)
                if value is not None:
                    option[f"taxonomy_{count}"] = f"{value}"
                    count += 1
            if True:
                value_name = "type_level_3"
                value = option.get(value_name, None)
                if value is not None:
                    option[f"taxonomy_{count}"] = f"{value}"
                    count += 1
            if True:
                value_name = "type_level_4"
                value = option.get(value_name, None)
                if value is not None:
                    option[f"taxonomy_{count}"] = f"{value}"
                    count += 1
            if True:
                value_name = "width_mm"
                value = str(option.get(value_name, None)).replace(".", "_")
                option[f"taxonomy_{count}"] = f"{value}_mm_{value_name.replace('_mm', '')}"
                count += 1
            #height
            if True:
                value_name = "height_mm"
                value = str(option.get(value_name, None)).replace(".", "_")
                option[f"taxonomy_{count}"] = f"{value}_mm_{value_name.replace('_mm', '')}"
                count += 1
            #depth
            if True:
                value_name = "depth_mm"
                value = str(option.get(value_name, None)).replace(".", "_")
                option[f"taxonomy_{count}"] = f"{value}_mm_{value_name.replace('_mm', '')}"
                count += 1
            #manucaturer at taxonomy 14
            if True:
                value_name = "manufacturer"
                value = option.get(value_name, None)
                if value is not None:
                    option[f"taxonomy_14"] = f"{value}"
            #part number 15
            if True:
                value_name = "manufacturer_part_number"
                value = option.get(value_name, None)
                if value is not None:
                    option[f"taxonomy_15"] = f"{value}"


            if option.get("oobb_type"):
                option["oobb_details"] = {                    
                    "run_scad": option.get("run_scad", True),
                    # True: native recipe; False: off; "working_scad": shared source.
                    "run_solidcraft": option.get("run_solidcraft", False),
                }
                option["oobb_details"].update(copy.deepcopy(option))
            else:
                option["oobb_details"] = {
                    "run_scad": option.get("run_scad", False),
                    "run_solidcraft": option.get("run_solidcraft", False),
                }
            #svg details
            if False:
                pass
                svg_details = {}
                svg_details["svg_name"] = option_type
                svg_details["svg_width"] = option.get("width", None)            
                svg_details["svg_height"] = option.get("height", None)
                option["svg_details"] = svg_details

    #load the options into full list
    extras = []
    for option in options:
        extra = {}
        extra.update(option)
        extras.append(extra)

    
    ######### add notes from an id string
    import working_oomp_populate_extra_detail
    working_oomp_populate_extra_detail.main(extras=extras)


    write_extras(extras)



# Call main automatically
if __name__ == "__main__":
    main()
