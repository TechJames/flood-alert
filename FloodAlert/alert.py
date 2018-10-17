class Alert:
    def __init__(self, level, river_sea, county, region, message, polygon):
        self.level = level
        self.river_sea = river_sea
        self.county = county
        self.region = region
        self.message = message
        self.title = "{0}, {1} [{2}]".format(message, region, county)
        self.url = polygon
        self.image = "images/warn{0}.png".format(level)