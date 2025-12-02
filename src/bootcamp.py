import datetime


def get_mission_start_time() -> str:
    """
    Return the current timestamp in ISO format.

    This acts as the 'genesis block' timestamp for the 90‑day challenge.
    """
    return datetime.datetime.now().isoformat()


def announce_start() -> None:
    """
    Print the official start message for the 90‑day challenge.
    """
    start_time = get_mission_start_time()
    print(f"MISSION STARTED: {start_time}")
    print("The Green Graph protocol is active.")


if __name__ == "__main__":
    announce_start()
