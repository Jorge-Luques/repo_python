planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])
print("We live in ", planets[2])

number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

planets.append("Pluto") # funcion que agrega valor al final de la lista
number_of_planets = len(planets)
print("Add the planet "+planets[-1])
print("There are actually", number_of_planets, "planets in the solar system.")

planets.pop()  # funcion que elimina el ultimo valor de la lista
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650 # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "kg")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")

planets_before_earth = planets[0:2]
print("The planets before Earth"+planets_before_earth)
planets_after_earth = planets[3:]
print("The planets after Earth"+planets_after_earth)

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons #unimos listas
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort() # funcion para ordenar lista
print("The sort regular satellite moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort(reverse=True) # funcion para ordenar lista en orden inverso
print("The reverse sort regular satellite moons of Jupiter are", regular_satellite_moons)


