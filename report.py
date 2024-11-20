def main():
    spacecraft = {"name": "James Web Space Telescope"}
    spacecraft.update ({"distance": "0.01" , "orbit": "Sun"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ========= REPORT =========
    
    NAME: {spacecraft["name"]}
    DISTANCE: {spacecraft.get("dsitance" , "Unknown")}
    Orbit: {spacecraft.get("orbit" , "Unknown")}

    ==========================
    """
main()
    