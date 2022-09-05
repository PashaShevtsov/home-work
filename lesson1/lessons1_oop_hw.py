class Element:
    def __init__(self, t_melt, t_boil):
        self.t_melt = t_melt
        self.t_boil = t_boil



    def chec_agg_state(self, temp ,scale):

        if temp < self.t_melt:
            return  "solid"
        elif temp > self.t_boil:
            return "gas"
        return "liquid"

    def temp_convert(self, temp, scale='C'):
        if scale == 'F':
            return (temp-32)*5/9
        if scale == 'K':
            return temp - 273
        return temp


if __name__ == '__main__':
    alumin = Element(660, 2862)
    print(alumin.chec_agg_state(20, "K"))