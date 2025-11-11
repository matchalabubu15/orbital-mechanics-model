G = 6.674e-11
Ls = 2.997e+8
pi = 3.14159

sun_mass = 1.989e+30
sun_radius = 6.975e+5

p_mass_input = input("Enter the star's mass: (in kg) ")
p_radius_input = input("Enter the star's radius: (in km) ")
s_distance = float(input("Enter the distance of the planet: (in AU) "))

if p_mass_input.lower() == "sun":
    p_mass = sun_mass
else:
    p_mass = float(p_mass_input)

if p_radius_input.lower() == "sun":
    p_radius = sun_radius
else:
    p_radius = float(p_radius_input)

orbital_radius = s_distance*1.496e+11
orbital_velocity = (G * (p_mass) / orbital_radius) ** 0.5

light_time = (s_distance*1.496e+11) / Ls

T = (2*pi*orbital_radius) / orbital_velocity

print()

if orbital_velocity >= 1000:
    print(f"Orbital velocity: {orbital_velocity/1000:.2f}km/s")
else:
    print(f"Orbital velocity: {orbital_velocity:.2f}m/s")

if T >= 31536000:
    print(f"Orbital period: {T/31536000:,.2f}y")
elif T >= 86400:
    print(f"Orbital period: {T/86400:.2f}d")
else:
    print(f"Orbital period: {T/3600:.2f}h")

print()

if light_time >= 31536000:
    print(f"Light takes {light_time/31536000:,.2f} years to reach your planet!")
elif light_time >= 86400:
    print(f"Light takes {light_time/31536000:.2f} days to reach your planet!")
elif light_time >= 3600:
    print(f"Light takes {light_time/3600:.2f} hours to reach your planet!")
elif light_time >= 60:
    print(f"Light takes {light_time/60:.2f} minutes to reach your planet!")
else:
    print(f"Light takes {light_time:.2f} seconds to reach your planet!")

print()
