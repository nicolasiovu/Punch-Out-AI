class Actions:
    IDLE = 0
    BLOCK = 1
    DODGE_LEFT = 2
    DODGE_RIGHT = 3
    PREP_PUNCH_LEFT = 4
    PREP_PUNCH_RIGHT = 5
    PUNCH_LEFT = 6
    PUNCH_RIGHT = 8
    PUNCHED_LEFT = 9
    PUNCHED_RIGHT = 10

    NUM_ACTIONS = 11

    DECISIONS = (IDLE, BLOCK, DODGE_LEFT, DODGE_RIGHT, PUNCH_LEFT, PUNCH_RIGHT)

    str_to_action = {
        "idle": IDLE,
        "block": BLOCK,
        "dodge-left": DODGE_LEFT,
        "dodge-right": DODGE_RIGHT,
        "prep-punch-left": PREP_PUNCH_LEFT,
        "prep-punch-right": PREP_PUNCH_RIGHT,
        "punch-left": PUNCH_LEFT,
        "punch-right": PUNCH_RIGHT,
        "punched-left": PUNCHED_LEFT,
        "punched-right": PUNCHED_RIGHT
    }

    action_to_str = {
        IDLE: "idle",
        BLOCK: "block",
        DODGE_LEFT: "dodge-left",
        DODGE_RIGHT: "dodge-right",
        PREP_PUNCH_LEFT: "prep-punch-left",
        PREP_PUNCH_RIGHT: "prep-punch-right",
        PUNCH_LEFT: "punch-left",
        PUNCH_RIGHT: "punch-right",
        PUNCHED_LEFT: "punched-left",
        PUNCHED_RIGHT: "punched-right"
    }
