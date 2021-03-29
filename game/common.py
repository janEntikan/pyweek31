"""Constants for easier tuning in one place"""

# Track Generation constants (TG_ prefix)

TG_MAX_ROAD_X = 30          # How far out left/right the road can go from the center
TG_MAX_SKEW_PER_UNIT = 1    # How much the direction can change per one unit forwards
TG_UNITS_PER_CHUNK = 500    # How much units are generated at once for the track
TG_CHUNK_TRIGGER = 100      # How far ahead of the track end a new chunk should be added
