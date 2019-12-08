pub fn mass_to_fuel(mass: f32) -> f32 {
    return (mass / 3.).floor() - 2.
}
